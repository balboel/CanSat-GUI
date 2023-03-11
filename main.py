import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWebEngineWidgets import QWebEngineView

import folium
import io
import serial
from serial.tools.list_ports import comports
import random
from random import randint

import mqtt_publisher

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import pandas as pd


#import GUI file
from ui_guiv1 import *

#import csv for sim
import csv

#import custom widget


from collections import deque
import time


#mainwindow class
class MainWindow(QMainWindow):
    ser = serial.Serial()
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1011, 620)
        self.readSerial()
        self.getData()
        self.gps_loc()
        self.voltage_graph()
        self.alt_graph()
        self.pressure_graph()
        self.temp_graph()
        self.show()

        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.ui.voltage_graph_cont.addWidget(self.voltageGraph)

        self.ui.start_btn.clicked.connect(self.start)
        self.ui.stop_btn.clicked.connect(self.stop)
        self.ui.send_btn.clicked.connect(self.send)

        self.ui.altitude_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.altitude))
        self.ui.temperature_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.temperature))
        self.ui.voltage_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.voltage))
        self.ui.gps_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.gps))
        self.ui.pressure_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pressure))

        self.sim = False
        self.state = False
    def enable_sim(self):
        self.sim = True

    def sim_mode(self):
        if self.sim == True:
            print('read csv') #dicari dulu caranya
        else:
            print('Press enable simulation first')
        
    def readSerial(self):
        self.baudrate = 9600
        self.list_port = comports()
        print("the available port:")
        for port in sorted(self.list_port):
            print(("{}".format(port)))
        self.serial_port = input('write serial port name:')
        try:
            self.ser = serial.Serial(self.serial_port, self.baudrate)
        except serial.serialutil.SerialException:
            self.randomSample = True
            print("Graph is showing random number")


    def isOpen(self):
        return self.ser.isOpen()

    def randomNumber(self):
        return self.randomSample

    def getData(self):
        if(self.randomNumber == False):
            value = self.ser.readline() #read single value line
            decoded_bytes = str(value[0:len(value) - 2].decode("utf-8"))
            value_chain = decoded_bytes.split(",")
        else:
            value_chain = [0] + random.sample(range(0,300), 1) + \
                [random.getrandbits(1)] + random.sample(range(0, 20), 8)
        return value_chain

    def logging(self, data):
        if self.state == True:
            data.append(time.asctime())
            with open("log.csv", "a") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(data)

    def start(self):
        self.state = True
        print('start saving to csv')

    def send(self):
        print("Command has been send")
    

    def stop(self):
        self.state = False
        print('stop saving to csv')

    def gps_loc(self):
        coordinate = (-6.990360, 110.422859)
        map = folium.Map(
            zoom_start= 13,
            location= coordinate,
            control_scale=True,
            max_bounds=True
        )
        folium.Marker([-6.990360, 110.422859], popup= coordinate).add_to(map)
        data = io.BytesIO()
        map.save(data, close_file=False)

        self.gps = QWebEngineView(self.ui.scrollAreaWidgetContents)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gps.sizePolicy().hasHeightForWidth())
        self.gps.setSizePolicy(sizePolicy2)
        self.gps.setMinimumSize(QSize(0, 0))
        self.gps.setHtml(data.getvalue().decode())

        self.ui.verticalLayout_21.addWidget(self.gps)

    def voltage_graph(self):
        self.voltageGraph = PlotWidget(self.ui.frame_22)
        self.voltagePlot = self.voltageGraph.plot(pen=(255,0,0))
        self.voltageData = np.linspace(0,0,30)
        self.point1 = 0

        self.voltageGraph.setBackground('w')

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.voltageGraph.sizePolicy().hasHeightForWidth())
        self.voltageGraph.setSizePolicy(sizePolicy)
        self.voltageGraph.setMinimumSize(QSize(0,300))


    def temp_graph(self):
        self.tempGraph = PlotWidget(self.ui.frame_17)
        self.tempPlot = self.tempGraph.plot(pen=(255,0,0))
        self.tempData = np.linspace(0,0,30)
        self.pt = 0

        self.tempGraph.setBackground('w')

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.tempGraph.sizePolicy().hasHeightForWidth())
        self.ui.temperature_graph_cont.addWidget(self.tempGraph)

    def pressure_graph(self):
        self.pressureGraph = PlotWidget(self.ui.frame_24)
        self.pressurePlot = self.pressureGraph.plot(pen=(255,0,0))
        self.pressureData = np.linspace(0,0,30)
        self.pt1 = 0

        self.pressureGraph.setBackground('w')
        self.ui.pressure_graph_cont.addWidget(self.pressureGraph)

    def alt_graph(self):
        self.altGraph = PlotWidget(self.ui.frame_18)
        self.altPlot = self.altGraph.plot(pen=(255,0,0))
        self.altData = np.linspace(0,0,30)
        self.pt2 = 0

        self.altGraph.setBackground('w')
        self.ui.altitude_graph_cont.addWidget(self.altGraph)

    def update_voltage(self, value):
        self.voltageData[:-1] = self.voltageData[1:]
        self.voltageData[-1] = float(value)
        self.point1 += 1
        self.voltagePlot.setData(self.voltageData)
        self.voltagePlot.setPos(self.point1, 0)
    
    def update_temp(self, value):
        self.tempData[:-1] = self.tempData[1:]
        self.tempData[-1] = float(value)
        self.pt += 1
        self.tempPlot.setData(self.tempData)
        self.tempPlot.setPos(self.pt, 0)

    def update_pressure(self, value):
        self.pressureData[:-1] = self.pressureData[1:]
        self.pressureData[-1] = float(value)
        self.pt1 += 1
        self.pressurePlot.setData(self.pressureData)
        self.pressurePlot.setPos(self.pt1, 0)

    def update_alt(self, value):
        self.altData[:-1] = self.altData[1:]
        self.altData[-1] = float(value)
        self.pt2 += 1
        self.altPlot.setData(self.altData)
        self.altPlot.setPos(self.pt2, 0)

    def update(self):
        self.value_chain = []
        self.value_chain = self.getData()
        self.update_alt(self.value_chain[1])
        self.update_temp(self.value_chain[3])
        self.update_voltage(self.value_chain[2])
        self.update_pressure(self.value_chain[4])
        



        self.logging(self.value_chain)
        

    
    
#execute
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



        