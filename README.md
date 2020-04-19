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

### Latest / Current TODO(s)

It looks like integrating my existing Python classes won't be as simple as I
initially thought. I have a bunch of classes that don't directly allow me to
display and return a "timer," per se. I'll need to write a class file that
does exactly what I just described.

- [ ] Write a Python class file that directly interacts with my Pomodoro.
  - Ideally, all it does is allow me to do the following things:
    - Input initial time required.
    - Output time remaining (for current pomodoro / break and global).
    - Allow me to decrement the time remaining (for each second that passes).

Let's see if I can update a Label continuously over time (and subsequently,
the meter).

- [ ] Try to update a Label continuously over time.

### Pomodoro Interactive Wrapper

So in this section, I'll cover how I implement the interface between the GUI and
the Pomodoro, globaltimer, etc. classes.

### History

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

- [x] Find out if you can:
  - [x] "reset" the application display [**Frames**](http://appjar.info/pythonWidgetGrouping/#frame)
  - [x] repopulate with a single Label (and later, Meter and Grip) **Start and stop Frames.**

Looks like what I need are [Grouping Widgets](http://appjar.info/pythonWidgetGrouping/).

> It's sometimes desirable to group widgets together within a window.
> Or to have multiple *pages* of widgets.

I'll probably want a [Frame Stack](http://appjar.info/pythonWidgetGrouping/#frame-stack) to
~~"reset" the application display~~ stack the timer on top of the the initial GUI.

But don't I want to just reset and resize the display?

[Frames](http://appjar.info/pythonWidgetGrouping/#frame) are what I want. I can
start and stop frames.

So what I want is:

```
refactor everything so far into a frame
on button press "submit":
    stop the current frame
    start a new frame
        new frame is populated with only (sample) timer text
```

- [x] ~~Implement above pseudocode.~~ This is the wrong approach. I need to open and close windows.

One thing I don't understand is how they stop frames before starting and stopping the app.
Maybe I just need to start and stop the app itself?

I might need [Multiple Windows](http://appjar.info/pythonSubWindows/).

- [x] ~~Redefine existing GUI in terms of a window that I can show/hide.~~

I actually want to go to a different page upon starting the timer via [Multiple Pages](http://appjar.info/multiplePages/).

According to [Emptying Containers](http://appjar.info/multiplePages/#emptying-containers):

> It's possible to quickly delete all widgets in a container, and then recreate them:

It might be another thing to just put a frame on top. But then how can I resize the window?

Let's just try to launch a new window upon "Start".

- [x] Go to a new page/window upon "Start".

Maybe I can delete all widgets in the current window, and then display one?

- [x] ~~delete all widgets in the~~ ~~Destroy~~ Hide current window, and then display one.

Let's see if I can update a Label continuously over time (and subsequently,
the meter).

- [ ] Try to update a Label continuously over time.

It looks like integrating my existing Python classes won't be as simple as I
initially thought. I have a bunch of classes that don't directly allow me to
display and return a "timer," per se. I'll need to write a class file that
does exactly what I just described.

- [ ] Write a Python class file that directly interacts with my Pomodoro.
  - Ideally, all it does is allow me to do the following things:
    - Input initial time required.
    - Output time remaining (for current pomodoro / break and global).
    - Allow me to decrement the time remaining (for each second that passes).

One issue right now is that once I start the timer, if I press "close" on that
window, it doesn't close the application (i.e. terminal hangs).

- [ ] Implement "if close timer window, close entire application."

There's another nuance: pressing "cancel" closes the application (currently), but
the terminal hang occurs *even on the main window.* How do I grab the event of "pressing the X to close" button?

- [ ] Grab the event of "pressing the X to close" button.

Also, ideally, I'd be able to resize the app to take up minimal space.

- [ ] See if can resize the app via code.
- [x] See if can resize the app via normal user window resizing. **Probably via [Paned Frames](http://appjar.info/pythonWidgetGrouping/#paned-frame)**.

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

Moreover, for this progress bar, I want it to be able to show a color depending on what I'm doing.
For example, red for breaktime, green for worktime.

- [ ] Find out if you can change the color of the progress bar (given that you can update it continuously over time, like the Label).

I want a grip that allows me to move this thing around wherever I want.

- [ ] Add a [grip output widget](http://appjar.info/outputWidgets/#grip).

According to [this answer](https://stackoverflow.com/questions/2933/how-can-i-create-a-directly-executable-cross-platform-gui-app-using-python),
there are other Python GUI libraries that might be better suited for this.
For the purpose of exporting the program as an executable binary, I might want
to use [PyInstaller](https://www.pyinstaller.org/) on top of this appJar business.

- [x] Try using [PyInstaller](https://www.pyinstaller.org/) to bundle the appJar Python GUI program as a Windows executable.

This doesn't work yet because of some stuff I need to add (such as [favicon.ico](https://stackoverflow.com/questions/18537918/why-isnt-ico-file-defined-when-setting-windows-icon)).

- [ ] Fix the above-described bug when bundling Python script as a Windows executable.

### Competing Pomodoro apps

- [PowerPom - Pomodoro Timer](https://www.microsoft.com/en-us/p/powerpom-pomodoro-timer/9p5zscl5qc8w?activetab=pivot:overviewtab): In this one, I don't see an option to make it a tiny part of the screen. Moreover, it has ads. Yuck.
- [Focus Booster App](https://www.focusboosterapp.com/download): 30-day trial. Also yuck.
- [Top 10 Free and Open Source Pomodoro Apps](https://medevel.com/top-10-free-and-open-source-pomodoro-apps-for-windows-macos-and-linux/): The problem is that these don't do *exactly* what I want it to do, and the one always-on-top option seems too big.

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
