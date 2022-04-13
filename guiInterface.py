

from tkinter import *

from PyQt5.QtWidgets import QApplication

from DatabaseTime import DatabaseTime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.timeEntity = DatabaseTime()

        self.setObjectName("Dialog")
        self.resize(640, 480)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 100, 150, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(140, 160, 100, 14))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 130, 120, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(280, 100, 150, 20))
        self.textEdit.setObjectName("textEdit")


        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "введите время"))
        self.pushButton.setText(_translate("self", "Зазеркалье!"))

        self.pushButton.clicked.connect(self.clicked)


    def clicked(self):
        try:
            realTime = self.timeEntity.convertTimeAndAddToDB(self.textEdit.toPlainText())
            self.label_2.setText(realTime)
        except ValueError:
            self.textEdit.configure(state="disable")
            self.pushButton.configure(state="disable")
            raise ValueError

# app = QApplication(sys.argv)
# ex = Ui_Dialog()
# ex.show()
# sys.exit(app.exec_())