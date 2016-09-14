# Filename: custom_pomodoro.py
# Description: Theoretical final pomodoro file, for when you have a limited time
# to work, or you only plan to work a certain amount of time. It will ask you
# how much time you have to work in hours and minutes (no seconds because BASEDWATM8).
# Requires timedpomodoro.py and Pomodoro.py

import sys
sys.dont_write_bytecode = True

from Pomodoro import *
from timedpomodoro import *

def main():
    # wat do here
    hourString = raw_input("How many hours can you work? ")
    minutesString = raw_input("How many minutes in addition to that? ")
    hours = int(hourString)
    minutes = int(minutesString)
    session = Pomodoro()
    # totalTime is in minutes
    totalTime = (hours * 60) + minutes
    pomodoroInMinutes = session.get_pomodoro() / 60
    if (totalTime < pomodoroInMinutes):
        totalTime = pomodoroInMinutes
    session.set_goal(totalTime)
    execute_pomodoro(session)

if __name__ == "__main__":
    main()