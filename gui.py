import sys
sys.dont_write_bytecode = True
# from Pomodoro import *
# from timedpomodoro import *
# from global_timer import *

# import the (appJar) library
from appJar import gui

def main():
    # handle button events
    def press(button):
        if button == "Cancel":
            app.stop()
        else:
            hours = app.getEntry("Hours to work:")
            minutes = app.getEntry("Minutes to work:")
            pomodoro = app.getEntry("Length of pomodoro:")
            print("hours:", hours, "minutes:", minutes, "pomodoro", pomodoro)

    # create a GUI variable called app
    # app = gui()

    # specify name and size for GUI
    app = gui("Pomodoro Timer", "400x200")

    # change general appearance of GUI
    # app.setBg("orange")
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

    # start the GUI (don't put any code after this line)
    app.go()

if __name__ == "__main__":
    main()
