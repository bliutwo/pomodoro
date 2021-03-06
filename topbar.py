import sys
sys.dont_write_bytecode = True

import interact
import time
import pygame_sound
import threading

def write_status(filename, status):
    f = open(filename, "w")
    f.write(status)
    f.close()

def play_sound(filename):
    pygame_sound.playSound(filename)

def main():
    start_work_sound = "./sounds/start3.mp3"
    start_break_sound = "./sounds/overcooked2_map_theme.mp3"
    finished_sound = "./sounds/7am_animal_crossing.mp3"
    status_filename = "status.txt"

    hourString = input("How many hours can you work this session? ")
    minutesString = input("How many minutes in addition to that? ")
    pomodoroString = input("How long do you want each Pomodoro to be (in minutes)? ")
    customBreaks = input("Do you want to set custom breaktimes [y/n]? ")

    options = ["y", "yes", "n", "no"]

    while customBreaks not in options:
        customBreaks = input("Please input 'y', 'yes', 'n', or 'no'. Do you want to set custom breaktimes? [y/n] ")

    break_bool = -1
    shortBreakString = ""
    longBreakString = ""
    if customBreaks == "y" or customBreaks == "yes":
        break_bool = 1
        shortBreakString = input("How long do you want your SHORT breaks to be (in minutes)? ")
        longBreakString = input("How long do you want your LONG breaks to be (in minutes)? ")
    else:
        break_bool = 0

    hours = int(hourString)
    mins = int(minutesString)
    length = int(pomodoroString)

    pomodoro = interact.InteractivePomodoro(hours, mins, length)

    if break_bool == 1:
        pomodoro.set_custom_breaktimes(shortbreak=int(shortBreakString), longbreak=int(longBreakString))

    play_sound(start_work_sound)
    threads = []
    while not pomodoro.done():
        p_percent, g_percent = pomodoro.percentages()
        num_pomo, gh, gm, gs, pm, ps = pomodoro.output_remaining_time_strings()
        status = str(num_pomo) + "  " + str(g_percent) + "% " + str(p_percent) + "% " + pm + ":" + ps
        if pomodoro.break_status() == True:
            status = "BREAK!  " + status
        else:
            status = "WORK!  " + status
        if pomodoro.one_second_remaining():
            if pomodoro.break_status() == True:
                t = threading.Thread(target=play_sound, args=(start_work_sound,))
                threads.append(t)
                t.start()
            else:
                t = threading.Thread(target=play_sound, args=(start_break_sound,))
                threads.append(t)
                t.start()
        write_status(status_filename, status)
        pomodoro.decrement()
        time.sleep(1)
    status = "DONE!  " + str(num_pomo) + "  " + str(g_percent) + "% " + str(p_percent) + "% " + pm + ":" + ps
    write_status(status_filename, status)
    play_sound(finished_sound)

if __name__ == "__main__":
    main()
