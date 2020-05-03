import unittest
from loot import ToiletPaper


class TestWall(unittest.TestCase):
    def setUp(self):
        self.loot1 = ToiletPaper(50, 50)

    def test_constructor(self):
        self.assertIsNotNone(self.loot1)
        self.assertIsInstance(self.loot1, ToiletPaper)

    def test_constructor_invalid(self):
        with self.assertRaises(TypeError):
            loot2 = ToiletPaper('0', '4', 5, 7)