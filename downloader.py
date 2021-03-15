
import youtube_dl


def download(link):
    options={
    'format': 'bestaudio/best',
    'outtmpl': '%(id)s',
    'quiet':'True'}

    downloader=youtube_dl.YoutubeDL(options)
    meta = downloader.extract_info(link, download=True)

    return meta

