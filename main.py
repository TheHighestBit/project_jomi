#Siia tuleb üldine programmi loogika, mis kõik teised moodulid kokku seob
#Lisaks tuleb siia ka masinkoodi protsessimine, ehk siin failis tuleb
#käsud sisse lugeda.
import sys
import config, instructions
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
    raise Exception("Kasutus: Python failinimi.risc16")

with open(failinimi, 'r') as f:
    käsud = f.read().splitlines()

käsud = [käsk[:käsk.index(' //')] for käsk in käsud] #Eemaldame kommentaarid

while config.pc < len(käsud): #Programm jookseb seni, kuni käsud otsa saavad
    käsk = käsud[config.pc].split(' ')

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
    else:
        raise Exception("Ebakorrektne käsk!")