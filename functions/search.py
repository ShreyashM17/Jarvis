import webbrowser
from jarvis import voice

query = " "


def initial():
    voice.speak("What should i search for")
    query = voice.take_command()
    return query


def done():
    voice.speak("Results are on your screen sir")


def google(query=None):
    voice.speak('initializing google')
    if query == None:
        query = initial()
        webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    else:
        webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    done()


def youtube(query=None):
    voice.speak('starting youtube')
    if query == None:
        query = initial()
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
    else:
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
    done()


def main(command):
    activity = []
    if "search for" in command:
        command = command.split()
        i = command.index("for")
        query = " "
        for j in range(i + 1):
            command.pop(0)
        if "youtube" in command:
            k = command.index("youtube")
            command.pop(k)
            command.pop(k - 1)
            command = query.join(command)
            activity.append('youtube')
            youtube(command)
        elif "google" in command:
            k = command.index("google")
            command.pop(k)
            command.pop(k - 1)
            command = query.join(command)
            activity.append('google')
            google(command)
    elif "who is" in command or 'what is' in command:
        activity.append('google')
        google(command)
    elif "google" in command:
        activity.append('google')
        google()
    elif "youtube" in command:
        activity.append('youtube')
        youtube()
    else:
        voice.speak("where should i search\ncurrently i could only search in google or youtube")
        command = voice.take_command()
        activity.append('search')
        if "google" in command:
            google()
            activity.append("google")
        elif "youtube" in command:
            youtube()
            activity.append('youtube')
        else:
            activity.append("can't understand")
            voice.speak("can't understand")
    return activity
