import sys
sys.dont_write_bytecode = True

from Pomodoro import *
import time

def clear_screen():
    for i in range(0, 100):
        print ""

# takes amount in seconds, sesh is a Pomodoro instance
def time_remaining(amount, sesh, globaltimer):
    orig_amount = amount
    while amount != 0:
        clear_screen()
        sesh.printProgress()
        if (orig_amount == sesh.get_breaktime()):
            for i in range(0,10):
                print "ON BREAK ON BREAK ON BREAK ON BREAK ON BREAK ON BREAK"
        print "\n%d minutes and %d seconds remaining." % ((amount / 60), (amount % 60))
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
        if (globaltimer != None) or globaltimer.done():
            globaltimer.status()
            break
        print "\a"
        session.add()
        if session.done():
            session.printProgress()
            break
        time_remaining(session.get_breaktime(), session, globaltimer)
        if (globaltimer != None) or globaltimer.done():
            globaltimer.status()
            break
        print "\a"
        session.printProgress()

    print "\nExiting."
    print "DONE!"


def main():
    # 27 minutes and 30 seconds = 1650 seconds
    sash = Pomodoro()
    sash.printProgress()

    execute_pomodoro(sash, None)

if __name__ == "__main__":
    main()