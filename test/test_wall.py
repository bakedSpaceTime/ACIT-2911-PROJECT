import unittest
from wall import Obstacle


class TestWall(unittest.TestCase):
    def setUp(self):
        self.wall1 = Obstacle(450, 10)

    def test_constructor(self):
        self.assertIsNotNone(self.wall1)
        self.assertIsInstance(self.wall1, Obstacle)

    def test_constructor_invalid(self):
        with self.assertRaises(TypeError):
            wall2 = Obstacle('0', '4', 5, 7)