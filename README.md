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

Seems like I've gotten all the "input" I need already just by
modifying the original `gui.py` file. Now, let's see what I can do with
output widgets. Maybe I can output what I was outputting before, anyway?

- [x] Check out [output widgets](http://appjar.info/outputWidgets/).

So in order to display my timer, I want to find out what the right output widget
actually is. I'm going to research a few possibilities, and write down a few that
I find might be relevant:

- [x] Research different output widgets.
  - Is there a "timer" or "clock" output widget?
  - **Label**: Maybe I can have an algorithm (lol, should I even call it this) that
    updates the label every second?
  - **Message**: This seems just like what I already have, but it doesn't seem appropriate
    because 1) it seems to be a place that stores a *lot* of text, and I *don't*
    want to store a *lot* of text; 2) I want a small amount of text. I guess
    these two go hand in hand.
  - **Meter**: I definitely want this. I put a TODO checkbox for this.
  - **Separator**: Separates widgets, but I'm not sure I'll have multiple widgets,
    and it also looks as if *Label* already does that somewhat.
  - **Grip**: "Clickable icon to drag the window around." I think I want this.
    Adding a TODO.
  - **Canvas**: Looks cool, but I don't want to draw anything for this one.
    Maybe I'll use this in the future?
  - **Turtle**: A turtle widget.
    Apparently, [turtle graphics](https://docs.python.org/3.6/library/turtle.html)
    are a popular way for introducing programming to kids. Maybe I'll check that out
    later if I want to make educational material.
  - **Microbit**: [Microbit emulator.](http://appjar.info/outputWidgets/#microbit-emulator).
    Here's [Microbit's main page](https://microbit.org/). Seems cool. I don't really
    know much about it. Apparently it's educational.
  - [**Google Maps**](http://appjar.info/outputWidgets/#googlemaps): Honestly,
    this seems really cool, and I'd want to make some GUI app that uses this.
  - **PieChart**: "Widget to depict a Pie Chart."
  - [**MatPlotLib**](http://appjar.info/outputWidgets/#matplotlib): Honestly,
    (lol, I write "honestly" a lot) I could use this to make a GUI app to replace my
    [django-glicko2](https://github.com/bliutwo/django-glicko2) website.

Sounds like my main output widgets are:

- Label
- Meter
- Grip

We'll work on these one at a time, and I already have TODOs made for the latter
two.

I'll have to see if I can somehow "reset" the application display before I display
a Label output widget.

- [ ] Find out if you can:
  - [ ] "reset" the application display
  - [ ] repopulate with a single Label (and later, Meter and Grip)

Let's see if I can update a Label continuously over time (and subsequently,
the meter).

- [ ] Try to update a Label continuously over time.

Also, ideally, I'd be able to resize the app to take up minimal space.

- [ ] See if can resize the app via code.
- [ ] See if can resize the app via normal user window resizing.

I'll eventually also need sound for my alarms so I'll check out
[sound](http://appjar.info/pythonSound/) for that.

- [ ] Check out [sound](http://appjar.info/pythonSound/).

I also want to see if [Toolbars, Menubars, and Statusbars](http://appjar.info/pythonBars/)
would be applicable for my app--that is, I want to be able to see at all times
what the status of my Pomodoro is.

- [ ] Check out and see if applicable: [Toolbars, Menubars, and Statusbars](http://appjar.info/pythonBars/)

I want to have a progress bar that displays actual overall progress (unlike
my jank setup that doesn't work in the script).

- [ ] Add a progress bar ([meter](http://appjar.info/outputWidgets/#meter)) that is properly calculated.

I want a grip that allows me to move this thing around wherever I want.

- [ ] Add a [grip output widget](http://appjar.info/outputWidgets/#grip).

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
