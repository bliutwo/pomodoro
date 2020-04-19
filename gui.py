import sys
sys.dont_write_bytecode = True
from Pomodoro import *
# from timedpomodoro import *
# from global_timer import *

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
            pomodoro = app.getEntry("Length of pomodoro:")
            print("hours:", hours, "minutes:", minutes, "pomodoro", pomodoro)
            app.hideSubWindow("main")
            app.showSubWindow("timer")

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

    app.startSubWindow("timer", modal = False)
    app.addLabel("time", "00:00")
    app.addGrip(0,1)
    app.stopSubWindow()

    # start the GUI (don't put any code after this line)
    app.go(startWindow="main")

if __name__ == "__main__":
    main()
