import subprocess
audio_file = "../exclamation.mp3"

def main():
    print "Memes"
    return_code = subprocess.call(["afplay", audio_file])


if __name__ == "__main__":
    main()
