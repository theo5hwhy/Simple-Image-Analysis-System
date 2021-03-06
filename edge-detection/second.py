# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from third import Ui_thirdPageWindow
from detection import *
from PIL import Image




images=[]

class Ui_SecondWindow(object):

    def openDialogBox(self):
        '''
        open a dialogBox to choose the image
        '''
        filename = QFileDialog.getOpenFileName()
        imagePath = filename[0]
        self.textBrowser.setText(imagePath)
        pixmap =QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.img_path = imagePath
        images.append(self.img_path)


    # def done(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_thirdPageWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()


    def done(self):
        self.analysis_of_img()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_thirdPageWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def analysis_of_img(self):
        '''
        Apply edge detection on the image
        first read the image path , create an image object , detect edges 
        '''
        img_path = self.img_path
        img_object =  MyImage(img_path)
        original , gray_level , gray_path = img_object.return_tupled_image()
        if self.radioButton.isChecked():
            detected_img,detected_path = img_object.apply_detector(roberts)
        else:
            detected_img,detected_path = img_object.apply_detector(sobel)


        self.detected_img = detected_img #numpy.ndarray
        self.original  = original
        self.gray_level = gray_level #PIL.Image.Image
        noise_free_path = img_object.noise_removal()
        ## append the tow images now
        images.append(gray_path)
        images.append(detected_path)
        images.append(noise_free_path)
        

        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(41, 40, 38);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        ## white area where we show the path of the image
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 40, 256, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        
        ## creation of PushButton (Browse)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 30, 121, 51))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(25, 148, 200);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openDialogBox)

        ### Radio buttons creation
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(310, 320, 181, 31))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        #Radio Butoon properities
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(25, 148, 200);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(310, 370, 171, 31))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(25, 148, 200);")
        self.radioButton_2.setObjectName("radioButton_2")

        ## creation of BushButton 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 430, 191, 51))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        #Properities of PushButton2
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(25, 148, 200);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.done)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 301, 181))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.radioButton.setText(_translate("MainWindow", "Robert Detector"))
        self.radioButton_2.setText(_translate("MainWindow", "Sobel Detector"))
        self.pushButton_2.setText(_translate("MainWindow", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
