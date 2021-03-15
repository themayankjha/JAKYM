from pydub import AudioSegment
from pydub.playback import play

def playmusic(name):
    sound = AudioSegment.from_file(name)
    play(sound)
