import jakym.downloader as downloader
import jakym.player as player

import random ,tempfile
from termcolor import colored

class Playlist:

    def __init__(self):
        self.queuedplaylist=[]
        self.playedplaylist=[]

    def returnsong(self):
        song=self.queuedplaylist.pop(0)
        self.playedplaylist.append(song)
        return song

    def addsong(self,query):
        self.queuedplaylist.append(query+" song")

    def downloadsong(self,song,dir):
        meta=downloader.download(song,dir)
        return meta
    
    def shuffleplaylist(self):
            random.shuffle(self.queuedplaylist)
            print("Queue Shuffled")

    def playsong(self,meta,dir):
        print(colored("Currently Playing : " + meta['title'],'yellow'))
        player.playmusic(dir.name+'/'+meta['id'])
    
    def returnplaylist(self):
        allplaylist=self.playedplaylist+self.queuedplaylist
        return allplaylist

def makedownload():
    dir = tempfile.TemporaryDirectory()
    return dir

def removedownload(dir):
    try:
        dir.cleanup()
    except:
        pass