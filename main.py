import downloader
import player
import os
import threading


queue=[]

def play(meta):
    print("Currently Playing : " + meta['title'])
    player.playmusic('downloads/'+meta['id'])
    os.remove('downloads/'+meta['id']) 

def getquery(queue):
    query = input("Enter Song Name or Link: ")
    return query+" song"

def doqueue():
    for query in queue:
        meta=downloader.download(query)
        play(meta)
    

t1 = threading.Thread(target=doqueue, args=(), daemon=True)

while True:
    query=getquery(queue)
    queue.append(query)
    try:
        t1.start()
    except:
        pass




    