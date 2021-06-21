import jakym.downloader as downloader
from jakym.playlistmanager import Playlist,makedownload,removedownload

import threading, argparse, json

from pyfiglet import Figlet
from colorama import init,deinit
from termcolor import colored

musicplaylist = Playlist()
songavailable = threading.Event()

dir=makedownload()

def playspotify(link):
    spotifyplaylist=downloader.spotifyparser(link)
    musicplaylist.queuedplaylist.extend(spotifyplaylist)
    songavailable.set()

def playyoutube(link):
    beg=1
    while beg!=-1:
        tempytplaylist,beg=downloader.ytplaylistparser(link,beg)
        musicplaylist.queuedplaylist.extend(tempytplaylist)
        songavailable.set()

def saveplaylist(path,name):
    with open(path+'jaylist.json', 'a+', encoding='utf-8') as f:
        f.seek(0)
        try:
            playlistdata=json.load(f)
        except:
            playlistdata={}
        playlistdata[name]=musicplaylist.returnplaylist()
        f.truncate(0)
        json.dump(playlistdata, f, ensure_ascii=False, indent=4)
    print("Successfully Saved")

def loadplaylist(path,name):
    try:
        with open(path+'jaylist.json', 'r', encoding='utf-8') as f:
            musicplaylist.queuedplaylist.extend(json.load(f)[name])
        print(print("Successfully loaded"))
        songavailable.set()
    except:
        print(colored("Cannot Find the jaylist.json file at "+path,'red'))
    
def play():
    while True:
        if musicplaylist.queuedplaylist:
            song=musicplaylist.returnsong()
            try:
                meta=musicplaylist.downloadsong(song,dir)
            except:
                print(colored("Error downloading "+song,'red'))
            else:
                musicplaylist.playsong(meta,dir)
        else:
            songavailable.clear()
            songavailable.wait()

def queue():
    request=""
    while request!="exit":
        request=input("")
        if request=="shuffle":
            if musicplaylist.playlist:
                musicplaylist.shuffleplaylist()
            else:
                print("Cannot Shuffle Empty Queue")
        elif request=="spotify":
            spotifyplaylistlink=input("Enter Playlist: ")
            playspotify(spotifyplaylistlink)
        elif request=="youtube":
            ytplaylist=input("Enter Playlist: ")
            playyoutube(ytplaylist)  
        elif request=="save":
            playlistname=input("Enter Playlist Name: ")
            playlistpath=input("Enter Path: ")
            saveplaylist(playlistpath,playlistname) 
        elif request=="load":
            playlistname=input("Enter Playlist Name: ")
            playlistpath=input("Enter Path: ")
            loadplaylist(playlistpath,playlistname) 
        else:
            musicplaylist.addsong(request)
            songavailable.set()
        

playthread=threading.Thread(target=play,daemon=True)
queuethread=threading.Thread(target=queue)

def main():
    init()

    f = Figlet(font='banner3-D')
    print(" ")
    print(colored(f.renderText('JAKYM'),'cyan'))
    print("\t\t\t\t\t\t- by Lex")

    parser = argparse.ArgumentParser(prog='jakym', description='Just Another Konsole Youtube-Music',epilog='Thank you for using Jakym! :)')
    parser.version = '0.3.3'
    parser.add_argument("-s", action='store', metavar='link', help="Play a Spotify Playlist")
    parser.add_argument("-y", action='store', metavar='link', help="Play a Youtube Playlist")
    parser.add_argument("-p", action='store', nargs='+', metavar='song', help="Play multiple youtube links or a songs")
    parser.add_argument("-l", action='store', nargs=2, metavar=('playlistpath','playlistname'), help="Play a jakym generated playlist")
    parser.add_argument('-v', action='version')
    args = parser.parse_args()

    queuethread.start()
    playthread.start()

    if args.s:
        playspotify(args.s)
    if args.y:
        playyoutube(args.y)
    if args.l:
        loadplaylist(args.l[0],args.l[1])
    if args.p:
        for songs in args.p:
            musicplaylist.addsong(songs)
        songavailable.set()
    
    queuethread.join()

    deinit()
    removedownload(dir)


if __name__ == "__main__":
    main()



    
