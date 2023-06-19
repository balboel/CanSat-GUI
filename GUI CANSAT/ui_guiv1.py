# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiv1qgxPcU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 571)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"color:#fff;\n"
"font-size:12px;\n"
"border: nine;\n"
"background: none;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(26, 101, 158);\n"
"}\n"
"#left_menu_widget, #temperature, #altitude,\n"
"#gps, #voltage, #pressure, #command\n"
"{\n"
"background-color: rgba(0, 78, 137, 100);\n"
"}\n"
"\n"
"#header_frame, #frame_3, #frame_5{\n"
"background-color: rgb(255, 107, 53);\n"
"}\n"
"\n"
"#frame_4 QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(239, 239, 208, 100);\n"
"}\n"
"\n"
"#header_nav QPushButton{\n"
"		background-color: rgb(255, 107, 53);\n"
"		\n"
"}\n"
"\n"
"#header_nav QPushButton:hover{\n"
"		background-color: rgb(239, 239, 208);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_widget = QCustomSlideMenu(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 11, 0, 11)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(30, 30))
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setPixmap(QPixmap(u":/icons/ionicons/logo-diposonda.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_9)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Poppins")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.temperature_btn = QPushButton(self.frame_4)
        self.temperature_btn.setObjectName(u"temperature_btn")
        self.temperature_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/ionicons/thermometer-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.temperature_btn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.temperature_btn)

        self.altitude_btn = QPushButton(self.frame_4)
        self.altitude_btn.setObjectName(u"altitude_btn")
        self.altitude_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/ionicons/globe-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.altitude_btn.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.altitude_btn)

        self.gps_btn = QPushButton(self.frame_4)
        self.gps_btn.setObjectName(u"gps_btn")
        self.gps_btn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/ionicons/map-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gps_btn.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.gps_btn)

        self.voltage_btn = QPushButton(self.frame_4)
        self.voltage_btn.setObjectName(u"voltage_btn")
        self.voltage_btn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/ionicons/flash-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.voltage_btn.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.voltage_btn)

        self.pressure_btn = QPushButton(self.frame_4)
        self.pressure_btn.setObjectName(u"pressure_btn")
        self.pressure_btn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/ionicons/rocket-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pressure_btn.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.pressure_btn)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mqtt_btn = QPushButton(self.frame_5)
        self.mqtt_btn.setObjectName(u"mqtt_btn")
        self.mqtt_btn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/ionicons/send-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mqtt_btn.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.mqtt_btn)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.left_menu_widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.start_btn = QPushButton(self.frame_6)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/ionicons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.frame_6)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/ionicons/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.stop_btn)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(11, 0, 0, 0)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 60))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 3, 0)
        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_11, 0, Qt.AlignLeft)

        self.label_3 = QLabel(self.header_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.header_nav = QFrame(self.header_frame)
        self.header_nav.setObjectName(u"header_nav")
        self.header_nav.setFrameShape(QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.header_nav)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.minimize_window_button = QPushButton(self.header_nav)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMinimumSize(QSize(30, 30))
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/icons/ionicons/remove-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_nav)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icons/ionicons/resize-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_nav)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMaximumSize(QSize(30, 30))
        icon10 = QIcon()
        icon10.addFile(u":/icons/ionicons/close-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.close_window_button)


        self.horizontalLayout_3.addWidget(self.header_nav, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.header_frame)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777211, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.temperature = QWidget()
        self.temperature.setObjectName(u"temperature")
        self.verticalLayout_8 = QVBoxLayout(self.temperature)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_16 = QFrame(self.temperature)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_16)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.frame_17 = QFrame(self.temperature)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.temperature_graph_cont = QGridLayout(self.frame_17)
        self.temperature_graph_cont.setObjectName(u"temperature_graph_cont")

        self.verticalLayout_8.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.temperature)
        self.altitude = QWidget()
        self.altitude.setObjectName(u"altitude")
        self.verticalLayout_11 = QVBoxLayout(self.altitude)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_19 = QFrame(self.altitude)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_19)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.frame_19)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.altitude)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.altitude_graph_cont = QGridLayout(self.frame_18)
        self.altitude_graph_cont.setObjectName(u"altitude_graph_cont")

        self.verticalLayout_11.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.altitude)
        self.gps = QWidget()
        self.gps.setObjectName(u"gps")
        self.verticalLayout_13 = QVBoxLayout(self.gps)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_21 = QFrame(self.gps)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_21)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.frame_21)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.frame_21)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)


        self.verticalLayout_13.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.gps)
        self.voltage = QWidget()
        self.voltage.setObjectName(u"voltage")
        self.verticalLayout_15 = QVBoxLayout(self.voltage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_23 = QFrame(self.voltage)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_23)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.frame_23)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_8, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.voltage)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.voltage_graph_cont = QGridLayout(self.frame_22)
        self.voltage_graph_cont.setObjectName(u"voltage_graph_cont")

        self.verticalLayout_15.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.voltage)
        self.pressure = QWidget()
        self.pressure.setObjectName(u"pressure")
        self.verticalLayout_6 = QVBoxLayout(self.pressure)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_25 = QFrame(self.pressure)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_25)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_10 = QLabel(self.frame_25)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.pressure)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.pressure_graph_cont = QGridLayout(self.frame_24)
        self.pressure_graph_cont.setObjectName(u"pressure_graph_cont")

        self.verticalLayout_6.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.pressure)
        self.csv = QWidget()
        self.csv.setObjectName(u"csv")
        self.verticalLayout_7 = QVBoxLayout(self.csv)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_27 = QFrame(self.csv)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_27)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_11 = QLabel(self.frame_27)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.csv)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.voltage_graph_cont_3 = QGridLayout(self.frame_26)
        self.voltage_graph_cont_3.setObjectName(u"voltage_graph_cont_3")

        self.verticalLayout_7.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.csv)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.command = QLineEdit(self.frame)
        self.command.setObjectName(u"command")
        self.command.setGeometry(QRect(10, 50, 78, 20))
        self.enable_sim = QPushButton(self.frame)
        self.enable_sim.setObjectName(u"enable_sim")
        self.enable_sim.setGeometry(QRect(10, 10, 69, 21))
        self.enable_sim.setFont(font)
        self.send_cmd = QPushButton(self.frame)
        self.send_cmd.setObjectName(u"send_cmd")
        self.send_cmd.setGeometry(QRect(10, 80, 71, 28))
        self.send_cmd.setFont(font)

        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.footer_frame = QFrame(self.frame_2)
        self.footer_frame.setObjectName(u"footer_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.footer_frame.sizePolicy().hasHeightForWidth())
        self.footer_frame.setSizePolicy(sizePolicy2)
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.footer_frame)
        self.frame_13.setObjectName(u"frame_13")
        font2 = QFont()
        self.frame_13.setFont(font2)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_17.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.footer_frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.size_grip = QFrame(self.frame_14)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.size_grip, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.frame_14)


        self.verticalLayout_5.addWidget(self.footer_frame, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"FLIGHT MONITORING", None))
        self.temperature_btn.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.altitude_btn.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.gps_btn.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.voltage_btn.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.pressure_btn.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.mqtt_btn.setText(QCoreApplication.translate("MainWindow", u"MQTT", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Command", None))
        self.enable_sim.setText(QCoreApplication.translate("MainWindow", u"ENABLE SIM", None))
        self.send_cmd.setText(QCoreApplication.translate("MainWindow", u"SEND CMD", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
    # retranslateUi

