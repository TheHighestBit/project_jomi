# Project Jomi
##### RiSC-16 arhitektuuri implementatsioon Pythonis

### Kasutamine
*Esmalt veendu, et oled projekti main kaustas kus on main.py*

python main.py path/to/masinkoodi_failinimi.risc16


## RiSC-16 arhitektuur
[Ülevaade](http://https://user.eng.umd.edu/~blj/risc/ "Ülevaade")

RiSC-16 on 8 16-bitise registriga arvuti arhitektuur, mida kasutatakse ennekõike õpetamiseks. Vaatamata oma lihtsusele on RiSC-16 arvutiga soovi korral võimalik luua vägagi keerulisi programme.

#### Käsud
**ADD rA, rB, rC** - Liida registrid B ja C ning salvesta tulemus registrisse A.

**ADDI rA, rB, imm** - Liida register B ja otsene väärtus imm ning salvesta tulemus registrisse A.

**NAND rA, rB, rC** - Teosta registrite B ja C vahel loogiline NAND ja salvesta tulemus registrisse A.

**LUI rA, imm** - Aseta 10 ülemist otseseväärtuse imm bitti registri A ülemise 10 biti asemele ja sea registri A alumised 6 bitti nullideks.

**SW rA, rB, imm** - Salvesta register A mällu aadressile register B + otseneväärtus imm.

**LW rA, rB, imm** - Lae registrisse A väärtus mäluaadressilt register B + otseneväärtus imm.

**BEQ rA, rB, imm** - Kui register A ja register B on võrdsed, siis liida programmiloendurile register B ja otseneväärtus imm + 1.

**JALR rA, rB** - Salvesta programmiloendur + 1 registrisse A ning Sea programmiloendur võrdseks registris B oleva väärtusega.

**PRINT rA** - Tõlgenda registri A sisu tähemärgina ja väljasta see.

**PRINTI rA** - Tõlgenda registri A sisu kümnendarvuna ja väljasta see.

**PRINTB rA** - Tõlgenda registri A sisu kahendarvuna ja väljasta see.

**NOP** - No operation, ära tee midagi.


Loodud kursuse Programmeerimine 1 raames. Loojateks: ***Joosep Orasmäe***, ***Jaan Kupri*** ja ***Rauno Raa***.
