import downloader
import player
import os , glob
import threading
import pyfiglet

class Playlist:

    def __init__(self):
        self.playlist=[]

    def playlistmanager(self):
        song=self.playlist.pop(0)
        return song

    def songqueuer(self,query):
        self.playlist.append(query+" song")

    def songdownloader(self,song):
        meta=downloader.download(song)
        return meta

    def songplayer(self,meta):
        print("Currently Playing : " + meta['title'])
        player.playmusic('downloads/'+meta['id'])

musicplaylist = Playlist()

def cleandownload():
    dir ='downloads'
    for file in os.scandir(dir):
        os.remove(file.path)

def play():
    while True:
        if musicplaylist.playlist:
            song=musicplaylist.playlistmanager()
            meta=musicplaylist.songdownloader(song)
            musicplaylist.songplayer(meta)
            cleandownload()
        else:
            pass

def queue():
        songrequest=""
        while songrequest!="exit":
            songrequest=input("Enter your Song Name or Youtube Link: ")
            musicplaylist.songqueuer(songrequest)
            try:
                playthread.start()
            except:
                pass

queuethread=threading.Thread(target=queue)
playthread=threading.Thread(target=play,daemon=True)

f = pyfiglet.Figlet(font='slant')
print(f.renderText('Console YouTube Music'))

queuethread.start()
queuethread.join()

cleandownload()






    