#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

import sys
sys.dont_write_bytecode = True

# Enable imports from super-directory
sys.path.append('/Users/bliutwo/Dropbox/pomodoro')

f = open("/Users/bliutwo/Dropbox/pomodoro/status.txt", "r")
print(f.read())
