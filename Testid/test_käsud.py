import sys
sys.path.append("..")

import unittest
import instructions, registers

trA = registers.Register()
trB = registers.Register()
trC = registers.Register()

class TestKäsud(unittest.TestCase):
    def test_ADD(self):
        #Kahe positiivse täisarvu liitmine
        trB.store(15)
        trC.store(30)
        instructions.ADD(trA, trB, trC)
        self.assertEqual(trA.value(), 45)

        #Negatiivse ja positiivse täisarvu liitmine
        trB.store(15)
        trC.store(-30)
        instructions.ADD(trA, trB, trC)
        self.assertEqual(trA.value(), -15)

        #Liitmine nulli ja positiivse täisarvuga
        trB.store(15)
        trC.store(0)
        instructions.ADD(trA, trB, trC)
        self.assertEqual(trA.value(), 15)

        #Liitmine nulliga ja negatiivse täisarvuga
        trB.store(-15)
        trC.store(0)
        instructions.ADD(trA, trB, trC)
        self.assertEqual(trA.value(), -15)

    def test_ADDI(self):
        #Kümnendsüsteemis imm
        trB.store(10)
        instructions.ADDI(trA, trB, '#300')
        self.assertEqual(trA.value(), 310)

        #hex imm
        trB.store(10)
        instructions.ADDI(trA, trB, '$64')
        self.assertEqual(trA.value(), 110)

        #octal imm
        trB.store(10)
        instructions.ADDI(trA, trB, 'O144')
        self.assertEqual(trA.value(), 110)

        #binary imm
        trB.store(10)
        instructions.ADDI(trA, trB, '%1100100')
        self.assertEqual(trA.value(), 110)

if __name__ == '__main__':
    unittest.main()