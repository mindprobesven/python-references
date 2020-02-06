#!/usr/bin/env python3

import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QTimer

def update_label():
    textLabel.setText("Sven")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.setText("Hello Sven!")
    textLabel.move(110, 85)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()

    timer = QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)

    sys.exit(app.exec_())
