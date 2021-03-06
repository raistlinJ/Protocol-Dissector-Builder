#!/usr/bin/python

"""
The MIT License (MIT)

Copyright (c) 2016 Luca Weiss

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

from UI.PacketPreview.waitingspinnerwidget import QtWaitingSpinner


class Demo(QWidget):


    spinner = None

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        groupbox1 = QGroupBox()
        groupbox1_layout = QHBoxLayout()
        self.setLayout(grid)
        self.setWindowTitle("LOADING")
        self.setMinimumSize(200,200)
        self.setWindowFlags(Qt.Dialog)

        # SPINNER
        self.spinner = QtWaitingSpinner(self)
        self.spinner.setLineWidth(15)
        self.spinner.setLineLength(30)
        self.spinner.setColor(QColor(0,0,139))


        # Layout adds
        groupbox1_layout.addWidget(self.spinner)
        groupbox1.setLayout(groupbox1_layout)


        grid.addWidget(groupbox1, *(1, 1))
        self.spinner.start()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Demo()
    sys.exit(app.exec())
