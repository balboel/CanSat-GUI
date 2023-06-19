from random import randint
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

import numpy as np
import pandas as pd
#import custom widget
from Custom_Widgets.Widgets import *

def voltage_graph(self):

        self.voltageGraph = PlotWidget(self.frame_22)
        self.voltageGraph.setObjectName(u"voltageGraph")
        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]

        self.voltageGraph.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.voltageGraph.plot(self.x, self.y, pen=pen)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.voltageGraph.sizePolicy().hasHeightForWidth())
        self.voltageGraph.setSizePolicy(sizePolicy)
        self.voltageGraph.setMinimumSize(QSize(0,300))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.voltage_graph_cont.addWidget(self.voltageGraph)

def get_next_data():
        data = pd.read_csv('nama_csv')
        voltage = np.array(data['kolom temp'])
        try:
                voltage_value = voltage[-1]*10
                return voltage_value
        except:
                return

def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data