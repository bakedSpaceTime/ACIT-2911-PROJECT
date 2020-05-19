import time


class Timer():
    """ Timer Class """
    def __init__(self):
        """ Timer Constructor """
        self.start_time = None
        self.pause_at = None
        self.current = None
        self.paused_duration = 0
        self.previous = 0

    def start(self):
        """ Start Timer """
        self.start_time = time.time()

    def pause(self):
        """ Pause timer """
        self.pause_at = time.time()

    def resume(self):
        """ Resume timer """
        self.paused_duration += time.time() - self.pause_at

    def get_current(self):
        """ Get current timer time """
        self.current = time.time() - self.paused_duration
        return self.current - self.start_time

    def reset(self):
        """ Reset Timer """
        self.start()
        self.paused_duration = 0
        self.previous = 0
