from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sys


class Question_Window(QtWidgets.QWidget):
    def __init__(self):
        super(Question_Window, self).__init__()
        uic.loadUi('uic/question_window.ui', self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        px = QtGui.QPixmap('images/fon1.jpg')
        px.scaled(100, 100)
        self.fon_lb.setPixmap(px)
