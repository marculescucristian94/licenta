import sys
from PyQt4 import QtGui, QtCore

class FingerPiMainWindow(QtGui.QWidget):
    
    def __init__(self):
        super(FingerPiMainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):

        # Labels and buttons
        guide_text = QtGui.QLabel('Welcome to FingerPi!')

        register_button = QtGui.QPushButton("Register", self)
        register_button.setToolTip('Register a new fingerprint')
        register_button.clicked.connect(self.buttonClicked)

        autocomplete_button = QtGui.QPushButton("Autocomplete", self)
        autocomplete_button.setToolTip('Autocomplete a PDF form')
        autocomplete_button.clicked.connect(self.buttonClicked)

        add_fields_button = QtGui.QPushButton("Add fields", self)
        add_fields_button.setToolTip('Add fields to a registered fingerprint')
        add_fields_button.clicked.connect(self.buttonClicked)

        # Layout
        # hbox = QtGui.QHBoxLayout()
        # hbox.setAlignment(QtGui.QAlignCenter)
        # hbox.addWidget(register_button)
        # hbox.addWidget(autocomplete_button)
        # hbox.addWidget(add_fields_button)
        # vbox = QtGui.QVBoxLayout()
        # vbox.setAlignment(QtGui.QAlignCenter)
        # vbox.addWidget(guide_text)
        # vbox.addLayout(hbox)
        # self.setLayout(vbox)

        # Grid Layout works
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(guide_text, 1, 1)
        grid.addWidget(register_button, 2, 0)
        grid.addWidget(autocomplete_button, 2, 1)
        grid.addWidget(add_fields_button, 2, 2)
        self.setLayout(grid) 

        self.resize(100, 100)
        self.center()        
        
        self.setWindowTitle('FingerPi main menu')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def buttonClicked(self):
        sender = self.sender()
        QtGui.QMessageBox.information(self, 'Info', "Not yet implmented.")

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you want to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    gui = FingerPiMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()