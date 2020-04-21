import sys
sys.dont_write_bytecode = True

import interact

def main():
    hours = 3
    mins = 16
    length = 20
    pomodoro = InteractivePomodoro(hours, mins, length)
    while not pomodoro.done():
        p_percent, g_percent = pomodoro.percentages()
        status = ""

        print(status) 

if __name__ == "__main__":
    main()
