#Siia tuleb graafilise kasutajaliidesega seonduv
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget,  QFileDialog, QGridLayout, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtGui import QCursor


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("MainWindow.ui", self)
        self.button2 = QPushButton("Automaatne")
        def OtherWindow():
            uic.loadUi("OtherWindow.ui",self)
        self.button2.clicked.connect(OtherWindow)
        self.show()
    
        
   
    
        

        
app = QApplication(sys.argv)
window = Ui()
app.exec_()


    




