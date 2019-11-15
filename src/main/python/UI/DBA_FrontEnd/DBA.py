# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dissectorbuilderarea.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from StartField import StartField

from UI.DBA_FrontEnd.Field import Field
from UI.DBA_FrontEnd.While_Loop import While_Loop
from UI.DBA_FrontEnd.Decision import Decision
from UI.DBA_FrontEnd.GraphicsProxyWidget import GraphicsProxyWidget
from UI.DBA_FrontEnd.DropGraphicsScene import DropGraphicsScene
from UI.DBA_FrontEnd.DragButton import DragButton
import json

class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox,self).showPopup()

class QGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(QGraphicsView, self).__init__(parent)
        
    #This helps zoom in and out the canvas 
    #RESOURCE: https://stackoverflow.com/questions/19113532/qgraphicsview-zooming-in-and-out-under-mouse-position-using-mouse-wheel
    def wheelEvent(self, event):
        
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        oldPos = self.mapToScene(event.pos())

        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

        newPos = self.mapToScene(event.pos())

        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 550)
        Form.setMinimumSize(QtCore.QSize(900, 550))
        self.dba_label = QtWidgets.QLabel(Form)
        self.dba_label.setGeometry(QtCore.QRect(120, 10, 151, 16))
        self.dba_label.setObjectName("dba_label")
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(35, 31, 600, 500))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = DropGraphicsScene(QtCore.QRectF(0,0,self.graphicsView.width(), self.graphicsView.height()))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setSceneRect(QtCore.QRectF(0, 0, 6000, 6000))
        self.toolbox_label = QtWidgets.QLabel(Form)
        self.toolbox_label.setGeometry(QtCore.QRect(650, 10, 64, 17))
        self.toolbox_label.setObjectName("toolbox_label")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(650, 30, 201, 320))
        self.toolBox.setObjectName("toolBox")
        self.field_tab = QtWidgets.QWidget()
        self.field_tab.setGeometry(QtCore.QRect(0, 0, 201, 110))
        self.field_tab.setObjectName("field_tab")
        

        self.field_button = DragButton('Field', self.field_tab)
        self.field_button.setGeometry(QtCore.QRect(20, 5, 100, 30))
        self.field_button.setObjectName("field_button")

        self.str_field_button = DragButton('Field (String)', self.field_tab)
        self.str_field_button.setGeometry(QtCore.QRect(20, 40, 100, 30))
        self.str_field_button.setObjectName("str_field_button")

        self.int_field_button = DragButton('Field (Integer)', self.field_tab)
        self.int_field_button.setGeometry(QtCore.QRect(20, 75, 100, 30))
        self.int_field_button.setObjectName("int_field_button")

        self.float_field_button = DragButton('Field (Float)', self.field_tab)
        self.float_field_button.setGeometry(QtCore.QRect(20, 110, 100, 30))
        self.float_field_button.setObjectName("float_field_button")

        self.octal_field_button = DragButton('Field (Octal)', self.field_tab)
        self.octal_field_button.setGeometry(QtCore.QRect(20, 145, 100, 30))
        self.octal_field_button.setObjectName("octal_field_button")

        #Code Block
        self.code_block_button = DragButton('Code Block', self.field_tab)
        self.code_block_button.setGeometry(QtCore.QRect(20, 180, 100, 30))
        self.code_block_button.setObjectName("code_block_button")

        self.list_fields_box = ComboBox(self.field_tab)
        self.list_fields_box.setGeometry(QtCore.QRect(20, 215, 171,30))
        self.list_fields_box.setObjectName("list_field_label")
        self.list_fields_box.addItem('Added Fields')
        self.list_fields_box.popupAboutToBeShown.connect(self.populateConbo)


        self.toolBox.addItem(self.field_tab, "")
        self.construct_tab = QtWidgets.QWidget()
        self.construct_tab.setGeometry(QtCore.QRect(0, 0, 201, 189))
        self.construct_tab.setObjectName("construct_tab")
        self.decision_button = DragButton("Decision", self.construct_tab)
        self.decision_button.setGeometry(QtCore.QRect(0, 0, 83, 25))
        self.decision_button.setObjectName("decision_button")
        

        self.while_loop_button =DragButton("while", self.construct_tab)
        self.while_loop_button.setGeometry(QtCore.QRect(0, 30, 83, 25))
        self.while_loop_button.setObjectName("while_loop_button")

        self.for_loop_button =DragButton("for", self.construct_tab)
        self.for_loop_button.setGeometry(QtCore.QRect(0, 60, 83, 25))
        self.for_loop_button.setObjectName("for_loop_button")

        self.do_loop_button =DragButton("do while", self.construct_tab)
        self.do_loop_button.setGeometry(QtCore.QRect(0, 90, 83, 25))
        self.do_loop_button.setObjectName("do_loop_button")

        self.end_loop_button = DragButton("End Loop", self.construct_tab)
        self.end_loop_button.setGeometry(QtCore.QRect(90, 0, 83, 25))
        self.end_loop_button.setObjectName("end_loop_button")

        self.do_button = DragButton("do", self.construct_tab)
        self.do_button.setGeometry(QtCore.QRect(90, 30, 83, 25))
        self.do_button.setObjectName("do_button")

        self.connector_button = QtWidgets.QPushButton('Connector', self.construct_tab)
        self.connector_button.setGeometry(QtCore.QRect(0,120,83,25))
        self.connector_button.setObjectName("connector_button")
        self.connector_button.clicked.connect(self.connector_button_clicked)

        self.save_button = QtWidgets.QPushButton('Save', self.construct_tab)
        self.save_button.setGeometry(QtCore.QRect(0,150,83,25))
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.save_button_clicked)

        self.toolBox.addItem(self.construct_tab, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dba_label.setText(_translate("Form", "Dissector Builder Area"))
        self.toolbox_label.setText(_translate("Form", "Toolbox"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.field_tab), _translate("Form", "Field"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.construct_tab), _translate("Form", "Construct"))

    def populateConbo(self):
        self.list_fields_box.clear()
        self.list_fields_box.addItem('Added Fields')
        self.fields = self.scene.proxyFieldWidgetList
        for field in self.fields:
            self.list_fields_box.addItem(field.widget().menu().actions()[0].defaultWidget().table.cellWidget(0,1).text())
        
    def open_field_window(self):
        self.field_win = Field()
        self.field_win.show()

    def open_loop_window(self):
        self.loop_win = Loop()
        self.loop_win.show()

    def open_decision_window(self):
        self.decision_win = Decision()
        self.decision_win.show()

    def connector_button_clicked(self):
        self.scene.setMode(self.scene.InsertLine_ON)

    def save_button_clicked(self):
        dissector_dictionary = self.scene.save_dissector()
        dissector_json = json.dumps(dissector_dictionary)
        print(dissector_json)
        #return dissector_json

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
