# Just Another Konsole YouTube-Music

## Overview

I wanted to create this application so that I could use the command line to play music easily. I often play games and listen to music simultaneously but using either Spotify or playing music in a browser takes much-needed resources from my CPU and RAM.

I have spent a lot of time looking through numerous CLI based music players. But they either required setting up lots of things, needed premium features to function or sometimes flat out didn't work even after tinkering with them for hours. Hence I thought that instead of looking for a solution, I should code it myself.

So I present to you JAKYM, Just Another Konsole YouTube-Music.

## How It Works

- The program starts and runs two threads, one to input music into the playlist and the other to iterate over the playlist and download the corresponding music and play it.
- The youtube-dl library does most of the heavy lifting of both parsing links and downloading them into a suitable file format.
- The pydub and simpleaudio libraries provide cross-platform audio playback without any issues though setting up simpleaudio on windows takes a different approach.
- The program runs until user specifically types exit.

## Instalation and usage

### Installing ffmpeg

ffmpeg is required for this program to work correctly. Install ffmpeg by following these steps :-

On Linux - <https://www.tecmint.com/install-ffmpeg-in-linux/>
On Windows - <https://www.wikihow.com/Install-FFmpeg-on-Windows>

### Installing simpleaudio

simpleaudio is an optional pydub dependency, it works fine on linux without installing but may give major issues on windows.

### On Linux

- Install Dependencies by ```sudo apt-get install -y python3-dev libasound2-dev```
- Install with: ```pip install simpleaudio```

#### On Windows

- Download the .whl file of simpleaudio from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#simpleaudio)
- Once downloaded, it can be installed using the following command : ```pip install package_name.whl```

### Installing jakym

- Install by using pypi :-``` pip install jakym ```

- Run using jakym command ``` jakym ``` or call it as a python module ```python -m jakym```

Violla jakym is now installed!

Type the song name or copy/paste the YouTube link.

Enjoy jakym

![Screenshot](img/screenshot.png?raw=true "screenshot")

---

## Copyright

Copyright (c) 2021 [Mayank Jha](https://github.com/themayankjha)

License - [GNU GPL v3](License)
