import jakym.downloader as downloader
import jakym.player as player

import random 
from termcolor import colored

class Playlist:

    def __init__(self):
        self.queuedplaylist=[]
        self.playedplaylist=[]
        self.starttime = None
        self.pausetime = None
        self.meta = None
        self.playobj = None 
        self.resumetime = None
        self.songpaused = False
        self.repeat = 0

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
        self.meta=meta
        self.resumetime=0
        print(colored("Currently Playing : " + self.meta['title'],'yellow'))
        self.playobj,self.starttime=player.genmusic(dir.name+'/'+self.meta['id'],0)

    def resumesong(self,dir):
        if self.songpaused==True:
            print(colored("Resuming : " + self.meta['title'],'yellow'))
            self.playobj,self.starttime=player.genmusic(dir.name+'/'+self.meta['id'],self.resumetime)
            self.songpaused=False
        else:
            print("Already Playing")
    
    def pausesong(self):
        if self.songpaused==True:
            print("Already Paused")
        else:
            self.songpaused=True
            self.pausetime=player.pausemusic(self.playobj)
            self.resumetime = self.resumetime+((self.pausetime - self.starttime)*1000)

    def nextsong(self):
        if self.repeat==2:
            self.repeat=0
            self.playobj.stop()
            self.songpaused=False
            player.wait()
            self.repeat=2
        else:
            self.playobj.stop()
            self.songpaused=False

    def shiftlastplayedsong(self):
        self.queuedplaylist=[self.playedplaylist.pop()]+self.queuedplaylist

    def loopqueue(self):
        self.queuedplaylist.extend(self.playedplaylist)
        self.playedplaylist.clear()
    
    def removelastqueuedsong(self):
        try:
            self.queuedplaylist.pop()
        except:
            print("Empty queue")

    def previoussong(self):
        try:
            self.queuedplaylist=[self.playedplaylist.pop()]+self.queuedplaylist
            self.queuedplaylist=[self.playedplaylist.pop()]+self.queuedplaylist
            self.playobj.stop()
            self.songpaused=False
        except:
            print(colored("Error: can't go back beyond start ",'red'))

    def repeatsong(self,mode):
        if mode == "off":
            self.repeat = 0
        elif mode == "all":
            self.repeat = 1
        elif mode == "song":
            self.repeat = 2
        else:
            print(colored("Error: Invalid Mode ",'red'))
    
    def seeksong(self,value,dir):
        if self.songpaused==False:
            self.pausesong()
        self.resumetime=self.resumetime + (value*1000)
        self.resumesong(dir)

    def returnplaylist(self):
        allplaylist=self.playedplaylist+self.queuedplaylist
        return allplaylist

