# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from new_backend import *
import json
import requests


class Ui_ids(object):
    def setupUi(self, ids):
        ids.setObjectName("ids")
        ids.resize(1226, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo_dino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ids.setWindowIcon(icon)
        ids.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.tabWidget = QtWidgets.QTabWidget(ids)
        self.tabWidget.setGeometry(QtCore.QRect(210, 130, 771, 341))
        self.tabWidget.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 731, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 71, 731, 211))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 70, 731, 211))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 70, 731, 211))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(ids)
        self.label.setGeometry(QtCore.QRect(450, 40, 301, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(117, 87, 153);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(ids)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 470, 161, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(ids)
        self.pushButton.setGeometry(QtCore.QRect(820, 470, 161, 61))
        self.pushButton.setStyleSheet("background-color: rgb(117, 87, 153);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ids)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(ids)

    def retranslateUi(self, ids):
        _translate = QtCore.QCoreApplication.translate
        ids.setWindowTitle(_translate("ids", "SoftSecurity"))
        self.label_2.setText(_translate("ids", "Vérification de site pornographique:"))
        self.textBrowser.setHtml(_translate("ids", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Le programme va chercher à se connecter à plusieurs sites pornographiques. L\'IDS à pour rôle de bloquer les requêtes qui sont destiner à ces sites afin d\'empêcher toute tentative de connexion.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ids", "Test N°1"))
        self.label_4.setText(_translate("ids", "Vérification de site banquaires"))
        self.textBrowser_3.setHtml(_translate("ids", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ce test consiste à executer des requêtes sur des sites banquaires. Tout comme le test précedent, l\'IDS a pour rôle de bloquer ces requêtes afin d\'empêcher toute tentative de connexion sur ce genre de site.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ids", "Test N°2"))
        self.label_3.setText(_translate("ids", "Vérification anti malware"))
        self.textBrowser_2.setHtml(_translate("ids", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dans cette partie du test, le programme va effectuer des tentives de téléchargement de malwares sur différents sites (ces sites ont été conçu à cet éffigie). L\'IDS aura pour role d\'empêcher le téléchargement des fichiers. </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("ids", "Test N°3"))
        self.label_5.setText(_translate("ids", "Vérification sur IP Tor"))
        self.textBrowser_4.setHtml(_translate("ids", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Même principe que lors des vérifications des sites webs, le programme va effectuer des tentives de connexion sur une multitude d\'IP Tor. Encore une fois, l\'IDS devra bloquer ces tentatives.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("ids", "Test N°4"))
        self.label.setText(_translate("ids", "SoftSecurity"))
        self.pushButton_2.setText(_translate("ids", "Quitter"))
        self.pushButton.setText(_translate("ids", "Lancer le test"))
        self.pushButton.clicked.connect(create_report)
        self.pushButton_2.clicked.connect(quit)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ids = QtWidgets.QWidget()
    ui = Ui_ids()
    ui.setupUi(ids)
    ids.show()
    sys.exit(app.exec_())
