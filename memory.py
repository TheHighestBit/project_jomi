#Siia tuleb Memory class
#Iga sõna on 2 baiti, ehk mälu saab addresseerida kahe baidi kaupa

class Memory():
    def __init__(self, size): #Mälukogus peaks olema baitides (max 65536 baiti)
        assert size <= 65536, f"Max mälukogus on 65536 baiti, sina sisestasid aga: {size} baiti" 
        
        self.memory = ['0b' + '0' * 15 for _ in range(size)]

    def store(self, value, address): #Paigutab väärtuse value mällu vastavale aadressile
        #value peab olema kümnendsüsteemis ja type == int
        assert abs(value) <= 2 ** 15, f"Arv {value} on liiga suur"
        assert 0 <= address <= len(self.memory), f"See aadress {address} on mälupiirkonnast väljas"

        if value >= 0:
            self.memory[address] = '0b' + bin(value)[2:].rjust(15, '0')
        else:
            self.memory[address] = '-0b' + bin(value)[3:].rjust(15, '0')

    def load(self, address): #Laeb mälust väärtuse kahendsüsteemis
        assert 0 <= address <= len(self.memory), f"See aadress {address} on mälupiirkonnast väljas"

        return self.memory[address]