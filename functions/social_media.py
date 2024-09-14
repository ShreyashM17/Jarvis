import webbrowser

from jarvis import voice


def whatsapp():
    voice.speak('starting whatsapp')
    webbrowser.open_new_tab("https://web.whatsapp.com/")
    voice.speak('whatsapp opened')


def facebook():
    voice.speak('starting facebook')
    webbrowser.open_new_tab("https://www.facebook.com/")
    voice.speak('facebook opened')


def instagram():
    voice.speak('starting instagram')
    webbrowser.open_new_tab("https://www.instagram.com/")
    voice.speak('instagram opened')


def twitter():
    voice.speak('starting twitter')
    webbrowser.open_new_tab("https://twitter.com/home")
    voice.speak('twitter opened')


def linkedin():
    voice.speak('starting linkedin')
    webbrowser.open_new_tab("https://www.linkedin.com/feed/")
    voice.speak('linkedin opened')


def main(command):
    activity = []
    if "whatsapp" in command:
        activity.append('whatsapp')
        whatsapp()
    elif "facebook" in command:
        activity.append('facebook')
        facebook()
    elif "linkedin" in command:
        activity.append('linkedin')
        linkedin()
    elif "instagram" in command:
        activity.append('instagram')
        instagram()
    elif "twitter" in command:
        activity.append('twitter')
        twitter()
    else:
        voice.speak("Which social media would you like to open")
        activity.append('social media')
        command = voice.take_command()
        if "whatsapp" in command:
            activity.append('whatsapp')
            whatsapp()
        elif "facebook" in command:
            activity.append('facebook')
            facebook()
        elif "linkedin" in command:
            activity.append('linkedin')
            linkedin()
        elif "instagram" in command:
            activity.append('instagram')
            instagram()
        elif "twitter" in command:
            activity.append('twitter')
            twitter()
        else:
            voice.speak("I don't have such social media sites in my database\n if you want i can tell u which "
                        "social media apps i can access")
            activity.append('social media options')
            voice.take_command()
            if "yes" in command:
                voice.speak("whatsapp instagram facebook linkedin twitter out of these which should i open")
                if "whatsapp" in command:
                    activity.append('whatsapp')
                    whatsapp()
                elif "facebook" in command:
                    activity.append('facebook')
                    facebook()
                elif "linkedin" in command:
                    activity.append('linkedin')
                    linkedin()
                elif "instagram" in command:
                    activity.append('instagram')
                    instagram()
                elif "twitter" in command:
                    activity.append('twitter')
                    twitter()
            else:
                activity.append('no social media')
                voice.speak("as you say sir")
    return activity
