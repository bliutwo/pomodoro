# Standard, manual pomodoro script.

class Pomodoro (object):
    # default values for Pomodoro class
    def __init__(self):
        self.count = 0
        self.pomodoro = 15 # TODO Default is 27.5
        self.goal = 8*60
        self.sofar = 0
        self.percentage = 0.0
        self.breaktime = 3 # TODO: Default is 3
        self.longbreak = 9 # TODO: Default is 12
        self.dividend = 4   # TODO: Default is 4
        self.remainingPomo = self.set_remaining_pomo(self.goal)
    # adds one pomodoro's worth of time to current session
    def add(self):
        self.count = self.count + 1
        self.sofar = self.pomodoro * self.count
        self.remainingPomo = self.remainingPomo - 1
        # self.percentage = 1.0 * self.sofar / self.goal * 100.0
        self.percentage = 1.0 * self.count / (self.remainingPomo + self.count) * 100.0
    # prints progress so far
    def printProgress(self):
        print("Number of pomodori: %d" % self.count)
        print("So far: %f hours" % (self.sofar / 60.0))
        print("Percentage: %f%%" % self.percentage)
        print("Pomodori left: %d" % self.remainingPomo)
        print("")
    # returns breaktime in seconds
    def get_breaktime(self):
        return (self.breaktime * 60)
    # returns longbreak in seconds
    def get_longbreak(self):
        return (self.longbreak * 60)
    # returns pomodoro amount in seconds
    def get_pomodoro(self):
        return (self.pomodoro * 60)
    # set the goal in minutes, takes customGoal in minutes
    def set_goal(self, customGoal):
        self.goal = customGoal
        self.remainingPomo = self.set_remaining_pomo(customGoal)
    # returns remainingPomo, takes customGoal in minutes
    def set_remaining_pomo(self, customGoal):
        divisor = ((self.pomodoro + self.breaktime) * self.dividend) - self.breaktime
        num_longbreaks = customGoal / divisor
        time_left = customGoal - (num_longbreaks * self.longbreak)
        if ((time_left % (self.pomodoro + self.breaktime)) == 0):
            return (time_left / (self.pomodoro + self.breaktime))
        else:
            return ((time_left / (self.pomodoro + self.breaktime)) + 1)
    def get_remaining_pomo(self):
        return self.remainingPomo
    # checks if session has finished
    def done(self):
        return self.sofar >= self.goal
    # gets pomodoro so far
    def get_number_pomo(self):
        return self.count

def main():  
    session = Pomodoro()
    session.printProgress()
    userInput = raw_input("Press [RETURN] to increase count by 1 (0 to exit): ")

    while userInput != "0":
        print("")
        if userInput != "":
            print("Invalid input.")
            userInput = raw_input("Press [RETURN] to increase "
                                  "count by 1 (0 to exit): ")
        else:
            session.add()
            session.printProgress()
            if session.done(): break
            userInput = raw_input("Press [RETURN] to increase "
                                  "count by 1 (0 to exit): ")

    if userInput == "0":
        print("Exiting.")
    else:
        print("DONE!")

if __name__ == "__main__":
    main()
