import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, QPushButton, 
    QListWidget, QHBoxLayout, QVBoxLayout
)

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

app.exec()

