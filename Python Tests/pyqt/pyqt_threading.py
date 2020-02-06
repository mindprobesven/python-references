#!/usr/bin/env python3

import sys
import time
from threading import Thread

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def start_gui():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()
    win.setLayout(grid)
    win.setWindowTitle("PyQt Grid Example")
    win.setGeometry(50, 50, 200, 200)
    win.show()

    build_grid(grid)

    t = Thread(target=loop, daemon=True)
    t.start()

    sys.exit(app.exec_())

def build_grid(grid):
    for i in range(0, 5):
        for j in range(0, 5):
            grid.addWidget(QPushButton(str(i)+str(j)), i, j)

def loop():
    counter = 0
    while True:
        print(counter)
        counter += 1
        time.sleep(1.0)

if __name__ == "__main__":
    try:
        start_gui()
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
