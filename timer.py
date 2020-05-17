import time


class Timer():
    def __init__(self):
        self.start_time = None
        self.pause_at = None
        self.current = None
        self.paused_duration = 0
        self.previous = 0

    def start(self):
        self.start_time = time.time()

    def pause(self):
        self.pause_at = time.time()

    def resume(self):
        self.paused_duration += time.time() - self.pause_at

    def get_current(self):
        self.current = time.time() - self.paused_duration
        return self.current - self.start_time

    def reset(self):
        self.start()
        self.paused_duration = 0
        self.previous = 0
