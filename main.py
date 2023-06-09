import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QLabel
from PyQt5 import QtWidgets, QtGui
from OCR_and_Generator import OCR, main
from PyQt5.QtGui import QPixmap
import time


class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("homescreen.ui", self)
        self.proceedbutton.clicked.connect(self.start)

    def start(self):
        if os.path.exists("info"): # to check if user's handwriting is already stored
            inputScreen = Input()
            widget.addWidget(inputScreen)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            mainScreen = Main()
            widget.addWidget(mainScreen)
            widget.setCurrentIndex(widget.currentIndex()+1)


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("mainscreen.ui", self)
        self.uppercasebutton.clicked.connect(lambda: self.openPhoto(0))
        self.lowercasebutton.clicked.connect(lambda: self.openPhoto(1))
        self.numbersbutton.clicked.connect(lambda: self.openPhoto(2))

        self.files = [0, 0, 0]

    def openPhoto(self, index):
        dlg = QFileDialog()
        name = dlg.getOpenFileName(self, 'Open file', 'D:\\Project\\Ignitia-Thachaina\\OCR_and_Generator\\Images', "Image files (*.jpg *.png *.jpeg)")
        print(name)
        ind = name[0].rfind("/")
        self.files[index] = name[0][ind+1:]
        print(self.files[0])

        if 0 not in self.files:
            OCR.run(self.files)

            popup = Popup()
            widget.addWidget(popup)
            widget.setCurrentIndex(widget.currentIndex()+1)

            '''
            os.mkdir("info")
            inputScreen = Input()
            widget.addWidget(inputScreen)
            widget.setCurrentIndex(widget.currentIndex()+1)
            '''


class Input(QDialog):
    def __init__(self):
        super(Input, self).__init__()
        loadUi("inputscreen.ui", self)
        self.uploadbutton.clicked.connect(self.openText)

        self.fname = ""

    def openText(self):
        dlg = QFileDialog()
        name = dlg.getOpenFileName(self, 'Open file', 'D:\\Project\\Ignitia-Thachaina\\OCR_and_Generator', "Text files (*.txt)")
        print(name)
        self.fname = name[0]

        main.run(self.fname)

        popup = Final()
        widget.addWidget(popup)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Final(QDialog):
    def __init__(self):
        super(Final, self).__init__()
        loadUi("final.ui", self)

        while not os.path.exists("image.png"):
            pass

        pix = QPixmap("image.png")
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        self.letterview.setScene(scene)


class Popup(QDialog):
    def __init__(self):
        super(Popup, self).__init__()
        loadUi("popup.ui", self)
        print("hello")

        self.continuebutton.clicked.connect(self.proceed)

        self.image = os.listdir("OCR_and_Generator/Characters")
        self.maxlen = len(self.image)
        self.index = 0

        pix = QPixmap("OCR_and_Generator/Characters/" + self.image[self.index])
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)

        self.letterview.setScene(scene)

        self.quelabel.setText("Is this " + self.image[self.index][0] + "?")
        self.index += 1

    def proceed(self):
        text = self.inputchar.text()
        if text == " ":  # unrecognized
            #print("OCR_and_Generator/Characters/" + self.image[self.index-1])
            os.remove("OCR_and_Generator/Characters/" + self.image[self.index-1])
        elif text == "":  # correct
            pass
        else:  # update
            #print("OCR_and_Generator/Characters/" + self.image[self.index-1], "OCR_and_Generator/Characters/" + text + ".jpg")
            os.rename("OCR_and_Generator/Characters/" + self.image[self.index-1], "OCR_and_Generator/Characters/" + text + ".jpg")

        #self.quelabel.removeText()

        pix = QPixmap("OCR_and_Generator/Characters/" + self.image[self.index])
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        self.letterview.setScene(scene)

        self.quelabel.setText("Is this " + self.image[self.index][0] + "?")
        self.index += 1

        if self.index >= self.maxlen:
            os.mkdir("info")
            inputScreen = Input()
            widget.addWidget(inputScreen)
            widget.setCurrentIndex(widget.currentIndex() + 1)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    homeScreen = Home()

    widget = QtWidgets.QStackedWidget()
    widget.addWidget(homeScreen)
    widget.setFixedHeight(620)
    widget.setFixedWidth(480)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

