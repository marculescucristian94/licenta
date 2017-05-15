import sys
from PyQt4 import QtGui, QtCore

class RegisterMenu(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(RegisterMenu, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.widget = RegisterWindowWidget(self)
        # TODO: Button listeners
        self.setCentralWidget(self.widget)  
        self.center()
        self.setWindowTitle('FingerPi Register')
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

class RegisterWindowWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(RegisterWindowWidget, self).__init__(parent)
        # Labels and buttons
        self.name_label = QtGui.QLabel('Name')
        self.name_line_edit = QtGui.QLineEdit(self)
        self.surname_label = QtGui.QLabel('Surname')
        self.surname_line_edit = QtGui.QLineEdit(self)
        # TODO: QCalendarWidget
        self.birthdate_label = QtGui.QLabel('Date of birth')
        self.birthdate_line_edit = QtGui.QLineEdit(self)
        self.birthdate_line_edit.setToolTip('Format is: DD/MM/YYYY')
        self.pid_label = QtGui.QLabel('Personal Number')
        self.pid_line_edit = QtGui.QLineEdit(self)
        self.id_series_label = QtGui.QLabel('ID Series')
        self.id_series_line_edit = QtGui.QLineEdit(self)
        self.id_number_label = QtGui.QLabel('ID Number')
        self.id_number_line_edit = QtGui.QLineEdit(self)
        self.address_label = QtGui.QLabel('Address')
        self.address_line_edit = QtGui.QLineEdit(self)
        self.register_button = QtGui.QPushButton('Register')
        # Grid Layout works
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.name_label, 1, 0)
        grid.addWidget(self.name_line_edit, 1, 1)
        grid.addWidget(self.surname_label, 1, 2)
        grid.addWidget(self.surname_line_edit, 1, 3)
        grid.addWidget(self.birthdate_label, 2, 0)
        grid.addWidget(self.birthdate_line_edit, 2, 1)
        grid.addWidget(self.pid_label, 2, 2)
        grid.addWidget(self.pid_line_edit, 2, 3)
        grid.addWidget(self.id_series_label, 3, 0)
        grid.addWidget(self.id_series_line_edit, 3, 1)
        grid.addWidget(self.id_number_label, 3, 2)
        grid.addWidget(self.id_number_line_edit, 3, 3)
        grid.addWidget(self.address_label, 4, 0)
        grid.addWidget(self.address_line_edit, 4, 1, 1, 4)
        grid.addWidget(self.register_button, 5, 1)
        self.setLayout(grid)

        
        