# Pomodoro Looping Timer

## TODO

### Latest / Current / Unfinished TODO(s) in order of decreasing priority

That is, high priority items appear first.

- [ ] Use Overcooked sounds as default. More details later.

- [ ] Add an *option* for the break like "Do you want to have a small 'break' to start, in order to 'ease' into the work session? (y/N)" using [`RadioButton`s](http://appjar.info/inputWidgets/#radiobutton).
  - [ ] Do this also for `topbar.py`.

- [ ] Write instructions for using this app.

[PyInstaller](https://www.pyinstaller.org/) (bundling the appJar Python GUI program as a Windows executable) doesn't work yet because of some stuff I need to add (such as [favicon.ico](https://stackoverflow.com/questions/18537918/why-isnt-ico-file-defined-when-setting-windows-icon)).

- [ ] Fix the above-described bug when bundling Python script as a Windows executable.
- [ ] Release cross-platform applcation bundle.

- [ ] Implement "if close timer window, close entire application."

There's another nuance: pressing "cancel" closes the application (currently), but
the terminal hang occurs *even on the main window.* How do I grab the event of "pressing the X to close" button?

- [ ] Grab the event of "pressing the X to close" button.

- [ ] Consider [widget layout](http://appjar.info/pythonWidgetLayout/).

Also, ideally, I'd be able to resize the app to take up minimal space.

- [ ] See if can resize the app via code.

According to [this answer](https://stackoverflow.com/questions/2933/how-can-i-create-a-directly-executable-cross-platform-gui-app-using-python),
there are other Python GUI libraries that might be better suited for this, but it honestly this works. Maybe someday.

- [ ] Research [other Python GUI libraries that might be better suited for this](https://stackoverflow.com/questions/2933/how-can-i-create-a-directly-executable-cross-platform-gui-app-using-python).

### History / Finished TODOs

The two sections below are mutually exclusive.

#### Reverse Chronological Order

Started doing this 4/22/20, 14:53.

- [x] Add a break at the beginning of the session in order to "ease" into the work session.

#### True Chronological Order

The beginning of 2020 completed TODOs starts here.

- [x] Figure out how to import appJar onto my PC.
  - [x] Run the following command:

```bash
$ pip3 install appjar
```

Now that I've got appJar installed, I should try creating a basic GUI app.

- [x] Create a basic GUI app.
- [x] Mold this basic GUI app into what I need for Pomodoro.
- [x] Find out how to control the logic of the buttons
- [x] Find out how to have changing display over time

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

- [x] Try to update a Label continuously over time.

#### Pomodoro Interactive Wrapper

In this section, I'll cover how I implement the interface between the GUI and
the Pomodoro, globaltimer, etc. classes.

##### The Actual Pomodoro Timer

According to the other scripts I've written, `custom_pomodoro.py` and `timedpomodoro.py`,
I'm actually creating a timer on top of the existing `Pomodoro()` class. I'll probably
need to do the same thing in `interact.py`.

I need to implement logic for breaks and longbreaks in `interact.py`.

- [x] Implement logic for breaks and longbreaks in `interact.py`.

It looks like integrating my existing Python classes won't be as simple as I
initially thought. I have a bunch of classes that don't directly allow me to
display and return a "timer," per se. I'll need to write a class file that
does exactly what I just described.

- [x] Write a Python class file that directly interacts with my Pomodoro.
  - Ideally, all it does is allow me to do the following things:
    - Input initial time required.
    - Output time remaining (for current pomodoro / break and global).
    - Allow me to decrement the time remaining (for each second that passes).

There are two aspects to this:

- "session" timer
- "global" timer

In the first one, we need to find out if we are on a break or Pomodoro work session.
In the second, we need to find out the total time remaining.

The second one seems to be taken care of mostly by `global_timer.py`.

The first one seems like it might be tricky, but we implemented what that would look like in `custom_pomodoro.py`.
Let's see how it's implemented there.

So according to `custom_pomodoro.py`, we'll want to make a `session = Pomodoro()` and `session.set_goal()` and `session.set_pomo()`.
(The `session.set_pomo()` may be optional, but we'll see if we need it when we define each one.)
At the same time, we'll want to make a `globaltimer = GlobalTimer()` and then `globaltimer.set_timer(seconds)`.

- `session.set_goal()`: "set the goal in minutes, takes customGoal in minutes." ~~This is specifically to do with the "number of Pomodoro" remaining, but we can cover more details later~~ This might mean that we can set how long we want our session to be? It seems not exactly right, so I'll do more research later.
- `session.set_pomo()`: "set the length of a pomodoro in minutes, takes customPomo in minutes." This means that we can give it the number of minutes we want each Pomodoro to be.
- `session.get_pomodoro()`: "returns pomodoro amount in seconds." Is this used to return whether we're on a break or long break? Yes. ~~If `session.get_pomodoro() % 4 == 0`, then we get a long break. Else, it's a regular break.~~ But not in that way.

We also want to check `timedpomodoro.py` because that has the `execute_pomodoro` function, which takes in a `session = Pomodoro()` and a `globaltimer = GlobalTimer()` as parameters.

An important distinction is that `Pomodoro()` itself only keeps track of a few things

- Pomodori so far
- Whether we're on break
- ~~How much time remains in a single pomodoro~~

Importantly, it doesn't keep track of how much time is left in a single pomodoro.

Let's try to output the global timer first.

- [x] Output global timer values and display it on the GUI.

Next, we need to decrement the timer label over time.

- [x] Decrement timer label over time.

The problem is that I can change it, but it doesn't show up until the end of the session.

I finally found from [this StackOverflow answer](https://stackoverflow.com/questions/47821806/creating-loops-to-update-a-label-in-app-jar)
that I need to think about appJar's [Loops and Sleeps](http://appjar.info/pythonLoopsAndSleeps/).

- [x] Check out appJar's [Loops and Sleeps](http://appjar.info/pythonLoopsAndSleeps/).

So I'm able to update the Label continuously over time, but two new problems have arisen:

- The updates don't actually correspond to one second.
- It's impossible to stop the timer (even with red X or ctrl+C on the keyboard in the terminal) unless I stop the "Python" task in task manager.

- [x] Get the updates to correspond to one second. (`app.setPollTime(1000)`)
- [x] Fix the unstoppable timer issue mentioned above. *~~Apparently fixing the above TODO also fixed this TODO. Ctrl + C works now~~.* **The actual fix was taking out the unnecessary `showSubWindow`s**.

Actually, the unstoppable timer issue isn't as important. What I really need to do now is to display the Pomodoro timer on top of the global timer, as well as a background corresponding to what the session is (pomodoro, break).

- [x] Display the Pomodoro timer ~~on top of~~ ~~next to the~~ on top of the global timer.

- [x] Display background corresponding to what the session is (pomodoro, break). Maybe red for pomodoro, green for break?

#### History (continued)

So I've implemented the main logic of `interact.py`. Now I need to play sounds to start breaks, pomodori, and when the global timer ends.

- [x] Play sounds to start breaks, pomodori, and when the global timer ends.
  - [x] global timer end
  - [x] pomodori end
  - [x] break end

> [Sound](http://appjar.info/pythonSound/) is only supported in Windows, using the Winsound API. Therefore, only .WAV files will work.

Well, that fucking blows.

- [x] Implement `.bell()`, ~~`.soundError()`~~, and ~~`soundWarning()`~~ for [if not on Windows](https://stackoverflow.com/questions/1325581/how-do-i-check-if-im-running-on-windows-in-python). The latter two don't work on non-Windows, and even on Windows they don't "work."

One issue right now is that once I start the timer, if I press "close" on that
window, it doesn't close the application (i.e. terminal hangs).

- [x] See if can resize the app via normal user window resizing. **Probably via [Paned Frames](http://appjar.info/pythonWidgetGrouping/#paned-frame)**.

I'll eventually also need sound for my alarms so I'll check out
[sound](http://appjar.info/pythonSound/) for that.

- [x] Check out [sound](http://appjar.info/pythonSound/).

I also want to see if [Toolbars, Menubars, and Statusbars](http://appjar.info/pythonBars/)
would be applicable for my app--that is, I want to be able to see at all times
what the status of my Pomodoro is.

- [x] Check out and see if applicable: [Toolbars, Menubars, and Statusbars](http://appjar.info/pythonBars/) *The most applicable one would be statusbar, but I already have a DualMeter for that.*

I want to have a progress bar that displays actual overall progress (unlike
my jank setup that doesn't work in the script).

- [x] Add a progress bar ([meter](http://appjar.info/outputWidgets/#meter)) that is properly calculated.

Moreover, for this progress bar, I want it to be able to show a color depending on what I'm doing.
For example, red for breaktime, green for worktime.

- [x] Find out if you can change the color of the progress bar (given that you can update it continuously over time, like the Label). `app.setMeterFill("progress", "blue")`

I want a grip that allows me to move this thing around wherever I want.

- [x] Add a [grip output widget](http://appjar.info/outputWidgets/#grip).

- [x] Keep timer on top using [`.setOnTop(stay=True)`](http://appjar.info/pythonGuiOptions/). *Problem: it doesn't work properly. It'll only stay on top per update, and if I want to stay focused on a different application, it won't stay on top.*

For the purpose of exporting the program as an executable binary, I might want
to use [PyInstaller](https://www.pyinstaller.org/) on top of this appJar business.

- [x] Try using [PyInstaller](https://www.pyinstaller.org/) to bundle the appJar Python GUI program as a Windows executable.

There's a bug in that the window constantly takes focus. We might be able to fix that by doing the following:

- [x] See if you can't eliminate extra `app.showSubWindow("Pomodoro")` lines. This should only be needed *once*.

#### BitBar stint

- [x] In `topbar.py`, play sounds.
- [x] Add multithreading action!
- [x] Use [BitBar](https://github.com/matryer/bitbar#plugin-api) (already installed) to display the script on top bar on Mac.

It displays at the top, but the main problem is that it expects a one-line output. All I need to do is update a file over time, and it'll work.

- [x] Make a Python script that updates a file over time, then make another that *only* reads and prints the line from the file.

### Competing Pomodoro apps

- [PowerPom - Pomodoro Timer](https://www.microsoft.com/en-us/p/powerpom-pomodoro-timer/9p5zscl5qc8w?activetab=pivot:overviewtab): In this one, I don't see an option to make it a tiny part of the screen. Moreover, it has ads. Yuck.
- [Focus Booster App](https://www.focusboosterapp.com/download): 30-day trial. Also yuck.
- [Top 10 Free and Open Source Pomodoro Apps](https://medevel.com/top-10-free-and-open-source-pomodoro-apps-for-windows-macos-and-linux/): The problem is that these don't do *exactly* what I want it to do, and the windows themselves (in the case of having any of them always-on-top) seem too big.

# 2020 Updates

(4/21/2020, 20:43) It works! Top bar application works, but I need to write instructions and installation.

(4/20/2020, 20:53) There may be hope yet for that problem below! Check [latest TODO](#latest--current-todos).

(4/20/2020, 00:43) This doesn't quite work on Mac. The window keeps going to the front, but more importantly, steals focus from other apps.

(4/19/2020, 17:08) I've finished the main functionality of the GUI app. There are several issues and bugs I plan to fix,
but since I mainly need to study material for job interviews (algorithms and such), I'll postpone the fixing and cross-platform release
to another weekend. For now, I have a working application that is better than my previous iteration.

*BIG caveat*: Sounds only work on Windows. Sucks.

I use [DeskPins](https://efotinis.neocities.org/deskpins/) to keep the window pinned on top.

## Old 2020 update

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
