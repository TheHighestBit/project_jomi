#Siia tuleb graafilise kasutajaliidesega seonduv
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget,  QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("RISC-16 arhitektuur!!")
window.setFixedWidth(1000)
window.setStyleSheet("background: DarkSlateGrey")

grid = QGridLayout()

#button widget
button = QPushButton("AUTOMAATNE")
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button.setStyleSheet(
    "border: 4px solid 'Aquamarine';" +
    "border-radius: 15px;" +
    "font-size: 20px;" +
    "color: 'white';"
)

button2 = QPushButton("MANUAALNE")
button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button2.setStyleSheet(
    "border: 4px solid 'Aquamarine';" +
    "border-radius: 15px;" +
    "font-size: 20px;" +
    "color: 'white';"
)
button2.move(64,64)


grid.addWidget(button, 1, 0)
grid.addWidget(button2, 1, 0)
window.setLayout(grid)
window.show()



sys.exit(app.exec())