# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homee.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homefile(object):
    def setupUi(self, homefile):
        homefile.setObjectName("homefile")
        homefile.resize(820, 621)
        homefile.setAcceptDrops(True)
        homefile.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(homefile)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-9, -9, 831, 141))
        self.label_2.setStyleSheet("background-color: rgb(255, 0, 255);\n"
"color: rgb(0, 255, 255);\n"
"font: 20pt \"MV Boli\";")
        self.label_2.setLineWidth(13)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 340, 181, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_check = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name_check.setStyleSheet("background-color: rgb(255, 0, 255);\n"
"font: 12pt \"MV Boli\";")
        self.name_check.setObjectName("name_check")
        self.verticalLayout.addWidget(self.name_check)
        self.password_check = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password_check.setStyleSheet("background-color: rgb(255, 0, 255);\n"
"font: 12pt \"MV Boli\";")
        self.password_check.setObjectName("password_check")
        self.verticalLayout.addWidget(self.password_check)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 440, 318, 87))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.enter_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_btn.sizePolicy().hasHeightForWidth())
        self.enter_btn.setSizePolicy(sizePolicy)
        self.enter_btn.setStyleSheet("QPushButton {\n"
"color: rgb(0, 255, 255);\n"
"background-color: rgb(200, 0, 235);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(200, 0, 245);\n"
"border-radius: 7px;\n"
"width: 100 px;\n"
"height: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 129, 245);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(200, 0, 245, 65);\n"
"}")
        self.enter_btn.setObjectName("enter_btn")
        self.horizontalLayout.addWidget(self.enter_btn)
        self.signup_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.signup_btn.setEnabled(True)
        self.signup_btn.setStyleSheet("QPushButton {\n"
"color: rgb(0, 255, 255);\n"
"background-color: rgb(200, 0, 235);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgb(200, 0, 245);\n"
"border-radius: 7px;\n"
"width: 100 px;\n"
"height: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 129, 245);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(200, 0, 245, 65);\n"
"}")
        self.signup_btn.setObjectName("signup_btn")
        self.horizontalLayout.addWidget(self.signup_btn)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(60, 176, 671, 131))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(450, 320, 281, 221))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("assets/p_home.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        homefile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homefile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName("menubar")
        homefile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homefile)
        self.statusbar.setObjectName("statusbar")
        homefile.setStatusBar(self.statusbar)

        self.retranslateUi(homefile)
        QtCore.QMetaObject.connectSlotsByName(homefile)

    def retranslateUi(self, homefile):
        _translate = QtCore.QCoreApplication.translate
        homefile.setWindowTitle(_translate("homefile", "HOMEPAGE"))
        self.label_2.setText(_translate("homefile", "Анализатор транзакций"))
        self.name_check.setPlaceholderText(_translate("homefile", "Имя:"))
        self.password_check.setPlaceholderText(_translate("homefile", "Пароль:"))
        self.enter_btn.setText(_translate("homefile", "Войти"))
        self.signup_btn.setText(_translate("homefile", "Регистрация"))
        self.textEdit.setHtml(_translate("homefile", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:400;\">Этот анализатор используется для контроля осуществляемых доходов и расходов. Он подсчитывает общую сумму затраченных и полученных денег, определяет сферы транзакций. В данном анализаторе можно вввести на что были затрачены деньги(или получены), кратко описать и указать дату совершенной транзакции. Также можно удалить определенную транзакцию, предварительно выбрав её.</span></p></body></html>"))
