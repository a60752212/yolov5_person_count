# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 679)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 2, 8, 1)
        self.PB_stop = QtWidgets.QPushButton(self.centralwidget)
        self.PB_stop.setObjectName("PB_stop")
        self.gridLayout.addWidget(self.PB_stop, 4, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_out = QtWidgets.QLabel(self.centralwidget)
        self.label_out.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_out.sizePolicy().hasHeightForWidth())
        self.label_out.setSizePolicy(sizePolicy)
        self.label_out.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_out.setText("")
        self.label_out.setObjectName("label_out")
        self.gridLayout_3.addWidget(self.label_out, 1, 1, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.label_title2 = QtWidgets.QLabel(self.centralwidget)
        self.label_title2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title2.setFont(font)
        self.label_title2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title2.setStyleSheet("")
        self.label_title2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title2.setObjectName("label_title2")
        self.horizontalLayout_13.addWidget(self.label_title2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        self.label_title1_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_title1_2.sizePolicy().hasHeightForWidth())
        self.label_title1_2.setSizePolicy(sizePolicy)
        self.label_title1_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title1_2.setFont(font)
        self.label_title1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title1_2.setStyleSheet("")
        self.label_title1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title1_2.setObjectName("label_title1_2")
        self.horizontalLayout_18.addWidget(self.label_title1_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.label_in = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_in.sizePolicy().hasHeightForWidth())
        self.label_in.setSizePolicy(sizePolicy)
        self.label_in.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_in.setText("")
        self.label_in.setObjectName("label_in")
        self.gridLayout_3.addWidget(self.label_in, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 3, 8, 5)
        self.PB_predict = QtWidgets.QPushButton(self.centralwidget)
        self.PB_predict.setObjectName("PB_predict")
        self.gridLayout.addWidget(self.PB_predict, 4, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 0, 1, 8)
        self.PB_c2 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_c2.setObjectName("PB_c2")
        self.gridLayout.addWidget(self.PB_c2, 5, 1, 1, 1)
        self.PB_c1 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_c1.setObjectName("PB_c1")
        self.gridLayout.addWidget(self.PB_c1, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.RB_camera = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RB_camera.sizePolicy().hasHeightForWidth())
        self.RB_camera.setSizePolicy(sizePolicy)
        self.RB_camera.setObjectName("RB_camera")
        self.horizontalLayout_5.addWidget(self.RB_camera)
        self.RB_url = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_url.setObjectName("RB_url")
        self.horizontalLayout_5.addWidget(self.RB_url)
        self.RB_img = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.RB_img.sizePolicy().hasHeightForWidth())
        self.RB_img.setSizePolicy(sizePolicy)
        self.RB_img.setObjectName("RB_img")
        self.horizontalLayout_5.addWidget(self.RB_img)
        self.PB_import = QtWidgets.QPushButton(self.centralwidget)
        self.PB_import.setObjectName("PB_import")
        self.horizontalLayout_5.addWidget(self.PB_import)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 2, 2)
        self.listWidget_out = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_out.setFont(font)
        self.listWidget_out.setStyleSheet("background-color:transparent")
        self.listWidget_out.setObjectName("listWidget_out")
        self.gridLayout.addWidget(self.listWidget_out, 8, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.PB_setThres = QtWidgets.QPushButton(self.centralwidget)
        self.PB_setThres.setObjectName("PB_setThres")
        self.horizontalLayout.addWidget(self.PB_setThres)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)
        self.gridLayout.setColumnStretch(7, 10)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_helmet_clothes = QtWidgets.QAction(MainWindow)
        self.action_helmet_clothes.setObjectName("action_helmet_clothes")
        self.action_weight = QtWidgets.QAction(MainWindow)
        self.action_weight.setObjectName("action_weight")
        self.action_loadmodel = QtWidgets.QAction(MainWindow)
        self.action_loadmodel.setObjectName("action_loadmodel")
        self.action_jump = QtWidgets.QAction(MainWindow)
        self.action_jump.setObjectName("action_jump")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PB_stop.setText(_translate("MainWindow", "停止"))
        self.label_title2.setText(_translate("MainWindow", "输出"))
        self.label_title1_2.setText(_translate("MainWindow", "输入"))
        self.PB_predict.setText(_translate("MainWindow", "开始"))
        self.PB_c2.setText(_translate("MainWindow", "选择离开区域(双向)"))
        self.PB_c1.setText(_translate("MainWindow", "选择进入区域(双向)"))
        self.RB_camera.setText(_translate("MainWindow", "摄像头"))
        self.RB_url.setText(_translate("MainWindow", "RTSP"))
        self.RB_img.setText(_translate("MainWindow", "视频"))
        self.PB_import.setText(_translate("MainWindow", "打开"))
        self.label.setText(_translate("MainWindow", "人数阈值:"))
        self.PB_setThres.setText(_translate("MainWindow", "确定"))
        self.action_helmet_clothes.setText(_translate("MainWindow", "头盔/反光衣"))
        self.action_weight.setText(_translate("MainWindow", "选择权重文件"))
        self.action_loadmodel.setText(_translate("MainWindow", "载入模型"))
        self.action_jump.setText(_translate("MainWindow", "tiaozhuan"))