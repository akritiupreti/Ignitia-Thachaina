import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QLabel
from PyQt5 import QtWidgets
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
        name = dlg.getOpenFileName(self, 'Open file', 'D:\\Project\\Ignitia-App\\OCR_and_Generator\\Images', "Image files (*.jpg *.png *.jpeg)")
        print(name)
        ind = name[0].rfind("/")
        self.files[index] = name[0][ind+1:]
        print(self.files[0])

        if 0 not in self.files:
            popup = Popup()
            widget.addWidget(popup)
            widget.setCurrentIndex(widget.currentIndex()+1)
            OCR.run(self.files)
            os.mkdir("info")
            inputScreen = Input()
            widget.addWidget(inputScreen)
            widget.setCurrentIndex(widget.currentIndex()+1)


class Input(QDialog):
    def __init__(self):
        super(Input, self).__init__()
        loadUi("inputscreen.ui", self)
        self.uploadbutton.clicked.connect(self.openText)

        self.fname = ""

    def openText(self):
        dlg = QFileDialog()
        name = dlg.getOpenFileName(self, 'Open file', 'D:\\Project\\Ignitia-App\\OCR_and_Generator', "Text files (*.txt)")
        print(name)
        self.fname = name[0]

        main.run(self.fname)
        print("hello")

        popup = Final()
        widget.addWidget(popup)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Final(QDialog):
    def __init__(self):
        super(Final, self).__init__()
        loadUi("final.ui", self)

        while not os.path.exists("image.png"):
            print("hello")
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

        self.continuebutton.clicked.connect(self.proceed)

    def proceed(self):
        while not os.path.exists("OCR_and_Generator/done.txt"):
            time.sleep(3)
            name = ""
            for name in os.listdir("OCR_and_Generator"):
                if "char" in name:
                    break

            pix = QPixmap("OCR_and_Generator/" + name)
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene(self)
            scene.addItem(item)
            self.letterview.setScene(scene)

            self.quelabel.setText("Is this " + name[-1] + "?")
            text = self.inputchar.text()

            f = open("OCR_and_Generator/data.txt", "w")
            if text == " ": # unrecognized
                f.write("!")
            elif text == "": # correct
                f.write("NULL")
            else: # update
                f.write(text)

            f.close()


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

