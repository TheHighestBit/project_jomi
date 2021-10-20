#Siia tuleb registrite class

class Register():
    def __init__(self):
        self.bin_value = '0b000000000000000' #Selle registri sisu kahendkoodis

    def store(self, value): #Asetab kümnendsüsteemis oleva väärtuse registrisse kahendsüsteemis
        try:
            if abs(value) > 32767: #See on 2 ** 15 - 1, ehk maksimaalne suurus mis sellesse registrisse panna saab
                raise Exception(f'Väärtus {value} on selle registri jaoks liiga suur või liiga väike!')
            else:
                if value < 0: #Kui arv on negatiivne, tuleb märki ka arvestada 
                    märk = str(bin(value))[:3]
                    väärtus = str(bin(value))[3:]
                    self.bin_value = märk + väärtus.zfill(15) #Registris peab alati olema 15 bitti (1 märgi jaoks, aga seda arvestab Python ise)
                else:
                    väärtus = str(bin(value))[2:]
                    self.bin_value = '0b' + väärtus.zfill(15)
        except (TypeError, ValueError):
            raise AssertionError(f'register.store argument peab olema int, aga oli {type(value)}')

    def value(self): #Tagastab registri sisu kümnendsüsteemis (sisu kahendsüsteemis saab kätte r.bin_value)
        return int(self.bin_value, 2)