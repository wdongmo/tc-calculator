import unittest


from src.calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5), 5)
        self.assertEqual(self.calc.add(5), 10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3), -3)
        self.assertEqual(self.calc.subtract(2), -5)

    def test_multiply(self):
        self.calc.add(1)
        self.assertEqual(self.calc.multiply(5), 5)
        self.assertEqual(self.calc.multiply(4), 20)

    def test_division_by_zero(self):
        self.calc.add(10)
        with self.assertRaises(ValueError):
            self.calc.divide(0)

    def test_division(self):
        self.calc.add(10)
        self.assertEqual(self.calc.divide(5), 2)

    def test_root(self):
        self.calc.add(25)
        self.assertEqual(self.calc.root(2), 5)

    def test_root_negative_value(self):
        self.calc.add(-25)
        with self.assertRaises(ValueError):
            self.calc.root(2)

    def test_reset(self):
        self.calc.add(10)
        self.calc.multiply(100)
        self.assertEqual(self.calc.reset(), 0)
