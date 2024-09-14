import sys
import time
import speech_recognition as sr
import pyttsx3
from brain import brainV1
from functions import calci, music_player, news, normal, social_media, search
from jarvis import voice
from jarvis.voice import speak
from jarvis.voice import take_command

listener = sr.Recognizer()
listener.pause_threshold = 0.5
talk = pyttsx3.init('sapi5')
say = ""
verified = True


def initialize_jarvis():
    print("Initializing Jarvis...")
    loading = ["[          ]", "[-         ]", "[--        ]", "[---       ]", "[----      ]", "[ ----     ]",
               "[  ----    ]", "[   ----   ]", "[    ----  ]", "[     ---- ]", "[      ----]", "[       ---]",
               "[        --]", "[         -]", "[          ]", "[          ]", "[-         ]", "[--        ]",
               "[S--       ]", "[IS--      ]", "[VIS--     ]", "[RVIS--    ]", "[ARVIS--   ]", "[JARVIS--  ]",
               "[-JARVIS-- ]", "[--JARVIS--]"]
    talk.say("Initializing jarvis")
    talk.runAndWait()
    for k in range(len(loading)):
        time.sleep(0.1)
        sys.stdout.write("\r" + loading[k] + "  " + str(k * 4) + "%")
        sys.stdout.flush()

    print("\n")
    talk.say("jarvis initialized")
    talk.runAndWait()
    vocal = talk.getProperty('voices')
    talk.setProperty('voice', vocal[0].id)
    print("Initialized")
    normal.greeting()


while not verified:
    voice.friday("hello May I know who are you")
    command = voice.take_command()
    if "shre" in command:
        voice.friday("Hello Shreyash, can you please verify yourself by typing the password")
        for i in range(3):
            password = input()
            if password == "1722":
                verified = True
                voice.friday("Password correct")
                initialize_jarvis()
                break
            else:
                voice.friday("incorrect password")
                voice.friday("Access Denied")
                voice.friday("")
        break
    else:
        voice.friday("Unauthorized Access")
        break

counter = 0
while verified:
    try:
        command = take_command()
        print("Recognizing....")
        start = time.time()
        saying = brainV1.brain(command)
        speak(saying[0])
        if 'greeting' in saying[1]:
            normal.greeting()
        elif 'search' in saying[1]:
            search.main(command)
        elif "normal" in saying[1]:
            normal.main(command)
        elif 'social media' in saying[1]:
            social_media.main(command)
        elif 'calculator' in saying[1]:
            calci.main(command)
        elif 'music' in saying[1]:
            counter = music_player.music_player(command, counter)
        elif 'news' in saying[1]:
            news.main(command)
        elif 'terminate' in saying[1]:
            normal.leaving()
            end = time.time()
            print(end - start)
            break
        elif 'not found' in saying[1]:
            speak(saying(0))
            speak("Can you add this in my command line and tell me what to do")
        end = time.time()
        print(end-start)
    except Exception as e:
        speak(f"Something went wrong sir {str(e)}")
