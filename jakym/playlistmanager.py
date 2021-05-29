import jakym.downloader as downloader
import jakym.player as player
import random , os
from termcolor import colored

class Playlist:

    def __init__(self):
        self.playlist=[]

    def returnsong(self):
        song=self.playlist.pop(0)
        return song

    def addsong(self,query):
        self.playlist.append(query+" song")

    def downloadsong(self,song):
        meta=downloader.download(song)
        return meta
    
    def shuffleplaylist(self):
            random.shuffle(self.playlist)
            print("Queue Shuffled")

    def playsong(self,meta):
        print(colored("Currently Playing : " + meta['title'],'yellow'))
        player.playmusic('downloads/'+meta['id'])

def cleandownload():
    dir ='downloads'
    try:
        for file in os.scandir(dir):
            os.remove(file.path)
    except:
        print("Failed Cleaning")

def makedownload():
    try:
        os.mkdir('downloads')
    except:
        pass
def removedownload():
    try:
        os.rmdir('downloads')
    except:
        pass