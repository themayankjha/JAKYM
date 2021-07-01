from threading import Timer
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import time
import simpleaudio


def genmusic(name,resumetime):
    sound = AudioSegment.from_file(name)
    sound = sound[resumetime:]
    playback = simpleaudio.WaveObject(
    sound.raw_data, 
    num_channels=sound.channels, 
    bytes_per_sample=sound.sample_width, 
    sample_rate=sound.frame_rate)
    t0 = time.time()
    playobj=playback.play()
    return playobj,t0
    

def pausemusic(playobj):
    t1 =time.time()
    playobj.stop()
    return t1


def wait():
    time.sleep(5)