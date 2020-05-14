import unittest
from unittest import mock
from game import Game


class TestGame(unittest.TestCase):

    def does_nothing(self):
        pass

    @mock.patch('game.Game._initialize_music')
    def setUp(self, does_nothing):
        self.game1 = Game()

    def test_constructor(self):
        self.assertIsNotNone(self.game1)
        self.assertIsInstance(self.game1, Game)

    def test_constructor_invalid(self):
        with self.assertRaises(TypeError):
            game2 = Game(5, 7)
            game3 = Game('START')
