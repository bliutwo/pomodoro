import sys
sys.dont_write_bytecode = True

from Pomodoro import *
from global_timer import *

class PomodoroTimer(object):
    def __init__(self, session):
        self.onbreak = False
        self.session = session
        print(self.session.get_pomodoro())
        print(self.session.get_breaktime())
        print(self.session.get_longbreak())
        # seconds
        self.remaining = self.session.get_pomodoro()
    # TODO: logic about whether break or not, and how that affects self.remaining
    def decrement(self):
        self.remaining = self.remaining - 1
        if self.remaining == 0:
            if self.onbreak == False:
                self.onbreak = True
                self.session.add()
                if self.session.get_number_pomo() % self.session.dividend == 0:
                    self.remaining = self.session.get_longbreak()
                else:
                    self.remaining = self.session.get_breaktime()
            else:
                self.onbreak = False
                self.remaining = self.session.get_pomodoro()
    def remainder(self):
        m = self.remaining / 60 % 60
        s = self.remaining % 60
        return int(m), int(s)
    def break_status(self):
        return self.onbreak
    def one_second_remaining(self):
        return self.remaining == 1

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
        self.pomodoro_timer = PomodoroTimer(self.session)
    def output_remaining_time_strings(self):
        gh, gm, gs = self.globaltimer.remainder()
        pm, ps = self.pomodoro_timer.remainder()
        onbreak = self.pomodoro_timer.break_status()
        gh = str(gh)
        gm = str(gm)
        gs = str(gs)
        pm = str(pm)
        ps = str(ps)
        if len(gh) == 1:
            gh = '0' + gh
        if len(gm) == 1:
            gm = '0' + gm
        if len(gs) == 1:
            gs = '0' + gs
        if len(pm) == 1:
            pm = '0' + pm
        if len(ps) == 1:
            ps = '0' + ps
        return self.session.get_number_pomo(), onbreak, gh, gm, gs, pm, ps
    def decrement_time_remaining(self):
        self.globaltimer.decrement()
        self.pomodoro_timer.decrement()
    def done(self):
        return self.globaltimer.done()
    def break_status(self):
        return self.pomodoro_timer.break_status()
    def one_second_remaining(self):
        return self.pomodoro_timer.one_second_remaining()
