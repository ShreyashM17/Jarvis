import speech_recognition as sr
import pyttsx3

talk = pyttsx3.init('sapi5')
listener = sr.Recognizer()


def friday(say):
    voices = talk.getProperty('voices')
    talk.setProperty('voice', voices[1].id)
    talk.say(say)
    print(f'--{say}')
    talk.runAndWait()


def speak(say):
    talk.say(say)
    talk.runAndWait()
    print(f'Jarvis: {say}')


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            listener.pause_threshold = 0.5
            command = listener.recognize_google(audio, language='en')
            command = command.lower()
            print(command)
            return command
    except:
        speak("Can't hear you can you please type the command")
        command = input("You:")
        command = command.lower()
        return command
