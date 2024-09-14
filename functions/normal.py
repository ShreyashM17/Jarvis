from datetime import datetime
from num2words import num2words
from jarvis import voice
import psutil
import urllib.request as req
current_hour = int(datetime.now().strftime('%H'))


def greeting():
    global current_hour
    current_hour = int(datetime.now().strftime('%H'))
    if 4 <= current_hour < 12:
        greet = "Good Morning"
    elif 12 <= current_hour < 18:
        greet = "Good Afternoon"
    elif 18 <= current_hour < 22:
        greet = "Good Evening"
    else:
        greet = " "
    voice.speak(greet)
    print(greet)


def current_time():
    current_minute = datetime.now().strftime('%M')
    current_hour12 = current_hour % 12
    time = num2words(current_hour12) + num2words(current_minute)
    if current_hour < 12:
        voice.speak(f"It's {time} am Sir")
    elif current_hour == 0:
        time = num2words(12) + num2words(current_minute)
        voice.speak(f"It's {time} pm Sir")
    else:
        voice.speak(f"It's {time} pm Sir")


def leaving():
    if 4 <= current_hour < 18:
        voice.speak("have a nice day")
    else:
        voice.speak("Good night")


def battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    charging = battery.power_plugged
    terminate = False
    if percentage == 100 and charging == True:
        voice.speak("Please unplug the charger sir, we are at our full capacity")
    elif percentage < 20 and charging == False:
        voice.speak("Please plugin the charger sir, we are low on power")
    elif percentage < 10 and charging == False:
        voice.speak("Battery too low, jarvis is getting shut down, to maintain some necessary option on")
        terminate = True
    return terminate


def internet():
    host = "https://www.google.com"
    try:
        req.urlopen(host)
        connected = True
    except:
        connected = False
    return connected


def main(command):
    activity = []
    if 'time' in command:
        current_time()
        activity.append('time')
    return activity
