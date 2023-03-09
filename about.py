# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutvpqSzJ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, 
    QMetaObject, QRect,
    QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QApplication, QLabel,
    QTextBrowser, QWidget)
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(690, 357)
        icon = QIcon()
        icon.addFile(u"./logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 310, 111, 16))
        self.label.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 310, 221, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 10, 185, 34))
        self.label_3.setStyleSheet(u"font: 20pt \"Geometr212 BkCn BT\";")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 50, 671, 241))
        self.textBrowser.setStyleSheet(u"font: 600 16pt \"Yu Gothic UI\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"About", None))
        self.label.setText(QCoreApplication.translate("Form", u"Source code -", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a href=\"https://github.com/rajsingh010\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/rajsingh010</span></a></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"About EnPass", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:400;\">EnPass is a very simple and useful tool which generates a set of encrypted passwords and the encryption methods are same ones which are used to make block chains so you should understand it's pretty much safe.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0"
                        "; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:400;\">EnPass is made using Python as the main programming language and PySide6 framework to design the ui while using some standard libraries of python to perform the encryption you can also view the source code from the link given below.(It's fairly simple and easy to use.)</span></p></body></html>", None))

    # retranslateUi
def _run():
    app = QApplication(sys.argv)
    MainWin = QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec())
    #ap._run() 
if __name__ == '__main__':
    _run()

