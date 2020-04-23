import sys
sys.dont_write_bytecode = True

from Pomodoro import *
from global_timer import *

class PomodoroTimer(object):
    def __init__(self, session, start_with_break):
        self.onbreak = False
        if start_with_break == True:
            self.onbreak = True
        self.session = session
        # seconds
        self.remaining = self.session.get_pomodoro()
        if start_with_break == True:
            self.remaining = self.session.get_breaktime()
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
    def percentage(self):
        if self.onbreak == True:
            if self.session.get_number_pomo() % self.session.dividend == 0:
                return int(self.remaining / float(self.session.get_longbreak()) * 100)
            else:
                return int(self.remaining / float(self.session.get_breaktime()) * 100)
        else:
            return int(self.remaining / float(self.session.get_pomodoro()) * 100)

class InteractivePomodoro(object):
    # usage: interface = InteractivePomodoro(hours, mins, pomodoro_length)
    def __init__(self, hours, mins, pomodoro_length, start_with_break=True):
        self.session = Pomodoro() # what does this allow me to do?
        self.session.set_pomo(pomodoro_length)
        self.pomodoro_timer = PomodoroTimer(self.session, start_with_break)
        seconds = (hours * 3600) + (mins * 60)
        if start_with_break == True:
            seconds += self.session.get_breaktime()
        self.seconds = seconds
        self.globaltimer = GlobalTimer()
        self.globaltimer.set_timer(seconds)
        self.ending_pomo = 0
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
        num_pomo = self.session.get_number_pomo()
        if self.ending_pomo != 0:
            num_pomo = self.ending_pomo
        return str(num_pomo), gh, gm, gs, pm, ps
    def decrement(self):
        self.globaltimer.decrement()
        self.pomodoro_timer.decrement()
    def done(self):
        if self.globaltimer.done():
            percent = (100 - self.pomodoro_timer.percentage()) / 100.0
            self.ending_pomo = self.session.get_number_pomo() + percent
            return self.globaltimer.done()
    def break_status(self):
        return self.pomodoro_timer.break_status()
    def one_second_remaining(self):
        return self.pomodoro_timer.one_second_remaining()
    # returns what percentage we're through with the timers, pomodoro and global
    def percentages(self):
        return 100 - self.pomodoro_timer.percentage(), 100 - int(self.globaltimer.remaining_seconds() / float(self.seconds) * 100)
    def get_num_pomo(self):
        return self.session.get_number_pomo()
