import os
from pygame import mixer

from jarvis import voice


def play(c):
    mixer.music.load(c)
    mixer.music.play()


def stop():
    mixer.music.stop()


def music_player(command, a):
    mixer.init()
    os.chdir(r"C:\Users\Shreyash\Music")
    loc = os.listdir()
    activity = []
    if 'stop' in command:
        activity.append('stop')
        stop()
    elif 'next' in command:
        activity.append('next')
        voice.speak("Playing next song")
        while True:
            try:
                a += 1
                play(loc[a])
                break
            except:
                continue
    elif 'previous' in command:
        activity.append('previous')
        voice.speak("Playing previous one")
        while True:
            try:
                a -= 1
                play(loc[a])
                break
            except:
                continue
    else:
        voice.speak("Droping some beats")
        activity.append('play')
        play(loc[a])
    return activity, a
