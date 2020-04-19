# Designed for when you have 8+ hours straight to work.
# TODO: Make this play the mp3 file included in the folder.
# http://stackoverflow.com/questions/307305/play-a-sound-with-python

import sys
from pygame_sound import * # TODO: include this when on Linux computer
sys.dont_write_bytecode = True

from Pomodoro import *
import time

def clear_screen():
    for i in range(0, 100):
        print("")

# TODO: comment or uncomment print \a vs playSound
# takes amount in seconds, session is a Pomodoro instance
def time_remaining(amount, session, globaltimer):
    orig_amount = amount
    while amount != 0:
        clear_screen()
        session.printProgress()
        if (orig_amount == session.get_breaktime() or orig_amount == session.get_longbreak()):
            for i in range(0,10):
                print("ON BREAK ON BREAK ON BREAK ON BREAK ON BREAK ON BREAK")
            print("\nBreak timer: %d minutes and %d seconds remaining. ON BREAK!!!" % ((amount / 60), (amount % 60)))
        else:
            print("\nPomodoro timer: %d minutes and %d seconds remaining." % ((amount / 60), (amount % 60)))
        amount = amount - 1
        if (globaltimer != None):
            if globaltimer.done():
                break
            globaltimer.status()
            globaltimer.decrement()
        time.sleep(1)

def execute_pomodoro(session, globaltimer):
    while session.done() == False:
        time_remaining(session.get_pomodoro(), session, globaltimer)
        if (globaltimer != None):
            if globaltimer.done():
                globaltimer.status()
                break
        playSound("./harp.mp3")
        #print "\a"
        session.add()
        if session.done():
            session.printProgress()
            break
        if ((session.get_number_pomo() % session.dividend) == 0):
            time_remaining(session.get_longbreak(), session, globaltimer)
        else:
            time_remaining(session.get_breaktime(), session, globaltimer)
        if (globaltimer != None):
            if globaltimer.done():
                globaltimer.status()
                break
        playSound("./exclamation.mp3")
        #print "\a"
        session.printProgress()

    playSound("./exclamation.mp3")
    #print "\a"
    print("\nExiting.")
    print("DONE! ctrl + c to exit")
    playSound("./abadis.mp3")

def main():
    # 27 minutes and 30 seconds = 1650 seconds
    session = Pomodoro()
    session.printProgress()

    execute_pomodoro(session, None)

if __name__ == "__main__":
    main()
