
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
            meta = ytdl.extract_info(f"ytsearch:{link}", download=True)['entries'][0]
        else:
            meta = ytdl.extract_info(link, download=True)
    print("Done Downloading")
    return meta

