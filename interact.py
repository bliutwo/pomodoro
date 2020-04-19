import sys
sys.dont_write_bytecode = True

from Pomodoro import *
from global_timer import *

class InteractivePomodoro(object):
    def __init__(self, ):
        self.session = Pomodoro()
        self.globaltimer = GlobalTimer()
