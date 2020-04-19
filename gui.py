import sys
sys.dont_write_bytecode = True
# from Pomodoro import *
# from timedpomodoro import *
# from global_timer import *
import interact
import time

# import the (appJar) library
from appJar import gui


def main():
    # handle button events
    def press(button):
        if button == "Cancel":
            app.stop()
        elif button == "Start":
            hours = app.getEntry("Hours to work:")
            minutes = app.getEntry("Minutes to work:")
            custom_pomo = app.getEntry("Length of pomodoro:")
            print("hours:", hours, "minutes:", minutes, "custom_pomo", custom_pomo)
            pomodoro = interact.InteractivePomodoro(hours, minutes, custom_pomo)
            app.hideSubWindow("main")
            # execute_pomodoro(session, globaltimer)
            app.startSubWindow("timer", modal = False)
            global_time = "%s:%s:%s" % pomodoro.output_remaining_time_strings()
            app.addLabel("global_time", global_time)
            app.addGrip(0,1)
            app.showSubWindow("timer")
            app.stopSubWindow()
            def decrement_timer():
                app.clearLabel("global_time")
                pomodoro.decrement_time_remaining()
                global_time = "%s:%s:%s" % pomodoro.output_remaining_time_strings()
                app.setLabel("global_time", global_time)
                app.showSubWindow("timer")
            app.registerEvent(decrement_timer)


    # create a GUI variable called app
    app = gui()

    # specify name and size for GUI
    # app = gui("Pomodoro Timer", "400x200")

    # change general appearance of GUI
    # app.setBg("orange")
    app.startSubWindow("main", "Welcome to Pomodoro Timer")
    app.setFont(18)

    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "Welcome to Pomodoro Timer")
    app.setLabelBg("title", "red")

    # input widget (EntryBox) for the user to type in
    app.addLabelNumericEntry("Hours to work:")
    app.addLabelNumericEntry("Minutes to work:")
    app.addLabelNumericEntry("Length of pomodoro:")

    # specify where you want the cursor to be when the GUI starts
    app.setFocus("Hours to work:")

    # link the buttons to the function called press
    app.addButtons(["Start", "Cancel"], press)
    app.stopSubWindow()

    # start the GUI (don't put any code after this line)
    app.go(startWindow="main")

if __name__ == "__main__":
    main()
