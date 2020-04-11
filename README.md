# 2020 Update

[The old README can be found here](#pomodoro-python-script).

I've been trying to create a good, cross-platform GUI for this, as can be seen
[here](https://github.com/bliutwo/pomodoro_django) and my research into
[QtCreator](https://doc.qt.io/qtcreator/index.html), and also the [original README](#pomodoro-python-script)
in which I talked about making a good GUI way back in 2015 or so. I figured that Python must
have its own GUI-app type framework, so I found, from the [Python Wiki](https://wiki.python.org/moin/GuiProgramming),
[appJar](http://appjar.info/), which is something like Tkinter (something that
Andy, my old, flakey project partner put into the project specifications of a
[project that I ended up doing on my own](https://github.com/bliutwo/disease-ontology)).

So I'll be making an app using appJar to make this a reality. Hopefully, it will
be a "double click this to run it" app that is easy to use for all kinds of
people, whether they are technologically literate or not.

## TODO

- [x] Figure out how to import appJar onto my PC.
  - [x] Run the following command:

```bash
$ pip3 install appjar
```

Now that I've got appJar installed, I should try creating a basic GUI app.

- [x] Create a basic GUI app.
- [x] Mold this basic GUI app into what I need for Pomodoro.
- [ ] Find out how to control the logic of the buttons
- [ ] Find out how to have changing display over time

Seems like I want to have basic input and output, so I'm going to check out
[input widgets](http://appjar.info/inputWidgets/) followed by
[output widgets](http://appjar.info/outputWidgets/).

- [x] Check out
[input widgets](http://appjar.info/inputWidgets/).

Seems like I've gotten all the "input" I need. Now, let's see what I can do with
output widgets. Maybe I can output what I was outputting before, anyway?

Also, ideally, I'd be able to resize the app to take up minimal space.

- [ ] Check out [output widgets](http://appjar.info/outputWidgets/).

I'll eventually also need sound for my alarms so I'll check out
[sound](http://appjar.info/pythonSound/) for that.

- [ ] Check out [sound](http://appjar.info/pythonSound/).

I also want to see if [Toolbars, Menubars, and Statusbars](http://appjar.info/pythonBars/)
would be applicable for my app--that is, I want to be able to see at all times
what the status of my Pomodoro is.

- [ ] Check out and see if applicable: [Toolbars, Menubars, and Statusbars](http://appjar.info/pythonBars/)

# Pomodoro Python script

Small python scripts designed to help with productivity.

Uses Python 3! As far as I know, it still works with Python 2.

Usage:

```
python3 custom_pomodoro.py
```

**OR**

```
python custom_pomodoro.py
```

## Pygame

Running this requires installation of pygame.

- Here are the [official pygame installation instructions](https://www.pygame.org/wiki/GettingStarted).

Alternatives if that doesn't work:

- [PyGame Installation Mac OS X](https://stackoverflow.com/questions/30743194/pygame-installation-mac-os-x)
- [Installing pygame (Mac) for Python 2](https://stackoverflow.com/questions/20968480/installing-pygame-module-for-python-2-7-5-on-terminal)
- [Old Ask Ubuntu forum on installing Pygame](https://www.pygame.org/wiki/GettingStarted)

[Wikipedia page](https://www.pygame.org/wiki/GettingStarted) about Pomodoro Technique.

TODO:

- [ ] Add a separate thread for playing the sound

- [ ] Make a Windows, Mac, Linux, and Android executable/app
  - [ ] Windows
  - [ ] Mac
  - [ ] Linux
  - [ ] Android

- [ ] Account for breaks and global timer in determining #pomodori & percentage

- [ ] Include functionality for smarter "break" times (e.g. if 3 hours, 6 pomodori, break after 3 instead of 4) <-- probably completely optional/unoptimal
