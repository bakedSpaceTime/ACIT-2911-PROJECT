import unittest
from wall import Wall


class TestWall(unittest.TestCase):
    def setUp(self):
        self.wall1 = Wall(0, 100, 450, 10)

    def test_constructor(self):
        self.assertIsNotNone(self.wall1)
        self.assertIsInstance(self.wall1, Wall)

    def test_constructor_invalid(self):
        with self.assertRaises(TypeError):
            wall2 = Wall('0', '4', 5, 7)