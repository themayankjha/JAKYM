import jakym.downloader as downloader
from jakym.playlistmanager import Playlist,cleandownload,makedownload,removedownload

import threading, argparse

from pyfiglet import Figlet
from colorama import init,deinit
from termcolor import colored

musicplaylist = Playlist()
songavailable = threading.Event()

def playspotify(link):
    spotifyplaylist=downloader.spotifyparser(link)
    musicplaylist.playlist.extend(spotifyplaylist)
    songavailable.set()

def playyoutube(link):
    beg=1
    while beg!=-1:
        tempytplaylist,beg=downloader.ytplaylistparser(link,beg)
        musicplaylist.playlist.extend(tempytplaylist)
        songavailable.set()

def play():
    while True:
        if musicplaylist.playlist:
            song=musicplaylist.returnsong()
            try:
                meta=musicplaylist.downloadsong(song)
            except:
                print(colored("Error downloading "+song,'red'))
            else:
                musicplaylist.playsong(meta)
            cleandownload()
        else:
            songavailable.clear()
            songavailable.wait()

def queue():
    songrequest=""
    while songrequest!="exit":
        songrequest=input("")
        if songrequest=="shuffle":
            if musicplaylist.playlist:
                musicplaylist.shuffleplaylist()
            else:
                print("Cannot Shuffle Empty Queue")
        elif songrequest=="spotify":
            spotifyplaylistlink=input("Enter Playlist: ")
            playspotify(spotifyplaylistlink)
        elif songrequest=="youtube":
            ytplaylist=input("Enter Playlist: ")
            playyoutube(ytplaylist)           
        else:
            musicplaylist.addsong(songrequest)
            songavailable.set()
        

playthread=threading.Thread(target=play,daemon=True)
queuethread=threading.Thread(target=queue)

def main():
    makedownload()
    init()

    f = Figlet(font='banner3-D')
    print(" ")
    print(colored(f.renderText('JAKYM'),'cyan'))
    print("\t\t\t\t\t\t- by Lex")

    parser = argparse.ArgumentParser(prog='jakym', description='Just Another Konsole Youtube-Music',epilog='Thank you for using Jakym! :)')
    parser.version = '0.3.2'
    parser.add_argument("-s", action='store', metavar='link', help="Play a Spotify Playlist")
    parser.add_argument("-y", action='store', metavar='link', help="Play a Youtube Playlist")
    parser.add_argument("-p", action='store', nargs='+', metavar='song', help="Play multiple youtube links or a songs")
    parser.add_argument('-v', action='version')
    args = parser.parse_args()

    queuethread.start()
    playthread.start()

    if args.s:
        playspotify(args.s)
    if args.y:
        playyoutube(args.y)
    if args.p:
        for songs in args.p:
            musicplaylist.addsong(songs)
        songavailable.set()
    

    queuethread.join()

    cleandownload()
    deinit()
    removedownload()


if __name__ == "__main__":
    main()



    
