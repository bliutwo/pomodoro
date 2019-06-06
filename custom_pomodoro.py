# Filename: custom_pomodoro.py
# Description: Theoretical final pomodoro file, for when you have a limited time
# to work, or you only plan to work a certain amount of time. It will ask you
# how much time you have to work in hours and minutes (no seconds because BASEDWATM8).
# Requires timedpomodoro.py and Pomodoro.py
# TODO: Make it so that pressing [RETURN] ends the session

import sys
sys.dont_write_bytecode = True

from Pomodoro import *
from timedpomodoro import *
from global_timer import *

def main():
    hourString = input("How many hours can you work this session? ")
    minutesString = input("How many minutes in addition to that? ")
    hours = int(hourString)
    minutes = int(minutesString)
    session = Pomodoro()
    seconds = (hours * 3600) + (minutes * 60)
    globaltimer = GlobalTimer()
    globaltimer.set_timer(seconds)
    # totalTime is in minutes
    totalTime = (hours * 60) + minutes
    pomodoroInMinutes = session.get_pomodoro() / 60
    if (totalTime < pomodoroInMinutes):
        totalTime = pomodoroInMinutes
    session.set_goal(totalTime)
    execute_pomodoro(session, globaltimer)

if __name__ == "__main__":
    main()
