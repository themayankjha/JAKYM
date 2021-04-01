# Just Another Konsole YouTube-Music

[![Downloads](https://static.pepy.tech/personalized-badge/jakym?period=total&units=international_system&left_color=blue&right_color=lightgrey&left_text=Total+Installs)](https://pepy.tech/project/jakym)

## Overview

I wanted to create this application so that I could use the command line to play music easily. I often play games and listen to music simultaneously but using either Spotify or playing music in a browser takes much-needed resources from my CPU and RAM.

I have spent a lot of time looking through numerous CLI based music players. But they either required setting up lots of things, needed premium features to function or sometimes flat out didn't work even after tinkering with them for hours. Hence I thought that instead of looking for a solution, I should code it myself.

So I present to you JAKYM, Just Another Konsole YouTube-Music.

![Screenshot](img/screenshot.gif?raw=true "screenshot")

## Usage

- Run the program using jakym command ``` jakym ``` or call it as a python module ```python -m jakym```
- This will open up the jakym command window.
- Type '''spotify'' to play music using spotify playlist or enter a songname to search for song or enter its youtube link.
- jekym will queue all the songs once you type them and play them one by one

## Installation

### Installing ffmpeg

ffmpeg is required for this program to work correctly. Install ffmpeg by following these steps :-

- On Linux - <https://www.tecmint.com/install-ffmpeg-in-linux/>
- On Windows - <https://www.wikihow.com/Install-FFmpeg-on-Windows>

### Installing simpleaudio (Optional on Linux)

simpleaudio is an optional pydub dependency, it works fine on linux without installing but gives major issues on windows.

#### On Linux

- Install Dependencies by ```sudo apt-get install -y python3-dev libasound2-dev```
- Install with: ```pip install simpleaudio```

#### On Windows

- Download the .whl file of simpleaudio from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#simpleaudio)
- Once downloaded, it can be installed using the following command : ```pip install package_name.whl```

### Installing jakym

- Install by using pypi :-``` pip install jakym ```

- Run using jakym command ``` jakym ``` or call it as a python module ```python -m jakym```

Violla jakym is now installed!

Enjoy jakym

## How It Works

- The program starts and runs two threads, one to input music into the playlist and the other to iterate over the playlist and download the corresponding music and play it.
- The youtube-dl library does most of the heavy lifting of both parsing links and downloading them into a suitable file format.
- The pydub and simpleaudio libraries provide cross-platform audio playback without any issues though setting up simpleaudio on windows takes a different approach.
- The program runs until user specifically types exit.

## Version history

| Version     | Improvements    |
| ----------- | -----------     |
| 0.2         | Added Spotify playlist support, Bug fixes |
| 0.1.1       | Improved documentation, Command line integration |
| 0.1         | Initial release |

---

## Copyright

Copyright (c) 2021 [Mayank Jha](https://github.com/themayankjha)

License - [GNU GPL v3](License)
