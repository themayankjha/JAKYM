import jakym.downloader as downloader
import jakym.player as player
import os , glob
import threading
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

    def songplayer(self,meta):
        print(colored("Currently Playing : " + meta['title'],'yellow'))
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
        if songrequest=="spotify":
            spotifyplaylist=input("Enter Playlist: ")
            spotifyplaylist=downloader.spotifyparser(spotifyplaylist)
            musicplaylist.playlist.extend(spotifyplaylist)
        else:
            musicplaylist.songqueuer(songrequest)
        try:
            playthread.start()
        except:
            pass

playthread=threading.Thread(target=play,daemon=True)
queuethread=threading.Thread(target=queue)

def main():
    f = Figlet(font='banner3-D')
    print(" ")
    print(colored(f.renderText('JAKYM'),'cyan'))
    print("\t\t\t\t\t- by Lex")

    queuethread.start()
    queuethread.join()

    cleandownload()
    os.rmdir('downloads')


if __name__ == "__main__":
    main()



    
