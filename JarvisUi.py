# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1170, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-24, -8, 1221, 611))
        self.bg.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bg.setObjectName("bg")
        self.bg_border = QtWidgets.QLabel(self.centralwidget)
        self.bg_border.setGeometry(QtCore.QRect(0, 0, 1171, 601))
        self.bg_border.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"BORDER:2px Solid White;")
        self.bg_border.setText("")
        self.bg_border.setObjectName("bg_border")
        self.CLOSE_Button = QtWidgets.QPushButton(self.centralwidget)
        self.CLOSE_Button.setGeometry(QtCore.QRect(1010, 530, 141, 51))
        self.CLOSE_Button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:rgb(255,255,255);\n"
"border:1px solid white;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.CLOSE_Button.setObjectName("CLOSE_Button")
        self.START_Button = QtWidgets.QPushButton(self.centralwidget)
        self.START_Button.setGeometry(QtCore.QRect(840, 530, 141, 51))
        self.START_Button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:rgb(255,255,255);\n"
"border:1px solid white;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.START_Button.setObjectName("START_Button")
        self.Gif = QtWidgets.QLabel(self.centralwidget)
        self.Gif.setGeometry(QtCore.QRect(10, 10, 581, 401))
        self.Gif.setStyleSheet("border:1.5px solid white;")
        self.Gif.setText("")
        self.Gif.setPixmap(QtGui.QPixmap("../UI/VoiceReg/Siri_1.gif"))
        self.Gif.setScaledContents(True)
        self.Gif.setObjectName("Gif")
        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(620, 10, 541, 401))
        self.Gif_2.setStyleSheet("background-color:rgb(0,0,0);\n"
"border-color:rgb(255,255,255);\n"
"border:1.5px solid white;")
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("../UI/ExtraGui/B.G_Template_1.gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(880, 450, 221, 61))
        self.Time.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border:1.5px solid white;\n"
"color: rgb(255, 255, 255);")
        self.Time.setObjectName("Time")
        self.Terminal = QtWidgets.QLabel(self.centralwidget)
        self.Terminal.setGeometry(QtCore.QRect(10, 420, 821, 171))
        self.Terminal.setStyleSheet("border:1.5px solid white;\n"
"border -color:rgb(255,255,255)")
        self.Terminal.setText("")
        self.Terminal.setObjectName("Terminal")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bg.setText(_translate("MainWindow", "l"))
        self.CLOSE_Button.setText(_translate("MainWindow", "CLOSE Jarvis"))
        self.START_Button.setText(_translate("MainWindow", "START Jarvis"))
        self.Time.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())