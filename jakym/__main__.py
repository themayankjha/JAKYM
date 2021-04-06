import jakym.downloader as downloader
import jakym.player as player
import os , glob
import threading
import random
from pyfiglet import Figlet
from termcolor import colored

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
    
    def shuffler(self):
            random.shuffle(self.playlist)
            print("Queue Shuffled")

    def songplayer(self,meta):
        print(colored("Currently Playing : " + meta['title'],'yellow'))
        player.playmusic('downloads/'+meta['id'])

musicplaylist = Playlist()

def cleandownload():
    dir ='downloads'
    try:
        for file in os.scandir(dir):
            os.remove(file.path)
    except:
        print("Failed Cleaning")

def play():
    while True:
        if musicplaylist.playlist:
            song=musicplaylist.playlistmanager()
            try:
                meta=musicplaylist.songdownloader(song)
            except:
                print(colored("Error downloading "+song,'red'))
            else:
                musicplaylist.songplayer(meta)
            cleandownload()
        else:
            pass

def queue():
    songrequest=""
    while songrequest!="exit":
        songrequest=input("")
        if songrequest=="shuffle":
            if musicplaylist.playlist:
                musicplaylist.shuffler()
            else:
                print("Cannot Shuffle Empty Queue")
        elif songrequest=="spotify":
            spotifyplaylist=input("Enter Playlist: ")
            spotifyplaylist=downloader.spotifyparser(spotifyplaylist)
            musicplaylist.playlist.extend(spotifyplaylist)
        elif songrequest=="youtube":
            ytplaylist=input("Enter Playlist: ")
            beg=1
            while beg!=-1:
                tempytplaylist,beg=downloader.ytplaylistparser(ytplaylist,beg)
                musicplaylist.playlist.extend(tempytplaylist)
                try:
                    playthread.start()
                except:
                    pass
        else:
            musicplaylist.songqueuer(songrequest)
        try:
            playthread.start()
        except:
            pass

playthread=threading.Thread(target=play,daemon=True)
queuethread=threading.Thread(target=queue)

def main():
    try:
        os.mkdir('downloads')
    except:
        pass
    f = Figlet(font='banner3-D')
    print(" ")
    print(colored(f.renderText('JAKYM'),'cyan'))
    print("\t\t\t\t\t- by Lex")

    queuethread.start()
    queuethread.join()

    cleandownload()
    try:
        os.rmdir('downloads')
    except:
        pass


if __name__ == "__main__":
    main()



    
