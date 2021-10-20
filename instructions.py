#Siia tuleb käskude loogika, kokku 8 käsku

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

