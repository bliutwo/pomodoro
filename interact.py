import sys
sys.dont_write_bytecode = True

from Pomodoro import *
from global_timer import *

class InteractivePomodoro(object):
    # usage: interface = InteractivePomodoro(hours, mins, pomodoro_length)
    def __init__(self, hours, mins, pomodoro_length):
        self.session = Pomodoro() # what does this allow me to do?
        seconds = (hours * 3600) + (mins * 60)
        self.globaltimer = GlobalTimer()
        self.globaltimer.set_timer(seconds)
        totalTime = (hours * 60) + mins
        pomodoroInMinutes = self.session.get_pomodoro() / 60
        if (totalTime < pomodoroInMinutes):
            totalTime = pomodoroInMinutes
        self.session.set_goal(totalTime)
        self.session.set_pomo(pomodoro_length)
        self.onbreak = False
    def output_remaining_time_strings(self):
        gh, gm, gs = self.globaltimer.remainder()
        gh = str(gh)
        gm = str(gm)
        gs = str(gs)
        if len(gh) == 1:
            gh = '0' + gh
        if len(gm) == 1:
            gm = '0' + gm
        if len(gs) == 1:
            gs = '0' + gs
        return gh, gm, gs
    def decrement_time_remaining(self):
        self.globaltimer.decrement()
