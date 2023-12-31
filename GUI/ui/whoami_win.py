# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\WhoamiWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 700)
        Form.setMinimumSize(QtCore.QSize(700, 400))
        Form.setMaximumSize(QtCore.QSize(1600, 800))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 45))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ip = QtWidgets.QLabel(self.widget)
        self.label_ip.setMinimumSize(QtCore.QSize(0, 30))
        self.label_ip.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout.addWidget(self.label_ip)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_ip.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_ip.setMaximumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(11)
        self.lineEdit_ip.setFont(font)
        self.lineEdit_ip.setReadOnly(False)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.horizontalLayout.addWidget(self.lineEdit_ip)
        self.label_port = QtWidgets.QLabel(self.widget)
        self.label_port.setMinimumSize(QtCore.QSize(0, 30))
        self.label_port.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout.addWidget(self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_port.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_port.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_port.setFont(font)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout.addWidget(self.lineEdit_port)
        self.startserver_btn = QtWidgets.QPushButton(self.widget)
        self.startserver_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.startserver_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.startserver_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startserver_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/start_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startserver_btn.setIcon(icon)
        self.startserver_btn.setObjectName("startserver_btn")
        self.horizontalLayout.addWidget(self.startserver_btn)
        spacerItem = QtWidgets.QSpacerItem(660, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_mainnode = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_mainnode.setMinimumSize(QtCore.QSize(130, 30))
        self.lineEdit_mainnode.setMaximumSize(QtCore.QSize(140, 40))
        self.lineEdit_mainnode.setText("")
        self.lineEdit_mainnode.setObjectName("lineEdit_mainnode")
        self.horizontalLayout.addWidget(self.lineEdit_mainnode)
        self.connect_node_btn = QtWidgets.QPushButton(self.widget)
        self.connect_node_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.connect_node_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.connect_node_btn.setText("")
        self.connect_node_btn.setIcon(icon)
        self.connect_node_btn.setObjectName("connect_node_btn")
        self.horizontalLayout.addWidget(self.connect_node_btn)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.add_document_btn = QtWidgets.QPushButton(self.widget_3)
        self.add_document_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.add_document_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.add_document_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/add_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_document_btn.setIcon(icon1)
        self.add_document_btn.setObjectName("add_document_btn")
        self.horizontalLayout_2.addWidget(self.add_document_btn)
        self.del_document_btn = QtWidgets.QPushButton(self.widget_3)
        self.del_document_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.del_document_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.del_document_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/del_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_document_btn.setIcon(icon2)
        self.del_document_btn.setObjectName("del_document_btn")
        self.horizontalLayout_2.addWidget(self.del_document_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_3)
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1054, 462))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mydocx_treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.mydocx_treeWidget.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.mydocx_treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mydocx_treeWidget.setObjectName("mydocx_treeWidget")
        self.verticalLayout_2.addWidget(self.mydocx_treeWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_3.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_ip.setText(_translate("Form", "IP"))
        self.lineEdit_ip.setText(_translate("Form", "127.0.0.1"))
        self.label_port.setText(_translate("Form", "PORT"))
        self.lineEdit_port.setText(_translate("Form", "5000"))
        self.label_3.setText(_translate("Form", "Путь:"))
        self.label_5.setText(_translate("Form", "Документы:"))
import resorse_rc
