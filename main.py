import time
from datetime import datetime, timedelta
from pygame import mixer

while True:
    mixer.init()
    mixer.music.load("C:/Users/xande/Documents/GitHub/Semi-hourly-Screaming/semi hourly screaming.mp3") # Change this to the folders in your computer
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    screamTime = datetime.now() + timedelta(minutes=30)
    screamHour = screamTime.hour
    screamMinute = screamTime.minute
    if len(str(screamMinute)) == 1:
        screamMinute = "0" + str(screamMinute)
    screamText = f"{screamHour}:{screamMinute}"
    print(f"Next scream will be at {screamText}")
    time.sleep(1800)