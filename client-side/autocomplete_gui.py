import sys
import client
from PyQt4 import QtGui, QtCore
from autocomplete_tools import pdf_filler 

MAX_LINEEDIT_WIDTH = 500

class AutocompleteMenu(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(AutocompleteMenu, self).__init__(parent)
        self.initUI()

    def initUI(self):
    	self.widget = AutocompleteWindowWidget(self)
    	self.widget.browse_button.clicked.connect(self.browseFiles)
    	self.setCentralWidget(self.widget)
    	self.widget.autocomplete_button.clicked.connect(self.autocompleteForm)  
    	self.center()
        self.setWindowTitle('FingerPi Autocomplete')
        self.setWindowIcon(QtGui.QIcon('fingerpi.png'))

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topRight())

    def autocompleteForm(self):
    	data_string = self.widget.id_line_edit.text()
	filepath = self.widget.filepath_line_edit.text()
    	response = client.send_command('autocomplete', str(data_string))
	if not response == 'mismatch':
		print response
		print filepath
		pdf_filler.autocomplete_pdf(response, filepath)
		QtGui.QMessageBox.information(self, 'Autocomplete successful', "Autocomplete operation successful.")
	else:
		QtGui.QMessageBox.information(self, 'Autocomplete failed', "Scanned fingerprint did not match with the given id. Please try again.")

    def browseFiles(self):
    	filepath = QtGui.QFileDialog.getOpenFileName(self, 'Select file', '/home')
    	self.widget.filepath_line_edit.setText(filepath)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Confirm exit',
            "Are you want to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class AutocompleteWindowWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(AutocompleteWindowWidget, self).__init__(parent)
        # Labels and buttons
        self.id_label = QtGui.QLabel('Fingerprint ID')
        self.id_line_edit = QtGui.QLineEdit(self)
        self.id_line_edit.setToolTip('The id registered on the FingerPi device')
        self.filepath_label = QtGui.QLabel('Path to file')
        self.filepath_line_edit = QtGui.QLineEdit(self)
        self.filepath_line_edit.setFixedWidth(MAX_LINEEDIT_WIDTH)
        self.filepath_line_edit.setToolTip('Path to the PDF form that must be completed')
        self.browse_button = QtGui.QPushButton('Browse...')
        self.autocomplete_button = QtGui.QPushButton('Start Autocomplete')
        # Grid Layout works
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.id_label, 1, 0)
        grid.addWidget(self.id_line_edit, 1, 1)
        grid.addWidget(self.filepath_label, 2, 0)
        grid.addWidget(self.filepath_line_edit, 2, 1)
        grid.addWidget(self.browse_button, 2, 2)
        grid.addWidget(self.autocomplete_button, 3, 1)
        self.setLayout(grid)
