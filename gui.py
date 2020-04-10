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
            usr = app.getEntry("Username")
            pwd = app.getEntry("Password")
            print("User:", usr, "Pass:", pwd)

    # create a GUI variable called app
    # app = gui()

    # specify name and size for GUI
    app = gui("Login Window", "400x200")

    # change general appearance of GUI
    # app.setBg("orange")
    app.setFont(18)

    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "Welcome to appJar")
    app.setLabelBg("title", "red")
    # start the GUI (don't put any code after this line)

    # input widget (EntryBox) for the user to type in
    app.addLabelEntry("Username")
    app.addLabelSecretEntry("Password")

    # specify where you want the cursor to be when the GUI starts
    app.setFocus("Username")



    # link the buttons to the function called press
    app.addButtons(["Submit", "Cancel"], press)

    app.go()

if __name__ == "__main__":
    main()
