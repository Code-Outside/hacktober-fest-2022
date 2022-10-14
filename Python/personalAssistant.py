import pyttsx3
import datetime
import requests
from requests.api import request
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import cv2
from requests import get
import sys
import pyautogui


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")

    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:

        speak("Good Evening")

    speak(" I am Adith., How may I help you!")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('devlegit146@gmail.com', 'Neeraj@7860')
    server.sendmail('devlegit146@gmail.com', to, content)

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c046d4a676484a789356a7523d35e337'

    main_page = requests.get(main_url).json

    articles = main_page["articles"]

    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):

        speak(f"today's {day[i]} news is: {head[i]}")

def takeCommand():
    #It takes microphne input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing Tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("Sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")


        elif 'open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'play music' in query:
            music_dir = 'N:\\adith\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, The time is", strTime)



        elif 'open vs code' in query:
            fileopen = '"N:\\Microsoft VS Code\\Code.exe"'
            os.startfile(fileopen)
        
        elif 'close vs code' in query:
            speak('okay sir, closing vs code')
            os.system("taskkill /f /im Code.exe")


        elif 'email to neeraj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nk5825162@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry sir email not sent")


        elif 'who is siri' in query:

            speak('siri and I are friends but you will get her after spending good bucks and I am cheaper')

        elif 'play video' in query:
            video_dir = 'N:\\love'
            videos = os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir, videos[0]))


        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"IP address{ip}")
            speak(f"Your IP address is{ip}")
            
        elif 'send message on whatsapp' in query:
            msg = speak('What to send')
            pywhatkit.sendwhatmsg("+916386478681" f"{msg}")

        elif 'set alarm' in query:
            alr = int(datetime.datetime.now().hour)
            if alr == 22:
                music_dir = 'N:\\adith\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")
        
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        
        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
              
        elif 'no thanks' in query:
            speak('thanks for using me sir, have a goodday')
            sys.exit()
        
        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        
        elif 'tell me news' in query:
            speak('please wait sir, fetching the latest news')
            news()


        speak("sir, do you have any other work")




