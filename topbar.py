import sys
sys.dont_write_bytecode = True

import interact
import time

def main():
    hours = 3
    mins = 16
    length = 20
    pomodoro = interact.InteractivePomodoro(hours, mins, length)
    while not pomodoro.done():
        p_percent, g_percent = pomodoro.percentages()
        num_pomo, gh, gm, gs, pm, ps = pomodoro.output_remaining_time_strings()
        status = str(g_percent) + "% " + pm + ":" + ps + " " + str(num_pomo)
        if pomodoro.break_status() == True:
            status = "BREAK! " + status
        print(status) 
        pomodoro.decrement()
        time.sleep(1)

if __name__ == "__main__":
    main()
