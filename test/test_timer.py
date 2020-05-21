import unittest
from unittest import mock
from timer import Timer
import time


class TestTimer(unittest.TestCase):

    def does_nothing(self):
        pass

    @mock.patch('game.Game._initialize_music')
    def setUp(self, does_nothing):
        self.timer = Timer()

    def test_constructor(self):
        self.assertIsNotNone(self.timer)
        self.assertIsInstance(self.timer, Timer)

    def test_constructor_invalid(self):
        with self.assertRaises(TypeError):
            timer2 = Timer(420)
            timer3 = Timer('Strength')

    def test_start(self):
        self.timer.start()
        self.assertEqual(self.timer.start_time, time.time())

    def test_pause(self):
        self.timer.pause()
        self.assertEqual(self.timer.pause_at, time.time())

    def test_resume(self):
        self.assertEqual(self.timer.paused_duration, 0)
        self.timer.start()
        self.timer.pause()
        self.timer.resume()
        self.assertEqual(self.timer.paused_duration, 0)

    def test_get_current(self):
        self.timer.start()
        self.timer.pause()
        self.timer.resume()
        self.assertEqual(self.timer.get_current(), 0)

    def test_reset(self):
        self.timer.start()
        self.timer.reset()
        self.assertEqual(self.timer.paused_duration, 0)
        self.assertEqual(self.timer.previous, 0)