import sys

sys.dont_write_bytecode = True
PYTHONDONTWRITEBYTECODE = 1

import vlc

p = vlc.MediaPlayer("./exclamation.mp3")
p.play()
p.play()
