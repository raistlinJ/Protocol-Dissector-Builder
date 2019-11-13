import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint
from UI.DBA_FrontEnd.DBA_BackEnd import While


class While_Loop(QWidget):
    def __init__(self, name):

        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):

        self.setWindowTitle("while Loop")
        self.layout = QGridLayout()
        self.col = 0
        
        self.while_label = QLabel()
        self.while_label.setText(" while")
        self.layout.addWidget(self.while_label, 0, 0)

        self.layout.addWidget(QLineEdit(), 1, self.col)
        self.col+=1
        logical_ops_box= QComboBox()
        logical_ops = ["",">", "<", "=>", "<=", "==", "!=", "AND", "OR"]

        for op in logical_ops:
            logical_ops_box.addItem(op)
        # self.layout.addWidget(logical_ops_box,1, self.col)
        # self.col+=1

        # self.layout.addWidget(QLineEdit(), 1, self.col)
        # self.col+=1

        self.addButton = QPushButton("+")
        self.layout.addWidget(self.addButton,2,0)
        self.addButton.clicked.connect(self.clickMethod)

        self.setLayout(self.layout)
        self.show()

    def getName(self):
        return self.name

    def clickMethod(self):
        logical_ops_box = QComboBox()
        logical_ops = ["",">", "<", "=>", "<=", "==", "!=", "AND", "OR"]

        for op in logical_ops:
            logical_ops_box.addItem(op)
        self.layout.addWidget(logical_ops_box,1, self.col)
        self.col+=1
        self.layout.setColumnMinimumWidth(self.col, 85)
        self.layout.addWidget(QLineEdit(), 1, self.col)
        self.col+=1
        self.layout.removeWidget(self.while_label)
        self.layout.addWidget(self.while_label, 0, self.col//2)

        self.parent().resize(self.layout.sizeHint())

    def saveMethod(self):
        while_properties = {}
        colCount = self.layout.columnCount()
        operandNum = 1
        if(colCount > 1):
            operatorNum = 1
        for i in range(colCount):
            loopWidget = self.layout.itemAtPosition(1, i).widget()
            if(isinstance(loopWidget, QLineEdit)):
                operandName = "operand" + str(operandNum)
                operandNum = operandNum + 1
                while_properties.update({operandName: loopWidget.text()})
            if(isinstance(loopWidget, QComboBox)):
                operatorName = "operator" + str(operatorNum)
                operatorNum = operatorNum + 1
                while_properties.update({operatorName: loopWidget.currentText()})
        return while_properties
        
if __name__ == '__main__':
    app = QApplication([])
    test = While_Loop()
    sys.exit(app.exec_())