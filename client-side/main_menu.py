import sys
from PyQt4 import QtGui, QtCore
from add_fields_gui import AddMenu
from register_gui import RegisterMenu
from autocomplete_gui import AutocompleteMenu

class RASPrintMainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(RASPrintMainWindow, self).__init__(parent)
        self.initUI()
        self.initSecondaryMenus()
        self.show()
        
    def initSecondaryMenus(self):
        self.register_menu = RegisterMenu(self)
        self.autocomplete_menu = AutocompleteMenu(self)
        self.add_menu = AddMenu(self) 

    def initUI(self):
        self.widget = MainWindowWidget(self)
        self.setCentralWidget(self.widget)
        self.setButtonListeners()
        self.center()       
        self.setWindowTitle('RASPrint Main Menu')
        self.setWindowIcon(QtGui.QIcon('RASPrint.png'))

    def setButtonListeners(self):
        self.widget.register_button.clicked.connect(self.buttonClicked)
        self.widget.autocomplete_button.clicked.connect(self.buttonClicked)
        self.widget.add_fields_button.clicked.connect(self.buttonClicked)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def buttonClicked(self):
        sender = self.sender()
        if   sender == self.widget.register_button:
            self.hide()
            self.register_menu.show()
        elif sender == self.widget.autocomplete_button:
            self.hide()
            self.autocomplete_menu.show()
        elif sender == self.widget.add_fields_button:
            self.hide()
            self.add_menu.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Confirm Exit',
            "Are you want to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class MainWindowWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(MainWindowWidget, self).__init__(parent)
        # Labels and buttons
        self.guide_label = QtGui.QLabel('Welcome to RASPrint!')
        self.register_button = QtGui.QPushButton("Register", self)
        self.register_button.setToolTip('Register a new fingerprint')
        self.autocomplete_button = QtGui.QPushButton("Autocomplete", self)
        self.autocomplete_button.setToolTip('Autocomplete a PDF form')
        self.add_fields_button = QtGui.QPushButton("Add/Update Fields", self)
        self.add_fields_button.setToolTip('Add fields to a registered fingerprint or update existing ones')
        # Grid Layout works
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.guide_label, 1, 1)
        grid.addWidget(self.register_button, 2, 0)
        grid.addWidget(self.autocomplete_button, 2, 1)
        grid.addWidget(self.add_fields_button, 2, 2)
        self.setLayout(grid)

        
def main():
    app = QtGui.QApplication(sys.argv)
    gui = RASPrintMainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
