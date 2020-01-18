# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

## create by yuval_zohar.
## enter the sentence and typing it the fast and accurate you can !


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import keyboard
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.randomse = QtWidgets.QLabel(self.centralwidget)
        self.randomse.setGeometry(QtCore.QRect(30, 100, 531, 51))
        self.randomse.setObjectName("randomse")
        self.count=0
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 180, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton_5")
        self.pushButton.clicked.connect(self.accordingly)
        self.newgame = QtWidgets.QPushButton(self.centralwidget)
        self.newgame.setGeometry(QtCore.QRect(350, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.newgame.setFont(font)
        self.newgame.setObjectName("newgame")
        self.newgame.clicked.connect(self.new_game)
        self.Head = QtWidgets.QLabel(self.centralwidget)
        self.Head.setGeometry(QtCore.QRect(250, 30, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Head.setFont(font)
        self.Head.setObjectName("Head")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 190, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 250, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.wrong = QtWidgets.QLabel(self.centralwidget)
        self.wrong.setGeometry(QtCore.QRect(11, 150, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wrong.setFont(font)
        self.wrong.setObjectName("label")
        self.wrong.hide()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 250, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 250, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.random_sentence()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def timer(self):
        second=3
        while second>0:
            self.randomse.setText(str(second))
            time.sleep(1)
            second-=1
    def random_sentence(self):
        lines = open('sentences.txt').read().splitlines()
        myline =random.choice(lines)
        self.randomse.setText(myline)
        self.t0=time.time()
    def calc_grade(self):
        if self.total>10:
            self.label_3.setText(("Grade: Bad"))
        if self.total>=7 and self.total<=10:
            self.label_3.setText(("Grade: Ok.."))
        if self.total>=5 and self.total<7:
            self.label_3.setText(("Grade: Nice!"))
        if self.total>=2 and self.total<5:
            self.label_3.setText(("Grade: Wow!"))
    def accordingly(self):
        self.curr_text=self.randomse.text()
        self.mytext=self.textEdit.toPlainText()
        print(self.mytext)
        print(self.curr_text)
        if self.curr_text!=self.mytext:
            self.wrong.show()
            self.count+=1
            
        if self.curr_text==self.mytext:
            self.wrong.hide()
            self.t1 = time.time()
            self.total=self.t1-self.t0
            print("wow")
            self.label.setText("Time: {}".format(self.total))
            self.label_2.setText("Accuracy: {}".format(self.count))
            self.calc_grade()
    def new_game(self):
        self.total=0
        self.count=0
        self.label.setText("Time:")
        self.label_2.setText("Accuracy:")
        self.label_3.setText("Grade:")
        self.textEdit.clear()
        self.random_sentence()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.randomse.setText(_translate("MainWindow", "Random Sentence"))
        self.Head.setText(_translate("MainWindow", "Test your typing - @yuvalzohar"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Time :"))
        self.wrong.setText(_translate("MainWindow", "Wrong !"))
        self.label_2.setText(_translate("MainWindow", "Accuracy :"))
        self.label_3.setText(_translate("MainWindow", "Grade :"))
        self.pushButton.setText(_translate("L", "Submit"))
        self.newgame.setText(_translate("L", "New Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
