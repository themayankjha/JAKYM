import jakym.downloader as downloader
from jakym.playlistmanager import Playlist
from jakym.player import wait

import threading, argparse, json, sys

from pyfiglet import Figlet
from colorama import init,deinit
from termcolor import colored

musicplaylist = Playlist()
songavailable = threading.Event()

dir=downloader.makedownload()


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

def startmusic():
    song=musicplaylist.returnsong()
    try:
        meta=musicplaylist.downloadsong(song,dir)
    except:
        print(colored("Error downloading "+song,'red'))
    else:
        musicplaylist.playsong(meta,dir)

def play():
    while True:
        try:
            if musicplaylist.playobj.is_playing():
                musicplaylist.playobj.wait_done()
        except:
            pass
        
        if  musicplaylist.songpaused==True:
            wait()

        elif musicplaylist.repeat==2:
            musicplaylist.shiftlastplayedsong()
            startmusic()

        elif musicplaylist.queuedplaylist :    
            startmusic()

        else:
            if musicplaylist.repeat==1:
                musicplaylist.loopqueue()

            else:
                songavailable.clear()
                songavailable.wait()

def queue():
    while True:
        request=input("")
        if request=="exit":
            deinit()
            downloader.removedownload(dir)
            sys.exit()
        
        elif request=="" or request==" ":
            pass

        elif request=="shuffle":
            if musicplaylist.queuedplaylist:
                musicplaylist.shuffleplaylist()
            else:
                print("Cannot Shuffle Empty Queue")
        
        elif request=="play":
            musicplaylist.resumesong(dir)
            songavailable.set()

        elif request=="pause":
            musicplaylist.pausesong()
        
        elif request=="next":
            musicplaylist.nextsong()

        elif request=="back":
            musicplaylist.previoussong()
        
        elif request=="rm":
            musicplaylist.removelastqueuedsong()

        elif request.startswith("repeat"):
            mode = request.split()[1]  
            musicplaylist.repeatsong(mode)

        elif request.startswith("seek"):
            value = request.split()[1]
            try:
                value = int(value)
                musicplaylist.seeksong(value,dir)
            except:
                print("Error: Invalid seek value ",'red')

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
        
        elif request=="commands":
            print("Type spotify to play music using spotify playlist")
            print("Type youtube to play music using youtube playlist")
            print("Use rm to remove the last queued song from the playlist.")
            print("Type shuffle to shuffle your queue.")
            print("Use load to load a playlist and save to save your playlist.Include the trailing slash in path i.e. specify path as C:\\Users\\Lex\\Music\\ or /home/lex/Projects/jakym/.")
            print("Use play , pause, next, back to control the playback.")
            print("Use repeat all, repeat song and repeat offto control song repetition.")
            print("Use seek with an integer like 10 or -10 to control the current song.")
            print("To exit the command window and hence the application simply type exit.")
                       
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
    parser.version = '0.4.0'
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
    downloader.removedownload(dir)


if __name__ == "__main__":
    main()
