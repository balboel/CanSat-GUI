from random import randint
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

import numpy as np
import pandas as pd
#import custom widget
from Custom_Widgets.Widgets import *

def altitude_graph(self):

        self.graphicsView = PlotWidget(self.frame_18)
        self.graphicsView.setObjectName(u"graphicsView")
        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]

        self.graphicsView.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))

        self.data_line =  self.graphicsView.plot(self.x, self.y, pen=pen)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QSize(0,300))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.altitude_graph_cont.addWidget(self.graphicsView)

def get_next_data():
        data = pd.read_csv('telemetry.csv')
        altitude = np.array(data['pressure'])
        try:
                altitude_value = altitude[-1]*10
                return altitude_value
        except:
                return

def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data