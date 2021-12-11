#Siia tuleb üldine programmi loogika, mis kõik teised moodulid kokku seob
#Lisaks tuleb siia ka masinkoodi protsessimine, ehk siin failis tuleb
#käsud sisse lugeda.
import sys
import config, instructions
from gui import GUI
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
config.init()

register_map = {
    'R0': config.r0,
    'R1': config.r1,
    'R2': config.r2,
    'R3': config.r3,
    'R4': config.r4,
    'R5': config.r5,
    'R6': config.r6,
    'R7': config.r7
}

if len(sys.argv) > 1:
    failinimi = sys.argv[1]
else:
    raise Exception("Kasutus: python main.py failinimi.risc16")

try:
    with open(failinimi, 'r', encoding='UTF-8') as f:
        käsud = f.read().splitlines()
except:
    raise Exception("Faili avamisel tekkis viga! Veendu, et antud fail eksisteeriks!")


app = QApplication(sys.argv)
gui = GUI()
gui.show()

gui.failinimi.setText(failinimi)

käsud = [käsk[:käsk.index('//')] if '//' in käsk else käsk for käsk in käsud] #Eemaldame kommentaarid

def kuva_käsud(): #Kuvab kasutajale ülevaate käskudest
    if len(käsud) < 11:
        gui.update_käsud(käsud, config.pc)
    elif (len(käsud) - config.pc) <= 4:
        gui.update_käsud(käsud[::-1][:11], (11 - len(käsud) + config.pc) - 1)
    elif config.pc <= 6:
        gui.update_käsud(käsud[:11], config.pc)
    else:
        gui.update_käsud(käsud[config.pc - 6:config.pc + 5])

def wait(n): #Ootab n millisekundit
    loop = QtCore.QEventLoop()
    QtCore.QTimer.singleShot(n, loop.quit)
    loop.exec_()

kuva_käsud()
gui.update_registers()

while config.pc != (len(käsud)):
    if config.close == True:
        exit()
    if config.running:
        käsk = käsud[config.pc].split(' ')

        if len(käsk) == 1 and käsk[0] == '':
            config.pc += 1
            kuva_käsud()
            continue

        if käsk[0] == 'ADDI':
            instructions.ADDI(register_map[käsk[1].strip(',')], register_map[käsk[2].strip(',')], käsk[3])
        elif käsk[0] == 'LUI':
            instructions.LUI(register_map[käsk[1].strip(',')], käsk[2])
        elif käsk[0] == 'ADD':
            instructions.ADD(register_map[käsk[1].strip(',')], register_map[käsk[2].strip(',')], register_map[käsk[3].strip(',')])
        elif käsk[0] == 'NAND':
            instructions.NAND(register_map[käsk[1].strip(',')], register_map[käsk[2].strip(',')], register_map[käsk[3].strip(',')])
        elif käsk[0] == 'SW':
            instructions.SW(register_map[käsk[1].strip(',')], register_map[käsk[2].strip(',')], käsk[3])
        elif käsk[0] == 'LW':
            instructions.LW(register_map[käsk[1].strip(',')], register_map[käsk[2].strip(',')], käsk[3])
        elif käsk[0] == 'BEQ':
            instructions.BEQ(register_map[käsk[1].strip(',')], register_map[käsk[2].strip(',')], käsk[3])
        elif käsk[0] == 'JALR':
            instructions.JALR(register_map[käsk[1].strip(',')], register_map[käsk[2].strip(',')])
        elif käsk[0] == 'PRINT': #Kuvab ekraanile registri sisu ASCII märgina
            print(chr(register_map[käsk[1]].value()))
            config.pc += 1
        elif käsk[0] == 'PRINTB': #Kuvab ekraanile registri sisu kahendkoodis
            print(register_map[käsk[1]].bin_value)
            config.pc += 1
        elif käsk[0] == 'PRINTI': #Kuvab ekraanile registri sisu kümnendkoodis
            print(register_map[käsk[1]].value())
            config.pc += 1
        else:
            raise Exception(f"Ebakorrektne käsk! Rida: {config.pc}")


        if gui.button_mode.text() == "MANUAALNE":
            config.running = False
        else:
            wait(1000)
        
        gui.update_registers()
        kuva_käsud()
    
    else: #Kuna kasutame pollimist, peame siis mõned millisekundid ootama, et CPU tühja ei käiks
        wait(10)

sys.exit(app.exec_())
