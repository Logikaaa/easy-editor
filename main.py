import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, QPushButton, 
    QListWidget, QHBoxLayout, QVBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image

app = QApplication([])
win = QWidget()
win.resize(700,500)

btn_dir = QPushButton('Папка')
filess = QListWidget()
img = QLabel('Картинка')
btn_left = QPushButton('Ліворуч')
btn_right = QPushButton('Праворуч')
btn_mir = QPushButton('Дзеркало')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('Ч/Б')

row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(filess)

col2.addWidget(img)
row_btn = QHBoxLayout()
row_btn.addWidget(btn_left)
row_btn.addWidget(btn_right)
row_btn.addWidget(btn_mir)
row_btn.addWidget(btn_sharp)
row_btn.addWidget(btn_bw)

col2.addLayout(row_btn)
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extension):
    result = []
    for filename in files:
        for ext in extension:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    extension = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extension)
    filess.clear()
    for filename in filenames:
        filess.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        img_path = os.path.join(dir, filename)
        self.image = Image.open(img_path)
    
    def showImage(self, path):
        img.hide()
        pixmapimage = QPixmap(path)
        w, h = img.width(), img.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        img.setPixmap(pixmapimage)
        img.show()
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        img_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(img_path)
    
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        img_path = os.path.join(path, self.filename)
        self.image.save(img_path)

workimage = ImageProcessor()

def showChosenImage():
    if filess.currentRow()>= 0:
        filename = filess.currentItem().text()
        workimage.loadImage(workdir, filename)
        img_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(img_path)

filess.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)

app.exec()

