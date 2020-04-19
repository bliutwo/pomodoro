import sys
sys.dont_write_bytecode = True
import interact
import time
import os

# import the (appJar) library
from appJar import gui

def main():
    # handle button events
    def press(button):
        if button == "Cancel":
            app.stop()
        elif button == "Start":
            hours = app.getEntry("How many hours can you work this session?")
            minutes = app.getEntry("How many minutes in addition to that?")
            custom_pomo = app.getEntry("How long do you want each Pomodoro to be (in minutes)?")
            print("hours:", hours, "minutes:", minutes, "custom_pomo", custom_pomo)
            pomodoro = interact.InteractivePomodoro(hours, minutes, custom_pomo)
            app.hideSubWindow("main")
            app.startSubWindow("Pomodoro", modal = False)
            global_time = "%s\n%s:%s:%s\n%s:%s" % pomodoro.output_remaining_time_strings()
            app.addLabel("global_time", global_time)
            app.setLabelBg("global_time", "red")
            app.addGrip(0,1)
            app.showSubWindow("Pomodoro")
            app.stopSubWindow()
            def decrement_timer():
                if pomodoro.done():
                    app.clearLabel("global_time")
                    app.setLabel("global_time", "DONE!!!")
                    app.showSubWindow("Pomodoro")
                    if os.name == 'nt':
                        app.playSound("./abadis.wav", wait=True)
                    else:
                        app.bell()
                    app.stop()
                else:
                    app.clearLabel("global_time")
                    pomodoro.decrement_time_remaining()
                    global_time = "%s\n%s:%s:%s\n%s:%s" % pomodoro.output_remaining_time_strings()
                    color = "red"
                    if pomodoro.one_second_remaining():
                        if pomodoro.break_status():
                            if os.name == 'nt':
                                app.playSound("./exclamation.wav")
                            else:
                                app.bell()
                        else:
                            if os.name == 'nt':
                                app.playSound("./harp.wav")
                            else:
                                app.bell()
                    app.setLabel("global_time", global_time)
                    if pomodoro.break_status():
                        color = "green"
                    else:
                        color = "red"
                    app.setLabelBg("global_time", color)
                    app.showSubWindow("Pomodoro")
            # takes time in milliseconds
            app.setPollTime(10)
            app.registerEvent(decrement_timer)


    # create a GUI variable called app
    app = gui()

    # change general appearance of GUI
    app.startSubWindow("main", "Welcome to Pomodoro Timer")
    app.setFont(18)

    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "Welcome to Pomodoro Timer")
    app.setLabelBg("title", "red")

    # input widget (EntryBox) for the user to type in
    app.addLabelNumericEntry("How many hours can you work this session?")
    app.addLabelNumericEntry("How many minutes in addition to that?")
    app.addLabelNumericEntry("How long do you want each Pomodoro to be (in minutes)?")

    # specify where you want the cursor to be when the GUI starts
    app.setFocus("How many hours can you work this session?")

    # link the buttons to the function called press
    app.addButtons(["Start", "Cancel"], press)
    app.stopSubWindow()

    # start the GUI (don't put any code after this line)
    app.go(startWindow="main")

if __name__ == "__main__":
    main()
