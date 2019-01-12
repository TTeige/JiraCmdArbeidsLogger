import time
import math
from multiprocessing.pool import ThreadPool


class TimerModule:

    def __init__(self):
        self.currently_timing = False
        self.async_result = None
        self.pool = ThreadPool(processes=1)
        self.should_print_timer = ""

    def start(self, print_timer):
        if print_timer != "":
            self.should_print_timer = print_timer
        if self.currently_timing is False:
            self.currently_timing = True
            if self.async_result is None:
                self.async_result = self.pool.apply_async(self.start_timer, ())
        else:
            print("Finish current timing")

    def end(self):
        if self.async_result is not None:
            self.currently_timing = False
            start_time, time_spent = self.async_result.get()
            self.async_result = None
            self.should_print_timer = ""
            return start_time, time_spent
        else:
            print("Start timer first")

    def start_timer(self):
        start_time = time.time()
        sec = 0
        minute = 0
        hour = 0
        print("\n")
        while self.currently_timing:
            if self.should_print_timer != "":
                if round(time.time() - start_time) > sec:
                    sec += 1
                    if sec % 60 == 0:
                        minute += 1
                    if minute % 60 == 0 and minute != 0:
                        hour += 1
                    print("\r   Current time: Hrs: %d Min: %d Sec: %d \r" % (hour, minute, sec % 60), sep=' ', end='',
                          flush=True)
        print("\n")
        return start_time, time.time() - start_time


def format_time_to_string(seconds):
    hour = math.floor(seconds / 3600)
    minutes = math.floor(seconds / 360)
    sec = round(seconds % 60)
    return "%dh %dm %ss" % (hour, minutes, sec)
