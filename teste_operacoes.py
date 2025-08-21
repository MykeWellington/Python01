import unittest
from operacoes import somar, subtrair, multiplicar, dividir

#Define uma classe de teste que herda de unittest.testcase
class TesteOperacoes(unittest.TestCase):
    def testar_somar(self):
        self.assertEqual(somar(2,3),5)
        self.assertEqual(somar(-1,1),0)
        self.assertEqual(somar(-2,-3),-5)
        
    def testar_subtrair(self):
        self.assertEqual(subtrair(5,3),2)
        self.assertEqual(subtrair(8,5), 3)
        self.assertEqual(subtrair(0,0), 0)
        
    def testar_multiplicar(self):
        self.assertEqual(multiplicar(5,3),15)
        self.assertEqual(multiplicar(5,10),50)
        self.assertEqual(multiplicar(-1,1), -1)
        
    def testar_dividir(self):
        self.assertEqual(dividir(5,5),1)
        self.assertEqual(dividir(-6,3),-2)
        with self.assertRaises(ValueError):
            dividir(1,0)
            
if __name__ == '__main__':
    unittest.main()