# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\test\App test\interface_calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# class of main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 34))
        self.lineEdit.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 255);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.b_div = QtWidgets.QPushButton(self.centralwidget)
        self.b_div.setGeometry(QtCore.QRect(10, 60, 56, 41))
        self.b_div.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_div.setObjectName("b_div")
        self.b_mod = QtWidgets.QPushButton(self.centralwidget)
        self.b_mod.setGeometry(QtCore.QRect(90, 60, 56, 41))
        self.b_mod.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_mod.setObjectName("b_mod")
        self.b_ac = QtWidgets.QPushButton(self.centralwidget)
        self.b_ac.setGeometry(QtCore.QRect(160, 60, 56, 41))
        self.b_ac.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_ac.setObjectName("b_ac")
        self.b_divide = QtWidgets.QPushButton(self.centralwidget)
        self.b_divide.setGeometry(QtCore.QRect(230, 60, 56, 41))
        self.b_divide.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_divide.setObjectName("b_divide")
        self.b_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.b_multiply.setGeometry(QtCore.QRect(230, 110, 56, 41))
        self.b_multiply.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_multiply.setObjectName("b_multiply")
        self.b_minus = QtWidgets.QPushButton(self.centralwidget)
        self.b_minus.setGeometry(QtCore.QRect(230, 160, 56, 41))
        self.b_minus.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_minus.setObjectName("b_minus")
        self.b_plus = QtWidgets.QPushButton(self.centralwidget)
        self.b_plus.setGeometry(QtCore.QRect(230, 210, 56, 51))
        self.b_plus.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_plus.setObjectName("b_plus")
        self.b_equal = QtWidgets.QPushButton(self.centralwidget)
        self.b_equal.setGeometry(QtCore.QRect(230, 270, 56, 81))
        self.b_equal.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_equal.setObjectName("b_equal")
        self.b_point = QtWidgets.QPushButton(self.centralwidget)
        self.b_point.setGeometry(QtCore.QRect(160, 310, 56, 41))
        self.b_point.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_point.setObjectName("b_point")
        self.b_del = QtWidgets.QPushButton(self.centralwidget)
        self.b_del.setGeometry(QtCore.QRect(10, 310, 56, 41))
        self.b_del.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_del.setObjectName("b_del")
        self.b_0 = QtWidgets.QPushButton(self.centralwidget)
        self.b_0.setGeometry(QtCore.QRect(90, 310, 56, 41))
        self.b_0.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_0.setObjectName("b_0")
        self.b_7 = QtWidgets.QPushButton(self.centralwidget)
        self.b_7.setGeometry(QtCore.QRect(10, 120, 56, 41))
        self.b_7.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_7.setObjectName("b_7")
        self.b_4 = QtWidgets.QPushButton(self.centralwidget)
        self.b_4.setGeometry(QtCore.QRect(10, 180, 56, 41))
        self.b_4.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_4.setObjectName("b_4")
        self.b_1 = QtWidgets.QPushButton(self.centralwidget)
        self.b_1.setGeometry(QtCore.QRect(10, 250, 56, 41))
        self.b_1.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_1.setObjectName("b_1")
        self.b_8 = QtWidgets.QPushButton(self.centralwidget)
        self.b_8.setGeometry(QtCore.QRect(90, 120, 56, 41))
        self.b_8.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_8.setObjectName("b_8")
        self.b_9 = QtWidgets.QPushButton(self.centralwidget)
        self.b_9.setGeometry(QtCore.QRect(160, 120, 56, 41))
        self.b_9.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_9.setObjectName("b_9")
        self.b_6 = QtWidgets.QPushButton(self.centralwidget)
        self.b_6.setGeometry(QtCore.QRect(160, 180, 56, 41))
        self.b_6.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_6.setObjectName("b_6")
        self.b_3 = QtWidgets.QPushButton(self.centralwidget)
        self.b_3.setGeometry(QtCore.QRect(160, 250, 56, 41))
        self.b_3.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_3.setObjectName("b_3")
        self.b_2 = QtWidgets.QPushButton(self.centralwidget)
        self.b_2.setGeometry(QtCore.QRect(90, 250, 56, 41))
        self.b_2.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_2.setObjectName("b_2")
        self.b_5 = QtWidgets.QPushButton(self.centralwidget)
        self.b_5.setGeometry(QtCore.QRect(90, 180, 56, 41))
        self.b_5.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.b_5.setObjectName("b_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #  buttons functions
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculatrice"))
        self.b_div.setText(_translate("MainWindow", "DIV"))
        self.b_mod.setText(_translate("MainWindow", "MOD"))
        self.b_ac.setText(_translate("MainWindow", "AC"))
        self.b_divide.setText(_translate("MainWindow", "/"))
        self.b_multiply.setText(_translate("MainWindow", "x"))
        self.b_minus.setText(_translate("MainWindow", "-"))
        self.b_plus.setText(_translate("MainWindow", "+"))
        self.b_equal.setText(_translate("MainWindow", "="))
        self.b_point.setText(_translate("MainWindow", "."))
        self.b_del.setText(_translate("MainWindow", "DEL"))
        self.b_0.setText(_translate("MainWindow", "0"))
        self.b_7.setText(_translate("MainWindow", "7"))
        self.b_4.setText(_translate("MainWindow", "4"))
        self.b_1.setText(_translate("MainWindow", "1"))
        self.b_8.setText(_translate("MainWindow", "8"))
        self.b_9.setText(_translate("MainWindow", "9"))
        self.b_6.setText(_translate("MainWindow", "6"))
        self.b_3.setText(_translate("MainWindow", "3"))
        self.b_2.setText(_translate("MainWindow", "2"))
        self.b_5.setText(_translate("MainWindow", "5"))



    
