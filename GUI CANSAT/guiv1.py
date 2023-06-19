from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 537)
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
"#gps, #voltage\n"
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
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(30, 30))
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setPixmap(QPixmap(u":/icons/ionicons/stats-chart-outline.svg"))
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
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/ionicons/thermometer-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/ionicons/globe-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/ionicons/map-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/ionicons/flash-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/ionicons/send-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.left_menu_widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/ionicons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/ionicons/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.pushButton_8)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 60))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 3, 0)
        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_9 = QPushButton(self.frame_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u":/icons/ionicons/reorder-four-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_3.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_6.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_11)

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
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
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
        self.gridLayout = QGridLayout(self.frame_17)
        self.gridLayout.setObjectName(u"gridLayout")

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
        self.gridLayout_2 = QGridLayout(self.frame_18)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

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


        self.verticalLayout_13.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.gps)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_20)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout_13.addWidget(self.frame_20)

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
        self.gridLayout_4 = QGridLayout(self.frame_22)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.verticalLayout_15.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.voltage)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFont(font1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.size_grip = QFrame(self.frame_14)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setGeometry(QRect(120, 20, 120, 80))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_14)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"FLIGHT MONITORING", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"MQTT", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_9.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
    # retranslateUi

