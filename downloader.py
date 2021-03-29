
from youtube_dl import YoutubeDL
from requests import get


def download(link):
    options={
    'format': 'aac/mp3/ogg/wav/3gp/mp4',
    'outtmpl': 'downloads/%(id)s',}
    with YoutubeDL(options) as ytdl:
        try:
            get(link)
        except:
            meta = ytdl.extract_info(f"ytsearch:{link}", download=True)['entries'][0]
        else:
            meta = ytdl.extract_info(link, download=True)
    return meta

