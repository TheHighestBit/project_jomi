#Siia tuleb käskude loogika, kokku 8 käsku

def nand_abi(bit1, bit2): #Funktsioon, mis tagastab NAND tulemuse nende kahe biti vahel
    return '0' if bit1 == '1' and bit2 == '1' else '1'

def decode_imm(imm): #tagastab kümnendarvu
    #kümnendsüsteem
    if '#' in imm:
        return int(imm[1:])
    #kuueteistkümnendik süsteem
    elif '$' in imm:
        return int(imm[1:], 16)
    #kahendiksüsteem
    elif 'O' in imm:
        return int(imm[1:], 8)
    #octal
    else:
        return int(imm[1:], 2)

def ADD(rA, rB, rC): #Add contents of regB with regC, store result in regA
    rA.store(rB.value() + rC.value())

def ADDI(rA, rB, imm): #Add contents of regB with imm, store result in regA.
    rA.store(rB.value() + decode_imm(imm))

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

def LUI(rA, imm): #Place the 10 ten bits of the 16-bit imm into the 10 ten bits of regA, setting the bottom 6 bits of regA to zero.
    #Ülemised bitid on vasakul ja alumised paremal
    imm_in_bin = bin(decode_imm(imm))

    if '-' in imm_in_bin:
        if (len(imm_in_bin) - 3) < 10:
            imm_in_bin = imm_in_bin[3:].rjust(10, '0')
            rA.bin_value = '-0b00000' + imm_in_bin
        else:
            imm_in_bin = imm_in_bin[-10:]
            rA.bin_value = '-0b00000' + imm_in_bin
    else:
        if (len(imm_in_bin) - 2) < 10:
            imm_in_bin = imm_in_bin[2:].rjust(10, '0')
            rA.bin_value = '0b00000' + imm_in_bin
        else:
            imm_in_bin = imm_in_bin[-10:]
            rA.bin_value = '0b00000' + imm_in_bin
