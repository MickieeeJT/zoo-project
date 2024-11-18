import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_age_less_than_zero(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)  # C1b1

    def test_age_between_0_and_12(self):
        self.assertEqual(self.zoo.get_ticket_price(1), 50)  # C1b2

    def test_age_between_13_and_20(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)  # C1b3

    def test_age_between_21_and_60(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)  # C1b4

    def test_age_above_60(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)  # C1b5

if __name__ == '__main__':
    unittest.main()
