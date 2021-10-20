import sys
sys.path.append("..")

import unittest
import instructions, registers

trA = registers.Register()
trB = registers.Register()
trC = registers.Register()

class TestStringMethods(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()