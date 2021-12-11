#Siia tuleb graafilise kasutajaliidesega seonduv
import sys
import config
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QGridLayout,QPushButton, QApplication, QLabel
from PyQt5 import Qt, QtCore

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        font_size = 15 #Kogu programmi font size, uute elementide loomisel tuleks seda kasutada
        käskude_näide = 'ADD R1, R2, R3\n' * 5 #Näide käskudest, mida kuvatakse, see genereeritakse pärisprogrammis automaatselt
        registrid_näide = ''.join(['R' + str(x) + ': #420' + '\n' for x in range(8)]) #Näide registrite olekutest, see genereeritakse peale igat käsku automaatselt
        
        command_rida = QtWidgets.QHBoxLayout() #Selles reas on start, paus ja programmi nimi
        self.start_stop = QPushButton()
        self.start_stop.setText("START")
        self.start_stop.setFont(QFont('Arial', font_size))
        self.start_stop.clicked.connect(self.start_stop_onclick)
        self.start_stop.setFixedSize(QtCore.QSize(500, 80))
        self.start_stop.setFocusPolicy(QtCore.Qt.NoFocus)
        command_rida.addWidget(self.start_stop)

        self.failinimi = QLabel()
        self.failinimi.setText('masinkood.risc16')
        self.failinimi.setFont(QFont('Arial', font_size))
        command_rida.addWidget(self.failinimi)

        vbox.addLayout(command_rida)
        
        rida1 = QtWidgets.QHBoxLayout() #Teine rida
        rida1.addStretch()
        label_käskude_täitmine = QLabel()
        label_käskude_täitmine.setText("Käskude täitmine:")
        label_käskude_täitmine.setAlignment(QtCore.Qt.AlignRight)
        label_käskude_täitmine.setFont(QFont('Arial', font_size))
        label_käskude_täitmine.setStyleSheet("padding: 15px;text-decoration: underline") #Selliselt saab kõiki elemente disainida nii nagu soovi on
        rida1.addWidget(label_käskude_täitmine)
        rida1.addStretch()

        self.button_mode = QPushButton("AUTOMAATNE") #Nupp, mis muudab käskude täitmise viisi, kas automaatne või manuaalne
        self.button_mode.setFont(QFont('Arial', font_size))
        self.button_mode.clicked.connect(self.button_mode_onclick)
        self.button_mode.setFixedSize(QtCore.QSize(500, 80))
        self.button_mode.setFocusPolicy(QtCore.Qt.NoFocus)
        rida1.addWidget(self.button_mode)

        vbox.addLayout(rida1) #Lisame rea üldisesse layouti

        abi_rida = QHBoxLayout()
        abi_rida.addStretch()
        käsud = QLabel() #Lihtne label mis on käskude kohal
        käsud.setText("Call stack")
        käsud.setFont(QFont('Arial', font_size))
        käsud.setAlignment(QtCore.Qt.AlignCenter)
        abi_rida.addWidget(käsud)
        abi_rida.addStretch()

        registrid = QLabel() #Lihtne label mis on registrite kohal
        registrid.setText("Registers")
        registrid.setFont(QFont('Arial', font_size))
        registrid.setAlignment(QtCore.Qt.AlignCenter)
        abi_rida.addWidget(registrid)
        abi_rida.addStretch()

        vbox.addLayout(abi_rida)

        rida2 = QHBoxLayout() #Selles reas on registrite ja käskude näitamine
        rida2.addStretch()
        self.label_käsud = QLabel()
        self.label_käsud.setText(käskude_näide)
        self.label_käsud.setFont(QFont('Arial', font_size))
        self.label_käsud.setAlignment(QtCore.Qt.AlignLeft)
        rida2.addWidget(self.label_käsud)
        rida2.addStretch()

        self.registrid = QLabel()
        self.registrid.setFont(QFont('Arial', font_size))
        self.registrid.setAlignment(QtCore.Qt.AlignCenter)
        self.registrid.setText(registrid_näide)
        rida2.addWidget(self.registrid)
        rida2.addStretch()
        
        vbox.addLayout(rida2)

        rida3 = QHBoxLayout() #Selles reas kuvatakse mälukasutus
        self.label_ram = QLabel()
        self.label_ram.setText('RAM: 0/100 baiti') #Otseloomulikult uuendatakse ka mälukasutust automaatselt peale igat käsku
        self.label_ram.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ram.setFont(QFont('Arial', font_size + 5))
        rida3.addWidget(self.label_ram)

        vbox.addLayout(rida3)

        self.setLayout(vbox)
        self.setWindowTitle('Project Jomi')

    def button_mode_onclick(self):
        if self.button_mode.text() == "AUTOMAATNE":
            self.start_stop.setDisabled(True)
            self.button_mode.setText("MANUAALNE")
        else:
            self.start_stop.setEnabled(True)
            self.button_mode.setText("AUTOMAATNE")

    def start_stop_onclick(self):
        if self.start_stop.text() == "START":
            config.running = True
            self.start_stop.setText("STOP")
        else:
            config.running = False
            self.start_stop.setText("START")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Right and self.button_mode.text() == "MANUAALNE":
            config.running = True

    def update_käsud(self, käsud, pc=-1): #Funktsioon, mis uuendab sõne mida kuvatakse kasutajale
        väljund = ''
        
        if len(käsud) < 11 or pc != -1: #Nool pannakse käsud[pc] kõrvale
            for i, käsk in enumerate(käsud):
                käsk_töödeldud = ' ' * 6 + (käsk).ljust(14)
                if i == pc:
                    väljund += '-->' + käsk_töödeldud[4:]
                else:
                    väljund += käsk_töödeldud

                väljund += '\n'
        
        else: #Nool läheb keskmise käsu kõrvale
            keskmine = (len(käsud) // 2)

            for i, käsk in enumerate(käsud):
                käsk_töödeldud = ' ' * 6 + (käsk).ljust(14)
                if i == keskmine:
                    väljund += '-->' + käsk_töödeldud[4:]
                else:
                    väljund += käsk_töödeldud

                väljund += '\n'

        self.label_käsud.setText(väljund)

    def closeEvent(self, event):
        event.accept()
        config.close = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = GUI()
    windowExample.show()
    sys.exit(app.exec_())
