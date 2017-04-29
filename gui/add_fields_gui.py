import sys
from PyQt4 import QtGui, QtCore

class AddMenu(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(AddMenu, self).__init__(parent)
        self.initUI()

    def initUI(self):
    	self.widget = AddMenuWindowWidget(self)
        self.setCentralWidget(self.widget)
        self.center()
        self.setWindowTitle('FingerPi Add Fields')
        self.setWindowIcon(QtGui.QIcon('fingerpi.png'))

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topRight())

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you want to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# TODO: 'Add fields' button
class AddMenuWindowWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(AddMenuWindowWidget, self).__init__(parent)
        # Labels and buttons
        self.id_label = QtGui.QLabel('Fingerprint ID')
        self.id_line_edit = QtGui.QLineEdit(self)
        self.id_line_edit.setToolTip('The id registered on the FingerPi device')
        self.field_name_label = QtGui.QLabel('Field name')
        self.field_name_line_edit = QtGui.QLineEdit(self)
        self.field_name_line_edit.setToolTip('The name of the field found in the PDF form')
        self.field_value_label = QtGui.QLabel('Field value')
        self.field_value_line_edit = QtGui.QLineEdit(self)
        self.field_value_line_edit.setToolTip('The value that will be written in the field')
        self.confirm_button = QtGui.QPushButton('Confirm')
        # Grid Layout works
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.id_label, 1, 0)
        grid.addWidget(self.id_line_edit, 1, 1)
        grid.addWidget(self.field_name_label, 2, 0)
        grid.addWidget(self.field_name_line_edit, 2, 1)
        grid.addWidget(self.field_value_label, 3, 0)
        grid.addWidget(self.field_value_line_edit, 3, 1)
        grid.addWidget(self.confirm_button, 4, 0, 1, 2)
        self.setLayout(grid)