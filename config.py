from registers import Register
from memory import Memory

#Siia tuleks defineerida globaalsed muutujad, mida üle kogu projekti kasutada
#Nt. tuleks siin defineerida kõik registrid, mälu olek jne.
def init():
    global r0
    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global r7
    global mälu
    global pc #program counter, lihtsalt tavaline int
    global running #Bool kas programm jookseb või mitte
    global close #Bool kas programmi aken on suletud ja kas programm tuleks peatada
    global used_ram #Jälgib, mitu baiti mälu on kasutuses

    r0 = Register(is_0=True) #Selle registri väärtus on alati null!
    r1 = Register()
    r2 = Register()
    r3 = Register()
    r4 = Register()
    r5 = Register()
    r6 = Register()
    r7 = Register()
    pc = 0

    mälu = Memory(128)

    running = False
    close = False
    used_ram = 0