class GlobalTimer (object):
    # default values for GlobalTimer class
    def __init__(self):
        # time remaining in seconds
        self.remaining = 0
    # decrements timer by one second
    def decrement(self):
        self.remaining = self.remaining - 1
    # takes a value for time in seconds
    def set_timer(self, seconds):
        self.remaining = seconds
    # prints time left
    def status(self):
        h = self.remaining / 3600
        m = self.remaining / 60
        s = self.remaining % 60
        print "\nGlobal timer: %d hours, %d minutes, and %d seconds remaining." % (h, m, s)
    # returns True if the global timer has been exhausted
    def done(self):
        if (self.remaining == 0): print "\a"
        return (self.remaining == 0)