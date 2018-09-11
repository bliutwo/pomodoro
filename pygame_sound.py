import pygame

def playSound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def main():
    playSound("./exclamation.mp3")
#    playSound("./abadis.mp3")


if __name__ == "__main__":
    main()
