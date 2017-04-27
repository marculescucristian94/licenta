import sys
from PyQt4 import QtGui, QtCore

class RegisterMenu(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(RegisterMenu, self).__init__(parent)
        self.initUI()

    def initUI(self):
    	self.resize(300, 300)        
        self.setWindowTitle('FingerPi Register')
        self.setWindowIcon(QtGui.QIcon('fingerpi.png'))

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you want to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()