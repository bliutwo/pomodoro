import subprocess
audio_file = "../exclamation.mp3"
a = "../abadis.mp3"

def main():
    print "Memes"
#    return_code = subprocess.call(["afplay", audio_file])
    return_code = subprocess.call(["afplay", a])

if __name__ == "__main__":
    main()
