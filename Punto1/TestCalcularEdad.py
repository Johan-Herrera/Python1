import unittest
from main import calcularEdad2070

class MyTestCase(unittest.TestCase):
    def test_calcularEdad2070(self):
        self.assertEqual(70,calcularEdad2070(20,2020))


if __name__ == '__main__':
    unittest.main()
