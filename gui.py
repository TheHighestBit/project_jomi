#Siia tuleb graafilise kasutajaliidesega seonduv
import sys
import config
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget,QPushButton, QApplication, QLabel
from PyQt5 import QtCore

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
        self.start_stop.setFont(QFont('Arial', font_size+4))
        self.start_stop.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.start_stop.clicked.connect(self.start_stop_onclick)
        self.start_stop.setFixedSize(QtCore.QSize(500, 80))
        self.start_stop.setStyleSheet(
            "border-style: outset;" +
            "border-width: 2px;" +
            "border-radius: 15px;" + 
            "border-color: black;" +
            "padding: 25px;" +
            "background-color: yellow;"+
            "font-weight:bold;"
        )


        self.setStyleSheet("background-color: #6662a6;")
        command_rida.addWidget(self.start_stop)

        self.failinimi = QLabel()
        self.failinimi.setText('masinkood.risc16')
        self.failinimi.setFont(QFont('Arial', font_size))
        self.failinimi.setStyleSheet("padding:20px; font-weight:bold; font-size: 30px;color:white")
        command_rida.addWidget(self.failinimi)

        vbox.addLayout(command_rida)
        
        rida1 = QtWidgets.QHBoxLayout() #Teine rida
        rida1.addStretch()
        label_käskude_täitmine = QLabel()
        label_käskude_täitmine.setText("KÄSKUDE TÄITMINE:")
        label_käskude_täitmine.setAlignment(QtCore.Qt.AlignRight)
        label_käskude_täitmine.setFont(QFont('Arial', font_size))
        label_käskude_täitmine.setStyleSheet("padding: 20px 5px;font-weight:bold;font-size:25px") #Selliselt saab kõiki elemente disainida nii nagu soovi on
        rida1.addWidget(label_käskude_täitmine)
        rida1.addStretch()

        self.button_mode = QPushButton("AUTOMAATNE") #Nupp, mis muudab käskude täitmise viisi, kas automaatne või manuaalne
        self.button_mode.setFont(QFont('Arial', font_size+1))
        self.button_mode.clicked.connect(self.button_mode_onclick)
        self.button_mode.setFixedSize(QtCore.QSize(500, 80))
        self.button_mode.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button_mode.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_mode.setStyleSheet(
            "border: 4px solid '#BC006C';" +
            "border-style: outset;" +
            "border-width: 2px;" +
            "border-radius: 15px;" + 
            "border-color: black;" +
            "padding: 4px;" +
            "background-color: #d47d13;"
        )

        rida1.addWidget(self.button_mode)

        vbox.addLayout(rida1) #Lisame rea üldisesse layouti

        abi_rida = QHBoxLayout()
        abi_rida.addStretch()
        käsud = QLabel() #Lihtne label mis on käskude kohal
        käsud.setText("\nCall stack")
        käsud.setFont(QFont('Arial', font_size))
        käsud.setAlignment(QtCore.Qt.AlignCenter)
        käsud.setStyleSheet('font-weight:bold;text-decoration:underline')
        abi_rida.addWidget(käsud)
        abi_rida.addStretch()

        registrid = QLabel() #Lihtne label mis on registrite kohal
        registrid.setText("\nRegisters")
        registrid.setFont(QFont('Arial', font_size))
        registrid.setAlignment(QtCore.Qt.AlignCenter)
        registrid.setStyleSheet('font-weight:bold;text-decoration:underline')
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
        self.registrid.setAlignment(QtCore.Qt.AlignJustify)
        self.registrid.setText(registrid_näide)
        rida2.addWidget(self.registrid)
        rida2.addStretch()
        
        vbox.addLayout(rida2)

        rida3 = QHBoxLayout() #Selles reas kuvatakse mälukasutus
        self.label_ram = QLabel()
        self.label_ram.setText('RAM: 0/100 baiti') #Otseloomulikult uuendatakse ka mälukasutust automaatselt peale igat käsku
        self.label_ram.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ram.setFont(QFont('Arial', font_size + 10))
        rida3.addWidget(self.label_ram)

        vbox.addLayout(rida3)

        self.setLayout(vbox)
        self.setWindowTitle('Project Jomi')

    def button_mode_onclick(self):
        if self.button_mode.text() == "AUTOMAATNE":
            self.start_stop.setDisabled(True)
            self.button_mode.setText('MANUAALNE (edenemiseks vajutage "->" klahvi)')
            self.button_mode.setStyleSheet(
                "border: 4px solid '#BC006C';" +
                "border-style: outset;" +
                "border-width: 2px;" +
                "border-radius: 15px;" + 
                "border-color: black;" +
                "padding: 4px;" +
                "background-color: #8a5719;"+
                "outline:none"
            )
        else:
            self.start_stop.setEnabled(True)
            self.button_mode.setStyleSheet(
                "border: 4px solid '#BC006C';" +
                "border-style: outset;" +
                "border-width: 2px;" +
                "border-radius: 15px;" + 
                "border-color: black;" +
                "padding: 4px;" +
                "background-color: #d47d13;"+
                "outline:none"
            )
            self.button_mode.setText("AUTOMAATNE")

    def start_stop_onclick(self):
        if self.start_stop.text() == "START":
            config.running = True
            self.start_stop.setText("STOP")
            self.start_stop.setStyleSheet(
            "border-style: outset;" +
            "border-width: 2px;" +
            "border-radius: 15px;" + 
            "border-color: black;" +
            "padding: 25px 0;" +
            "background-color: red;"+
            "font-weight:bold;"+
            "outline:none"
            )
        else:
            config.running = False
            self.start_stop.setText("START")
            self.start_stop.setStyleSheet(
            "border-style: outset;" +
            "border-width: 2px;" +
            "border-radius: 15px;" + 
            "border-color: black;" +
            "padding: 25px 0;" +
            "background-color: yellow;"+
            "font-weight:bold;"+
            "outline:none"
            )
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Right and self.button_mode.text() == 'MANUAALNE (edenemiseks vajutage "->" klahvi)':
            config.running = True

    def update_käsud(self, käsud, pc=-1): #Funktsioon, mis uuendab sõne mida kuvatakse kasutajale
        väljund = ''
        
        if len(käsud) >= 11 and pc != -1: #Nool pannakse käsud[pc] kõrvale
            for i, käsk in enumerate(käsud):
                if config.pc < 11:
                    käsk_töödeldud = (' ' * 6) + str(i) + ': ' + (käsk).ljust(14)
                else:
                    käsk_töödeldud = (' ' * 6) + str(i + config.pc - pc) + ': ' + (käsk).ljust(14)
                if i == pc:
                    väljund += '-->' + käsk_töödeldud[4:]
                else:
                    väljund += käsk_töödeldud

                väljund += '\n'
        
        elif len(käsud) < 11 and pc != -1:
            for i, käsk in enumerate(käsud):
                käsk_töödeldud = (' ' * 6) + str(i) + ': ' + (käsk).ljust(14)
                if i == pc:
                    väljund += '-->' + käsk_töödeldud[4:]
                else:
                    väljund += käsk_töödeldud

                väljund += '\n'
        else: #Nool läheb keskmise käsu kõrvale
            keskmine = (len(käsud) // 2) + 1

            for i, käsk in enumerate(käsud):
                käsk_töödeldud = (' ' * 6) + str(i + config.pc - 6) + ': ' + (käsk).ljust(14)
                if i == keskmine:
                    väljund += '-->' + käsk_töödeldud[4:]
                else:
                    väljund += käsk_töödeldud

                väljund += '\n'

        self.label_käsud.setText(väljund)

    def update_registers(self): #Uuendab kasutajale kuvatavate registrite sisu
        väljund = ' ' * 7 + 'R0: #0' + '\n'

        väljund += ' ' * 7 + 'R1: #' + (str(config.r1.value())).ljust(15) + '\n'
        väljund += ' ' * 7 + 'R2: #' + (str(config.r2.value())).ljust(15) + '\n'
        väljund += ' ' * 7 + 'R3: #' + (str(config.r3.value())).ljust(15) + '\n'
        väljund += ' ' * 7 + 'R4: #' + (str(config.r4.value())).ljust(15) + '\n'
        väljund += ' ' * 7 + 'R5: #' + (str(config.r5.value())).ljust(15) + '\n'
        väljund += ' ' * 7 + 'R6: #' + (str(config.r6.value())).ljust(15) + '\n'
        väljund += ' ' * 7 + 'R7: #' + (str(config.r7.value())).ljust(15) + '\n'

        self.registrid.setText(väljund)

    def increase_ram(self):
        config.used_ram += 1
        
        protsent = (100 * config.used_ram) / len(config.mälu.memory)
        self.label_ram.setText(f'RAM: {protsent}% {config.used_ram} B')

    def decrease_ram(self):
        if config.used_ram != 0:
            config.used_ram -= 1
        
        protsent = (100 * config.used_ram) / len(config.mälu.memory)
        self.label_ram.setText(f'RAM: {protsent}% {config.used_ram} B')

    def closeEvent(self, event):
        event.accept()
        config.close = True