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
from PIL import Image,ImageGrab
import time

# Engine Where We Can Access All Root Of pyttsx3 Module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak Function Let Our Program To Speak Something That We Pass In Audio Argument 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# It Can Take Screenshot With Pillow Module
def takeScreenshot():
    image = ImageGrab.grab()
    image.show()

# It Wish Us According To Time
def wishAccordingToTime():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("How Can I Help You?")

# This Command Take Input From User With Microphone
def takeCommand():
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

if __name__ == '__main__':
    # First Program Wish Us
    wishAccordingToTime()
    # Then It Take Query In Infinite Loop
    while True:
        query = takeCommand().lower()

        # Search In Wikipedia From Our Query
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)
        
        # Open Youtube In Browser
        elif 'open youtube' in query:
            print("opening Youtube...")
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com/')
        
        # Open Visual Studio Code
        elif 'open vs code' in query:
        	print("Opening Visual Studio Code...")
        	speak("opening Visual Studio Code")
        	webbrowser.open('''Path To Visual Studio Code''')
        
        # Open Stackoverflow In Browser
        elif 'open stack overflow' in query:
            print("opening StackOver Flow...")
            speak("opening stack over flow")
            webbrowser.open('https://stackoverflow.com/')
        
        # Open Google In Browser
        elif 'open google' in query:
            print("opening Google...")
            speak("opening google")
            webbrowser.open('https://www.google.com/')
        
        # Tell Us That Who Is He
        elif 'who are you' in query:
            speak("I'am Jarvis , A Voice Assistant")
        
        # Take Screenshot
        elif "take screenshot" in query:
        	speak("Taking screenshot")
        	time.sleep(2)
        	takeScreenshot()
        	speak("screenshot taked")
        
        # Open Chrome
        elif 'open chrome' in query:
            print("Opening Chrome Browser...")
            speak("opening chrome browser")
            chrome = '''Path To Chrome'''
            os.startfile(os.path.join(chrome))
        
        # KILL CHROME TASK
        elif 'close chrome' in query:
            print("closing Chrome Browser...")
            speak("closing chrome browser")
            os.system('TASKKILL /F /IM Google_Chrome.exe')
        
        # Open Sublime Text
        elif 'open sublime text' in query:
            print("opening Sublime Text 3...")
            speak("opening sublime text 3")
            text = '''Path To Sublime Text'''
            os.startfile(os.path.join(text))
        
        # Open PyCharm
        elif 'open pycharm' in query:
            print("opening PyCharm...")
            speak("opening pycharm")
            PyCharm = '''Path to pycharm'''
            os.startfile(os.path.join(PyCharm))
        
        # Terminate The Program
        elif 'go to sleep' in query:
            speak("Okay , I'am Going")
            exit()
            print("Program Closed")
        
        # Tell Us The Time
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir , The Time Is {time}")
        
        # Speak Hello Sir When We Say Hello Jarvis
        elif "hello jarvis" in query:
            speak("Hello Sir")
        
        # Force Python Developer To Create Python4
        elif "how are you" in query:
            speak("I'am Fine, but i don't know when my house is upgrade, when python 4 is release")
        
        # Shut Down Your Computer/Laptop
        elif "shut down" in query:
            print("Shuting Down Computer...")
            speak("Shuting Down Computer")
            os.system("shutdown /s /t 1")
        
        # Play Music In a List
        elif "play music list" in query:
            musicR = '''Path To Your Favorite Music Directory'''
            songs = os.listdir(musicR)
            os.startfile(os.path.join(musicR, songs[0]))
        
        # Remind Us That We Made Him
        elif "you are mad" in query:
        	speak("Sir , First Think That , Who made me")

        # You Can Add So Much Query And Can Send It To https://programmingfire.com/Contacts/