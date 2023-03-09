# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject, QRect, QTranslator,
                            QSize, Qt)
from PySide6.QtGui import (QIcon, QShortcut, QKeySequence, QAction)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QTextBrowser, QWidget)
from hashlib import sha256, sha384, sha512, sha224
import sys
import pyperclip

from tkinter import filedialog
from tkinter import Tk, Label, Button, GROOVE
from PIL import ImageTk, Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 350)
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 50, 671, 21))
        self.lineEdit.setStyleSheet(u"border-width:1px;\n"
                                    "border-style:solid;\n"
                                    "border-radius:5px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 80, 91, 24))
        self.pushButton.setStyleSheet(u"")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(120, 120, 591, 21))
        self.textBrowser.setStyleSheet(u"border-width:1px;\n"
                                       "border-style:solid;\n"
                                       "border-radius:5px;")
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(120, 180, 591, 21))
        self.textBrowser_2.setStyleSheet(u"border-width:1px;\n"
                                         "border-style:solid;\n"
                                         "border-radius:5px;")
        self.textBrowser_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_3 = QTextBrowser(self.centralwidget)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(120, 230, 591, 21))
        self.textBrowser_3.setStyleSheet(u"border-width:1px;\n"
                                         "border-style:solid;\n"
                                         "border-radius:5px;")
        self.textBrowser_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 130, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 71, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 230, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 10, 471, 31))
        self.label_4.setStyleSheet(u"font: 700 14pt \"Segoe Print\";")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(720, 120, 75, 24))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(720, 180, 75, 24))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(720, 230, 75, 24))
        self.textBrowser_4 = QTextBrowser(self.centralwidget)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(120, 280, 591, 21))
        self.textBrowser_4.setStyleSheet(u"border-width:1px;\n"
                                         "border-style:solid;\n"
                                         "border-radius:5px;")
        self.textBrowser_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(720, 280, 75, 24))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 280, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"GENERATE", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Password 1 : ", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Password 2 : ", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Password 3 : ", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the text below to generate the passwords", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Copy!", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", u"Copy!", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", u"Copy!", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", u"Copy!", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Password 4 : ", None))
        self.menuExport.setTitle(
            QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuHelp.setTitle(
            QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton.clicked.connect(self.config_browsers)
        self.pushButton_2.clicked.connect(self.copy1)
        self.pushButton_3.clicked.connect(self.copy2)
        self.pushButton_4.clicked.connect(self.copy3)
        self.pushButton_5.clicked.connect(self.copy4)
        self.menuHelp.addAction('About', self.about)
        self.menuExport.addAction('Export', self.export)
        self.pushButton.addAction('Generate', self.config_browsers)
        tr = QCoreApplication.translate

    # retranslateUi

    def export(self):
        win = Tk()
        try:
            if self.textBrowser.toPlainText() == '':
                img = ImageTk.PhotoImage(Image.open('majikayo.jpg'))
                lb = Label(win, image=img)
                lb.pack()
                lb2 = Label(win, text="(Means 'Seriously??)\nBtw you forget to put some text inside the input box\nOR didn't hit the generate button.\n")
                lb2.pack()
                btn = Button(win, text="Oh! Stupid me..", command=win.destroy, relief=GROOVE)
                btn.pack()
                win.mainloop()
            else:
                win.withdraw()
                filename = filedialog.asksaveasfilename(
                    initialfile='Enpass_Export.txt', initialdir='/', title='Save File', filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
                start = 'ENPASS EXPORTED CODES'.center(50, '-')
                end = '-'*len(start) + '\n' + 'You can go to https://github.com/rajsingh010/EnPass to download the software again'
                textContent = f'{start}\nPass1 = {self.textBrowser.toPlainText()}\nPass2 = {self.textBrowser.toPlainText()}\nPass3 = {self.textBrowser_2.toPlainText()}\nPass4 = {self.textBrowser_3.toPlainText()}\n{end}'
                myfile = open(filename, "w")
                myfile.write(textContent)
                print("File saved as ", filename)

        except FileNotFoundError as e:
            pass
        win.destroy()
        # to test

    def about(self):
        from about import Ui_Form
        self.newWin = QWidget()
        ui = Ui_Form()
        ui.setupUi(self.newWin)
        self.newWin.show()

    def _encode(self, text_):
        text_ = text_.encode('utf-8')
        x1 = sha256(text_)
        x2 = sha384(text_)
        x3 = sha512(text_)
        x4 = sha224(text_)
        x1 = x1.hexdigest()
        x2 = x2.hexdigest()
        x3 = x3.hexdigest()
        x4 = x4.hexdigest()
        return [x1, x2, x3, x4]

    def config_browsers(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        passes = self._encode(self.lineEdit.text())
        self.textBrowser.insertPlainText(passes[0])
        self.textBrowser_2.insertPlainText(passes[1])
        self.textBrowser_3.insertPlainText(passes[2])
        self.textBrowser_4.insertPlainText(passes[3])

    def copy1(self):
        pyperclip.copy(self.textBrowser.toPlainText())

    def copy2(self):
        pyperclip.copy(self.textBrowser_2.toPlainText())

    def copy3(self):
        pyperclip.copy(self.textBrowser_3.toPlainText())

    def copy4(self):
        pyperclip.copy(self.textBrowser_4.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec())
    # ap._run()
