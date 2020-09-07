import unittest
from main import imprimirPrimeraUltima

class MyTestCase(unittest.TestCase):
    def Test_imprimirPrimeraUltima(self):
        self.assertEqual("La primera letra es 'p' La segunda letra es 'a'", imprimirPrimeraUltima)


if __name__ == '__main__':
    unittest.main()
