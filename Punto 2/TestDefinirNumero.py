import unittest
from main import definirNumero

class MyTestCase(unittest.TestCase):
    def test_definirNumero(self):
        self.assertEqual('El número es par.', definirNumero(4))


if __name__ == '__main__':
    unittest.main()
