import vlc
import time
import random

p = vlc.MediaPlayer("file:///pypasstheparcel/media/song1.mp3")
p.play()

i = 0

while i <= 10:
    playtime = random.randint(20,50)
    p.play()
    time.sleep(playtime)
    p.stop()
    time.sleep(60)
    i += 1 
