import time
from datetime import datetime, timedelta
from pygame import mixer

while True:
    mixer.init()
    mixer.music.load("C:/Users/xande/Documents/GitHub/Semi-hourly-Screaming/semi hourly screaming.mp3") # Change this to the folders in your computer
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    screamTime = f"{(datetime.now() + timedelta(minutes=30)).hour}:{(datetime.now() + timedelta(minutes=30)).minute}"
    print(f"Next scream will be at {screamTime}")
    time.sleep(1800)