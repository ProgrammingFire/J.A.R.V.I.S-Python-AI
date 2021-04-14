# pip install speechrecognition
import speech_recognition as sr
# pip install pyttsx3
import pyttsx3
import datetime
# pip install wikipedia
import wikipedia
import webbrowser
import os
# pip install pillow
from PIL import Image, ImageGrab
import time
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeScreenshot():
    image = ImageGrab.grab()
    image.show()


def wishAccordingToTime():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("How Can I Help You?")


def takeCommand():  # This command take input from user with microphone

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-In')
        print("You Said :", query)

    except Exception as e:
        # print(e)
        return "None"

    return query

def sendEmail(to, message):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    email = '''Your Email Address'''
    password = '''Your Email Password'''
    server.login(email, password)
    contact = to
    message = message
    server.sendmail(email, contact, message)
    server.quit()

if __name__ == '__main__':
    wishAccordingToTime()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("opening Youtube...")
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com/')

        elif 'open vs code' in query:
            print("Opening Visual Studio Code...")
            speak("opening Visual Studio Code")
            webbrowser.open('''Path To Visual Studio Code''')

        elif 'open stack overflow' in query:
            print("opening StackOver Flow...")
            speak("opening stack over flow")
            webbrowser.open('https://stackoverflow.com/')

        elif 'open google' in query:
            print("opening Google...")
            speak("opening google")
            webbrowser.open('https://www.google.com/')

        elif 'who are you' in query:
            speak("I'am Jarvis , A Voice Assistant")

        elif "take screenshot" in query:
            speak("Taking screenshot")
            time.sleep(2)
            takeScreenshot()
            speak("screenshot taked")

        elif 'open chrome' in query:
            print("Opening Chrome Browser...")
            speak("opening chrome browser")
            chrome = '''Path To Chrome'''
            os.startfile(os.path.join(chrome))

        elif 'close chrome' in query:
            print("closing Chrome Browser...")
            speak("closing chrome browser")
            os.system('TASKKILL /F /IM Google_Chrome.exe')

        elif 'open sublime text' in query:
            print("opening Sublime Text 3...")
            speak("opening sublime text 3")
            text = '''Path To Sublime Text'''
            os.startfile(os.path.join(text))

        elif 'open pycharm' in query:
            print("opening PyCharm...")
            speak("opening pycharm")
            PyCharm = '''Path to pycharm'''
            os.startfile(os.path.join(PyCharm))

        elif 'go to sleep' in query:
            speak("Okay , I'am Going")
            exit()
            print("Program Closed")

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir , The Time Is {time}")

        elif "hello jarvis" in query:
            speak("Hello Sir")

        elif "how are you" in query:
            speak(
                "I'am Fine, but i don't know when my house is upgrade, when python 4 is release")

        elif "shut down" in query:
            print("Shuting Down Computer...")
            speak("Shuting Down Computer")
            os.system("shutdown /s /t 1")

        elif "play music list" in query:
            musicR = '''Path To Your Favorite Music Directory'''
            songs = os.listdir(musicR)
            os.startfile(os.path.join(musicR, songs[0]))

        elif "send mail" in query:
            try:
                speak("What Message Should I Send")
                message = takeCommand()
                sendEmail('''Your Friend Email Address''', message)
                speak("E-Mail Sent")
            except Exception as e:
                print(e)

elif "you are mad" in query:
    speak("Sir , First Think That , Who made me")

    # You Can Add So Much Query And Can Send It To https://programmingfire.com/Contacts/
