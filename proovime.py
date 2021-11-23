import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("RISC-16 arhitektuur!!")
window.setFixedWidth(1000)
window.setStyleSheet("background: DarkSlateGrey")

window.show()
sys.exit(app.exec())