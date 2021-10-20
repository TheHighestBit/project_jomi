#Siia tuleb käskude loogika, kokku 8 käsku

def nand_abi(bit1, bit2): #Funktsioon, mis tagastab NAND tulemuse nende kahe biti vahel
    return '0' if bit1 == '1' and bit2 == '1' else '1'

def ADD(rA, rB, rC): #Add contents of regB with regC, store result in regA
    rA.store(rB.value() + rC.value())

def ADDI(rA, rB, imm): #Add contents of regB with imm, store result in regA.
    #Kui imm on kümnendsüsteemis ehk #
    if '#' in imm:
        rA.store(rB.value() + int(imm[1:]))
    #kuueteistkümnendik süsteem
    elif '$' in imm:
        rA.store(rB.value() + int(imm[1:], 16))
    #kahendiksüsteem
    elif 'O' in imm:
        rA.store(rB.value() + int(imm[1:], 8))
    #octal
    else:
        rA.store(rB.value() + int(imm[1:], 2))

def NAND(rA, rB, rC): #Nand contents of regB with regC, store results in regA.
        #See käsk on väga kahtlane, kuna NANDis kasutatakse kogu registrit, mitte ainult relevantseid bitte
        #Pole kindel, kas see töötab õieti

        #Peame kontrollima, kas registrites on negatiivsed arvud
        if '-' in rB.bin_value and '-' not in rC.bin_value:
            rA.store(int('-0b' + ''.join([nand_abi(bit1, bit2) for bit1, bit2 in zip(rB.bin_value[3:], rC.bin_value[2:])]), 2))
        elif '-' not in rB.bin_value and '-' in rC.bin_value:
            rA.store(int('-0b' + ''.join([nand_abi(bit1, bit2) for bit1, bit2 in zip(rB.bin_value[2:], rC.bin_value[3:])]), 2))
        elif '-' not in rB.bin_value and '-' not in rC.bin_value:
            rA.store(int('-0b' + ''.join([nand_abi(bit1, bit2) for bit1, bit2 in zip(rB.bin_value[2:], rC.bin_value[2:])]), 2))
        else:
            rA.store(int('0b' + ''.join([nand_abi(bit1, bit2) for bit1, bit2 in zip(rB.bin_value[3:], rC.bin_value[3:])]), 2))