import datetime
import operator
import os
import smtplib
import sys
import ecapture
import time
import webbrowser
from email.message import EmailMessage
import instabot as Bot
import pyttsx3
import speech_recognition as sr
import wikipedia
import googlesearch as gs
import speedtest
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import PyPDF2
import tkinter
import json
import pyjokes
from twilio.rest import Client
import shutil
import winshell
import requests
import feedparser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    strTime = datetime.datetime.now().strftime('%H:%M:%S')
    speak(f"Sir, the time is {strTime}")
    print(strTime)

def username():
    speak("What should i call you sir")
    name = takeCommand()
    speak('Welcome Mister')
    speak(name)
    columns = shutil.get_terminal_size().columns
    print("################".center(columns))
    print('Welcome Mr. ', name.center(columns))
    print('################'.center(columns))
    speak('How can i Help you, Sir')


def sendEmail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('divyakabra2003@gmail.com', 'divyakabra2590689d')
    email = EmailMessage()
    email['From'] = 'divyakabra2003@gmail.com'
    email['TO'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    '2233': 'divyakabra2233@gmail.com',
    'tonji': 'ayushikabra0@gmail.com',
    'Hulk': 'shrutikabra3@gmail.com'
}
def alarm():
    hour = (datetime.datetime.now().hour)
    if hour == 17:
        speak('Sir now you have to start learning about ML. Its 5pm')

    elif hour == 18:
        speak('This is a second alarm')


def get_email_info():
    speak('To whom you want to send email')
    name = takeCommand()
    receiver = email_list[name]
    print(receiver)
    speak('What is the subject of your email?')
    subject = takeCommand()
    speak('What is the body of your email?')
    message = takeCommand()
    sendEmail(receiver, subject, message, )
    speak('Sir,email is sent')
    speak('do you want to send email once more?')
    send_more = takeCommand()
    if 'yes' in send_more:
        get_email_info()
    elif 'no' in send_more:
        speak('ok')


def pdf_reader():
    book = open('python_tutorial.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in the book {pages}")
    speak("sir please enter the page number you have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n ")


    except Exception as e:
        # print(e)
        print("Say that again please")
        return 'None'
    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    wishMe()
    alarm()
    username()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'sleep friday' in query:
            sys.exit()
        elif 'how are you' in query:
            speak("I am fine sir, How are you")
        elif 'activate how to do mode' in query:
            from pywikihow import search_wikihow

            speak("how to do mode is activated please tell me what you want to know")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif 'who i am' in query:
            speak('If you talk then definitely you are human.')
        elif 'read book' in query:
            pdf_reader()
        elif 'who are you' in query:
            speak('I am your virtual assistant created by Divya')
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak('Recycle bin recycled')
        elif "don't listen" in query:
            speak("For how much time you want me to sleep")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif 'how are you' in query:
            speak("I'm fine, glad you asked me that")


        elif 'weather' in query:
            api_key = '692a2efb66b6a674ae636640416af2ac'
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak('City name')
            print('City name : ')
            city_name = takeCommand()
            complete_url = base_url + 'appid = ' + api_key + '&q =' + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x['cod'] != '404':
                y = x['main']
                currrent_temperature = y['temp']
                current_pressure = y['pressure']
                current_humidiy = y['humidity']
                z = x['weather']
                weather_description = z[0]['description']
                print(' Temperature (in kelvin unit) = ' + str(currrent_temperature)+'\n atmospheric pressure (in hPa unit)='+str(current_pressure) + '\n humidity (in percentage) = ' +str(current_humidiy) + '\n description = ' +str(weather_description))
            else:
                speak("City not found")
        elif 'open youtube' in query:
            webbrowser.get('C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s').open('youtube.com')
        elif 'open google' in query:
            webbrowser.get('C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s').open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.get('C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s').open('stackoverflow.com')

        elif 'open codecademy' in query:
            webbrowser.get('C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s').open('codecademy.com')
        elif 'whatsapp' in query:
            webbrowser.get('C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s').open('web.whatsapp.com')
        elif 'telegram' in query:
            webbrowser.get('C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s').open(
                'https://web.telegram.org/')
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir[0]))

        elif 'open code' in query:
            path = "C:\\Users\\Kabra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open illustrator' in query:
            illustrator = "C:\\Program Files\\Adobe\\Adobe Illustrator 2021\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(illustrator)
        elif 'open photoshop' in query:
            photoshop = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(photoshop)
        elif 'dreamveaver' in query:
            dream = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
        elif 'epic games launcher' in query:
            launcher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(launcher)
        elif 'tlauncher' in query:
            minecraft = "C:\\Users\\Kabra\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(minecraft)
        elif "What is the temperature in indore" in query:
            search = "temperature in indore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
        elif "Why did I made you friday" in query:
            speak("I made you to use for your personal uses.")

        elif "search on google" in query:
            speak("What should i search sir")
            search = takeCommand()
            gx_path = 'C://Users//Kabra//AppData//Local//Programs//Opera GX//launcher %s'
            webbrowser.get(gx_path).open_new_tab(search + '.com')
        elif "search on youtube" in query:
            speak("What should i search on youtube sir")
            search = takeCommand()
            gx_path = 'C://Users//Kabra//AppData//Local//Programs//Opera GX//launcher %s'
            webbrowser.get(gx_path).open_new_tab('https://www.youtube.com/results?search_query=' + search)
        elif "play liked songs on spotify" in query:
            speak('Ok, Sir')
            gx_path = 'C://Users//Kabra//AppData//Local//Programs//Opera GX//launcher %s'
            webbrowser.get(gx_path).open_new_tab('https://open.spotify.com/collection/tracks')

        elif "play shield playlist" in query:
            speak('Ok, Sir')
            gx_path = 'C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s'
            webbrowser.get(gx_path).open_new_tab('https://open.spotify.com/show/1ia59VHpHGZARDqULINlx2')

        elif 'email' in query:
            get_email_info()
        elif 'what is the favorite show of mine?' in query:
            speak('Agents of shield')
            if 'I want to search it on google' in query:
                webbrowser.get('C:/Users/Kabra/AppData/Local/Programs/Opera GX/launcher.exe %s').open(
                    'https://www.google.com/search?client=opera-gx&q=agents+of+shield&sourceid=opera&ie=UTF-8&oe=UTF-8')
            elif 'I dont want to open' in query:
                speak('Ok')
        elif 'write a note' in query:
            speak('What should i write, sir')
            note = takeCommand()
            file = open('jarvis.txt.txt', 'w')
            speak('Sir, Should i include date and time')
            snfm = takeCommand()
            if 'yes' in snfm:
                strTime = datetime.datetime.now().strftime('% H:% M:% S')
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif 'show note' in query:
            speak('Showing Notes')
            file = open('jarvis.txt.txt', 'r')
            print(file.read())
            speak(file.read())
        elif 'Which is the most common website I open regularly' in query:
            speak('According to your history of browser, You open mostly youtube and codecademy on daily purposes.')
        elif 'Why did I made you Friday' in query:
            speak('You have made me to make your work easier...')
        elif "what's your name" in query:
            speak('My friends call me')
            speak(assname)
            print("My friends call me", assname)
        elif 'change name' in query:
            speak('What would you like to call me, Sir')
            assname = takeCommand()
            speak('Thanks for naming me')
        elif "what is the internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per second upload speed.")
            print(f"Sir we have {dl} bit per second downloading speed and {up} bit per second upload speed.")
        elif "what is the upload speed" in query:
            st = speedtest.Speedtest()
            up = st.upload()
            speak(f"Sir the upload speed is {up}")
            print(f"Sir the upload speed is {up}")
        elif "what is the download speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            speak(f"Sir the download speed is {dl}")
            print(f"Sir the download speed is {dl}")
        elif 'Fridya' in query:
            speak("Yes sir")

        elif 'I want to upload a photo on instagram' in query:
            def instagram_upload():
                bot = Bot
                bot.login(username="divya_the_dev", password="divyakabra12345")
                speak('which photo you want to upload')
        elif "do some calculations" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("So what do you want me to calculate")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)


                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                    }[op]


                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)


                speak("your result is ")
                speak(eval_binary_expr(*(my_string.split())))
                print((eval_binary_expr(*(my_string.split()))))

        elif 'Good morning' in query:
            speak('Good morning sir')
        elif 'Good afternoon' in query:
            speak("Good afternoon sir")