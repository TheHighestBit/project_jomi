#Siia tuleb käskude loogika, kokku 8 käsku

def ADD(rA, rB, rC): #Add contents of regB with regC, store result in regA
    rA.store(rB.value() + rC.value())