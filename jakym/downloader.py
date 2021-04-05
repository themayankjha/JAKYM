
from youtube_dl import YoutubeDL
from requests import get
from bs4 import BeautifulSoup
import re
import json

def spotifyparser(url):
    print("Pinging "+url)
    spotifyhtml=get(url)
    soup=BeautifulSoup(spotifyhtml.content,"lxml")
    tags=soup('script')
    x=re.findall("Spotify.Entity = (.*);",tags[5].contents[0])
    data=x[0]
    jsonfile=json.loads(data)

    print("Adding "+jsonfile['name']+" To Queue." )
    tracks=jsonfile['tracks']['items']

    tracklist=[]

    for track in tracks:
        trackname=track['track']['name']
        artistname=""
        for artist in track['track']['artists']:
            artistname=artistname+" "+artist['name']
        tracklist.append(trackname+artistname)

    return tracklist

class MyLogger(object):
    def debug(self, msg):
        if msg.startswith("[download] Downloading video"):
            numlist=re.findall('[0-9]+', msg)
            print("Processing Song: "+numlist[0]+"/"+numlist[1])
    def warning(self, msg):
        pass

    def error(self, msg):
        pass

def ytplaylistparser(url,beg):
    
    options={
    'logger': MyLogger(),
    'playlist_items':f'{beg}-{beg+4}'
    }
    print("Pinging Youtube")
    with YoutubeDL(options) as ytdl:
        try:
            meta = ytdl.extract_info(url, download=False)
        except:
            pass
    
    tracklist=[]

    tracker=0
    for song in meta['entries']:
        tracklist.append(song['webpage_url'])
        tracker=tracker+1
    if tracker==5:
        beg=beg+tracker
    else:
        beg=-1
    return tracklist,beg

def download(link):
    options={
    'format': 'aac/mp3/ogg/wav/3gp/m4a/mp4',
    'outtmpl': 'downloads/%(id)s',
    'quiet':'True'
    }
    print("Downloading")
    with YoutubeDL(options) as ytdl:
        try:
            get(link)
        except:
            meta=ytdl.extract_info(f"ytsearch:{link}", download=True)['entries'][0]
        else:
            meta=ytdl.extract_info(link, download=True)
    print("Done Downloading")
    return meta
