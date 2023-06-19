from random import randint
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import pandas as pd

import numpy as np

#import custom widget
from Custom_Widgets.Widgets import *

def temp_graph(self):

        self.tempGraph = PlotWidget(self.frame_17)
        self.tempGraph.setObjectName(u"tempGraph")
        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]

        self.tempGraph.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.tempGraph.plot(self.x, self.y, pen=pen)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.tempGraph.sizePolicy().hasHeightForWidth())
        self.tempGraph.setSizePolicy(sizePolicy)
        self.tempGraph.setMinimumSize(QSize(0,300))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.temperature_graph_cont.addWidget(self.tempGraph)

def get_next_data():
        data = pd.read_csv('nama_csv')
        temperature = np.array(data['kolom temp'])
        try:
                temperature_value = temperature[-1]*10
                return temperature_value
        except:
                return
        
def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data

