import vlc
import time
import random

p = vlc.MediaPlayer("file:///home/namal/MyTest/Python/pypasstheparcel/media/song1.mp3")
p.play()

i = 0

while i <= 6:
    playtime = random.randint(20,50)
    p.play()
    time.sleep(playtime)
    p.stop()
    time.sleep(30)
    i += 1 
