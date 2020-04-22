import sys
sys.dont_write_bytecode = True

import interact
import time
import pygame_sound
import threading

def play_sound(filename):
    pygame_sound.playSound(filename)

def main():
    start_work_sound = "./exclamation.mp3"
    start_break_sound = "./harp.mp3"
    finished_sound = "./abadis.mp3"
    hours = 3
    mins = 16
    length = 20
    pomodoro = interact.InteractivePomodoro(hours, mins, length)
    threads = []
    while not pomodoro.done():
        p_percent, g_percent = pomodoro.percentages()
        num_pomo, gh, gm, gs, pm, ps = pomodoro.output_remaining_time_strings()
        status = str(g_percent) + "% " + pm + ":" + ps + " " + str(num_pomo)
        if pomodoro.break_status() == True:
            status = "BREAK! " + status
        if pomodoro.one_second_remaining():
            if pomodoro.break_status() == True:
                t = threading.Thread(target=play_sound, args=(start_work_sound,))
                threads.append(t)
                t.start()
            else:
                t = threading.Thread(target=play_sound, args=(start_break_sound,))
                threads.append(t)
                t.start()
        print(status) 
        pomodoro.decrement()
        time.sleep(1)
    print("DONE!")
    play_sound(finished_sound)

if __name__ == "__main__":
    main()
