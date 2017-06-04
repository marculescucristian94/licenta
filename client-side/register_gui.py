import sys
import client
from PyQt4 import QtGui, QtCore

class RegisterMenu(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(RegisterMenu, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.widget = RegisterWindowWidget(self)
        self.setCentralWidget(self.widget)
        self.widget.register_button.clicked.connect(self.convertInput)
        self.center()
        self.setWindowTitle('FingerPi Register')
        self.setWindowIcon(QtGui.QIcon('fingerpi.png'))

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topRight())

    def convertInput(self):
        data_string =  'name:%s|' % (self.widget.name_line_edit.text())
        data_string += 'surname:%s|' % (self.widget.surname_line_edit.text())
        data_string += 'birthdate:%s|' % (self.widget.birthdate_line_edit.text())
        data_string += 'pid:%s|' % (self.widget.pid_line_edit.text())
        data_string += 'id_series:%s|' % (self.widget.id_series_line_edit.text())
        data_string += 'id_number:%s|' % (self.widget.id_number_line_edit.text())
        data_string += 'address:%s' % (self.widget.address_line_edit.text())
        id = client.send_command('register', data_string)
	if not id == '' and 0 <= int(id) <= 199:
		message = 'Registration complete! Your id is %s, please remember it!' % (id)
		QtGui.QMessageBox.information(self, 'Operation success', message)
	else: 
		message = 'Something went wrong during the registration process. Please try again.'
		QtGui.QMessageBox.information(self, 'Operation failed', message)

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

        
        
