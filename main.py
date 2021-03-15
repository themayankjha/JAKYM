import downloader
import player
import os


link="https://www.youtube.com/watch?v=q7_DqgVDKkM"

meta=downloader.download(link)
print("Currently Playing : " + meta['title'])

player.playmusic(meta['id'])
os.remove(meta['id']) 

    