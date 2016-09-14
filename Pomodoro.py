# Standard, manual pomodoro script.

class Pomodoro (object):
    # default values for Pomodoro class
    def __init__(self):
        self.count = 0
        self.pomodoro = 27.5
        self.goal = 8*60
        self.sofar = 0
        self.percentage = 0.0
        self.breaktime = 3
        self.remainingPomo = self.set_remaining_pomo(self.goal)
    # adds one pomodoro's worth of time to current session
    def add(self):
        self.count = self.count + 1
        self.sofar = self.pomodoro * self.count
        self.percentage = self.sofar / self.goal * 100.0
        self.remainingPomo = self.remainingPomo - 1
    # prints progress so far
    def printProgress(self):
        print "Number of pomodori: %d" % self.count
        print "So far: %f hours" % (self.sofar / 60.0)
        print "Percentage: %f%%" % self.percentage
        print "Pomodori left: %d" % self.remainingPomo
        print ""
    # returns breaktime in seconds
    def get_breaktime(self):
        return (self.breaktime * 60)
    # returns pomodoro amount in seconds
    def get_pomodoro(self):
        return (self.pomodoro * 60)
    # set the goal in minutes, takes customGoal in minutes
    def set_goal(self, customGoal):
        self.goal = customGoal
        self.remainingPomo = self.set_remaining_pomo(customGoal)
    # returns remainingPomo, takes customGoal in minutes
    def set_remaining_pomo(self, customGoal):
        if ((customGoal % self.pomodoro) == 0):
            return (customGoal / self.pomodoro)
        else:
            return ((customGoal / self.pomodoro) + 1)
    # checks if session has finished
    def done(self):
        return self.sofar >= self.goal

def main():  
    session = Pomodoro()
    session.printProgress()
    userInput = raw_input("Press [RETURN] to increase count by 1 (0 to exit): ")

    while userInput != "0":
        print ""
        if userInput != "":
            print "Invalid input."
            userInput = raw_input("Press [RETURN] to increase "
                                  "count by 1 (0 to exit): ")
        else:
            session.add()
            session.printProgress()
            if session.done(): break
            userInput = raw_input("Press [RETURN] to increase "
                                  "count by 1 (0 to exit): ")

    if userInput == "0":
        print "Exiting."
    else:
        print "DONE!"

if __name__ == "__main__":
    main()
