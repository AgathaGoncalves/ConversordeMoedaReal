import unittest
import conversoes

class TestConversao(unittest.TestCase):

    def testConverterparYen(self):
        self.assertEqual(conversoes.converterYen(100),2974)

    def testConverterDolar(self):
        self.assertEqual(conversoes.converterDolar(10),2.1)

    def testConverterparEuro(self):
        self.assertEqual(conversoes.converterEuro(1000),190)

   def testConverterparLibra(self):
        self.assertEqual(conversoes.converterLibra(10),1.60)

if  __name__=='__main__':
    unittest.main()
