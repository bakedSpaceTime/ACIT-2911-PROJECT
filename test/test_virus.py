import unittest
from unittest import mock
from game import Game
from player import Player
from virus import Virus
from wall import Obstacle
import pygame
from settings import GAME_SETTINGS, PLAYER_SETTINS, PLAYER_SPRITES, WALL_LIST_1ST_FLOOR, VIRUS_SETTINS


class TestVirus(unittest.TestCase):

    def does_nothing(self):
        pass

    def no_path(self):
        pass

    def no_snap(self):
        pass


    @mock.patch('game.Game._initialize_music')
    @mock.patch('settings.VIRUS_SETTINS', [
    {
        "starting_x": 30,
        "starting_y": 180,
        "velocity": 8,
    },])
    @mock.patch('virus.Virus.update_path')
    @mock.patch('virus.Virus.snap_to_node')
    def setUp(self, does_nothing, no_path, no_snap):
        self.game1 = Game()
        self.player = Player(self.game1)
        self.virus = Virus(self.game1, 1, WALL_LIST_1ST_FLOOR["virus"])

    def test_constructor(self):
        self.assertIsNotNone(self.game1)
        self.assertIsInstance(self.game1, Game)

        self.assertIsNotNone(self.player)
        self.assertIsInstance(self.player, Player)

        self.assertIsNotNone(self.virus)
        self.assertIsInstance(self.virus, Virus)

    def mock_direction(self):
        return 0

    @mock.patch('virus.Virus.direction_of_next_node')
    def test_switch_directions(self, mock_direction):
        self.assertIsNone(self.virus.switch_directions())

    def test_move(self):
        self.assertIsNone(self.virus.move())

