import unittest
from game import Game
from player import Player
from wall import Wall
import pygame
from settings import GAME_SETTINGS, PLAYER_SETTINS, PLAYER_SPRITES


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.game1 = Game()
        self.player = Player(self.game1)
        self.wall = Wall(0, 0, 10, 500)

    def test_constructor(self):
        self.assertIsNotNone(self.game1)
        self.assertIsInstance(self.game1, Game)

        self.assertIsNotNone(self.player)
        self.assertIsInstance(self.player, Player)

    def test_constructor_invalid(self):
        with self.assertRaises(TypeError):
            player2 = Player(420)
            player3 = Player('Strength')

    def test_is_in_bounds(self):
        with self.assertRaises(ValueError):
            self.player.is_in_bounds("lol")

    def test_will_hit_wall(self):
        """ testing if player will hit a all at the starting location """
        self.assertFalse(self.player.will_hit_wall("up"))
        self.assertTrue(self.player.will_hit_wall("right"))
        self.assertTrue(self.player.will_hit_wall("down"))
        self.assertFalse(self.player.will_hit_wall("left"))

    def test_align_with_wall(self):
        self.player.align_with_wall("left", self.wall)
        self.assertEqual(self.player.rect.left, self.wall.rect.right)

        self.player.align_with_wall("up", self.wall)
        self.assertEqual(self.player.rect.top, self.wall.rect.bottom)

    def test_switch_directions(self):
        key = pygame.K_LEFT
        self.player.switch_directions(key)
        self.assertTrue(self.player.directions["left"])
        self.assertFalse(self.player.directions["right"])
        self.assertFalse(self.player.directions["up"])
        self.assertFalse(self.player.directions["down"])

    def test_move_player(self):
        key = pygame.K_LEFT
        self.player.switch_directions(key)
        self.player.move_player()
        self.assertEqual(1, self.player.score)

        key = pygame.K_RIGHT
        self.player.switch_directions(key)
        self.player.move_player()
        self.assertEqual(1, self.player.score)

        key = pygame.K_UP
        self.player.switch_directions(key)
        self.player.move_player()
        self.assertEqual(1, self.player.score)

        key = pygame.K_DOWN
        self.player.switch_directions(key)
        self.player.move_player()
        self.assertEqual(1, self.player.score)



