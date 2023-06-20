import unittest
import conversoes

class TestConversao(unittest.TestCase):

    def testConverterparYen(self):
        self.assertEqual(conversoes.converterYen(100),2974)


if  __name__=='__main__':
    unittest.main()