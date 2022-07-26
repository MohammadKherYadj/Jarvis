import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get
import requests
import random
import wikipedia
import webbrowser
import sys
import pyjoke
import pyautogui
import time

sir = 'sir'
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


# text to speech

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


# to convert voice into text

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f'user said:{query}')
    except Exception:
        speak('say that again please')
        return 'none'
    return query


# get location

def get_location():
    r = requests.get('https://get.geojs.io/')
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ipAdd = ip_request.json()['ip']
    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    speak('i am not sure sir, but i think we are in ' + geo_data['country'])


# to wish

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        speak(f'good morning , its {tt}')
    elif hour > 12 and hour < 18:
        speak(f'good afternoon {sir}, its {tt}')
    else:
        speak(f'good evening {sir},its {tt}')
    speak('how can i help you')


def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dfa2b2dfdbbd4f3ca53f955bcc853644'
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f'today‘s {day[i]} news is : {head[i]}')


if __name__ == '__main__':
    wish()
    while True:
        if 1:
            try:
                # query = input('').lower()
                query = take_command().lower()
            except Exception:
                query = ''

            # logic building for task

            # open notepad

            if 'open' in query and 'notepad' in query:
                npath = 'C:\\Windows\\System32\\notepad.exe'
                os.startfile(npath)

            # close notepad

            elif 'close' in query and 'notepad' in query:
                speak(f'okay {sir}, closing notepad...')
                os.system('taskkill /f /im notepad.exe')

            # open adobe reader

            elif 'open' in query and 'adobe reader' in query:
                apath = 'C:\\Program Files (x86)\\Adobe\\Reader 10.0\\Reader\\AcroRd32.exe'
                os.startfile(apath)

            # close adobe reader

            elif 'close' in query and 'adobe reader' in query:
                speak(f'okay {sir}, closing adobe reader...')
                os.system('taskkill /f /im AcroRd32.exe')

            # open cmd

            elif ('open' in query and 'command prompt' in query) or ('open' in query and 'cmd' in query):
                os.system('start cmd')

            # close cmd

            elif ('close' in query and 'command prompt' in query) or ('close' in query and 'cmd' in query):
                speak(f'okay {sir}, closing command prompt...')
                os.system('taskkill /f / im cmd.exe')

            # open word

            elif 'open' in query and 'word' in query:
                wpath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe'
                os.startfile(wpath)

            # close word

            elif 'close' in query and 'word' in query:
                speak(f'okay {sir}, closing word')
                os.system('taskkill /f /im WINWORD.exe')

            # open excel

            elif 'open' in query and 'excel' in query:
                epath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.exe'
                os.startfile(epath)

            # close excel

            elif 'close' in query and 'excel' in query:
                speak(f'okay {sir}, closing excel')
                os.system('taskkill /f /im EXCEL.exe')

            # open power point

            elif 'open' in query and 'power point' in query:
                ppath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe'
                os.startfile(ppath)

            # close power point

            elif 'close' in query and 'power point' in query:
                speak(f'okay {sir}, closing power point')
                os.system('taskkill /f /im POWERPNT.exe')

            # open access

            elif 'open' in query and 'access' in query:
                apath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ACCICONS.exe'
                os.startfile(apath)

            # close access

            elif 'close' in query and 'access' in query:
                speak(f'okay {sir}, closing access')
                os.system('taskkill /f /im ACCICONS.exe')

            # open control panel

            elif 'open' in query and 'control panel' in query:
                cpath = 'C:\\Windows\\System32\\control.exe'
                os.startfile(cpath)

            # close control panel

            # elif 'close' in query and 'control panel' in query:
            #     speak(f'okay {sir}, closing control panel')
            #     os.system('taskkill /f /im explorer.exe')

            # open internet download manager

            elif 'open' in query and 'internet download manager' in query:
                ipath = 'C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe'
                os.startfile(ipath)

            # close internet download manger

            elif 'close' in query and 'internet download manager' in query:
                speak(f'okay {sir}, closing internet download manger')
                os.system('taskkill /f /im IDMan.exe')

            # opne by click downloader

            elif 'open' in query and 'by click downloader' in query:
                bpath = 'C:\\Program Files (x86)\\By Click Downloader\\ByClickDownloader.exe'
                os.startfile(bpath)

            # close by click downloader

            elif 'close' in query and 'by click downloader' in query:
                speak(f'okay {sir}, closing by click downloader')
                os.system('taskkill /f /im ByClickDownloader.exe')

            # open unity

            elif 'open' in query and 'unity' in query:
                upath = 'C:\\Program Files\\Unity\\Editor\\Unity.exe'
                os.startfile(upath)

            # unity

            elif 'close' in query and 'unity' in query:
                speak(f'okay {sir}, closing unity')
                os.system('taskkill /f /im Unity.exe')

            # open visual studio

            elif 'open' in query and 'visual studio' in query:
                vpath = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Enterprise\\Common7\\IDE\\devenv.exe'
                os.startfile(vpath)

            # close visual studio

            elif 'close' in query and 'visual studio' in query:
                speak(f'okay {sir}, closing visual studio')
                os.system('taskkill /f /im devenv.exe')

            # open pycharm

            elif 'open' in query and 'pycharm' in query:
                ppath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.4\\bin\\pycharm64.exe'
                os.startfile(ppath)

            # close pycharm

            elif 'close' in query and 'pycharm' in query:
                speak(f'okay {sir}, closing pycharm')
                os.system('taskkill /f /im pycharm64.exe')

            # open camtasia

            elif 'open' in query and 'camtasia' in query:
                cpath = 'C:\\Program Files\\TechSmith\\Camtasia 2021\\CamtasiaStudio.exe'
                try:
                    os.startfile(cpath)
                except Exception:
                    speak('camtasia not installed')

            # close camtasia

            elif 'close' in query and 'camtasia' in query:
                speak(f'okay {sir}, closing camtasia')
                os.system('taskkill /f /im CamtasiaStudio.exe')

            # open psiphone

            elif 'open' in query and 'psiphone' in query:
                ppath = 'D:\\Mohammad\\Programs\\VPN\\psiphon-162.exe'
                os.startfile(ppath)

            # close psiphone

            elif 'close' in query and 'psiphone' in query:
                speak(f'okay {sir}, closing psiphone')
                os.system('taskkill /im psiphon-162.exe')

            # open adobe photoshop

            elif 'open' in query and 'photoshop' in query:
                apath = 'C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe'
                try:
                    os.startfile(apath)
                except Exception:
                    speak('photoshop not found')

            # close adobe photoshop

            elif 'close' in query and 'photoshop' in query:
                speak(f'okay {sir}, closing adobe photoshop')
                os.system('taskkill /f /im Photoshop.exe')

            # open calculator

            elif 'open' in query and 'calculator' in query:
                cpath = 'C:\\Windows\\System32\\calc.exe'
                os.startfile(cpath)

            # close calculator

            elif 'close' in query and 'calculator' in query:
                speak(f'okay {sir}, closing calculator')
                os.system('taskkill /f /im calculator.exe')

            # open task manager

            elif 'open' in query and 'task manager' in query:
                tpath = 'C:\\Windows\\system32\\Taskmgr.exe'
                os.startfile(tpath)

            # close task manager

            # elif 'close' in query and 'task manager' in query:
            #     speak('okay sir, closing calculator')
            #     os.system('taskkill /f /im Taskmgr.exe')

            # play music

            elif 'play' in query and 'music' in query:
                music_dir = 'D:\\Mohammad\\Music\\مشكل'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            # close music

            # get ip address

            elif 'ip address' in query:
                ip = get('http://api.ipify.org').text
                speak(f'your ip address is {ip}')

            # search in wikipedia

            elif 'search in' in query and 'wikipedia' in query:
                speak('what do you want to look for ?')
                try:
                    search = take_command().lower()
                    speak('searching wikipedia...')
                    results = wikipedia.summary(search, sentences=2)
                    speak('according to wikipedia')
                    speak(results)
                except Exception:
                    speak('try again')

            # open youtube history

            elif 'open' in query and 'youtube history' in query:
                webbrowser.open('https://www.youtube.com/feed/history')

            # open youtube

            elif 'open' in query and 'youtube' in query:
                webbrowser.open('http://www.youtube.com')

            # search in youtube

            elif 'search in' in query and 'youtube' in query:
                try:
                    speak('what do you want to look for ?')
                    cm = take_command().lower()
                    webbrowser.open(f'https://www.youtube.com/results?search_query={cm}')
                except Exception:
                    speak('try again')

            # search in google

            elif 'search in' in query and 'google' in query:
                try:
                    speak('what do you want to look for ?')
                    cm = take_command().lower()
                    webbrowser.open(f'www.google.com/search?q={cm}')
                except Exception:
                    speak('try again')
            # open facebook

            elif 'open' in query and 'facebook' in query:
                webbrowser.open('www.facebook.com')

            # open gmail

            elif 'open' in query and 'gmail' in query:
                webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

            # open instgram

            elif 'open' in query and 'instagram' in query:
                webbrowser.open('www.instagram.com')

            # open stack over flow

            elif 'open' in query and 'stackoverflow' in query:
                webbrowser.open('www.stackoverflow.com')

            # open Egy best

            elif 'open' in query and 'eyg best' in query:
                webbrowser.open('www.egybest.com')

            # search in egy best

            elif 'search in' in query and 'egy best' in query:
                try:
                    speak('what do you want to look for ?')
                    cm = take_command().lower()
                    webbrowser.open(f'https://hola.egybest.co/movie/{cm}/')
                except Exception:
                    speak('try again')
            # to stop

            elif 'that‘s enough' in query:
                speak('have a good day')
                sys.exit()

            # set alarm

            elif 'set alarm' in query:
                nn = int(datetime.datetime.now().hour)
                if nn == 12:
                    music_dir = 'D:\\Mohammad\\Music\\مشكل'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            # tell me a joke

            elif 'tell me a joke' in query:
                joke = pyjoke.get_joke()
                speak(joke)

            # shutdown the computer

            elif 'shut down the system' in query:
                speak('the system is shuting down')
                os.system('shutdown /s /t /s')

            # restart the computer

            elif 'restart the system' in query:
                speak('the system is restarting')
                os.system('shutdown /r /t /s')

            # sleep the computer

            elif 'sleep the system' in query:
                speak('the system is sleeping')
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

            # switch the window (alt + tab)

            elif 'switch the window' in query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')

            # the the most important news in the day

            elif 'tell me news' in query:
                speak(f'please wait {sir}, fetching the last news')
                news()

            # to get me location

            elif ('where' in query and 'am i' in query) or ('what' in query and 'my location' in query):
                get_location()
            elif 'what' in query and 'time' in query:
                speak(f'it is {time.strftime("%I:%M %p")}')
            elif 'take' in query and 'screenshot' in query:
                speak(f'{sir}, please tell me the name for this screenshot file')
                name = take_command().lower()
                speak(f'please {sir} hold the screen for few seconds, i am taking screenshot')
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f'{name}.png')
                speak(f'i am done {sir}, the screenshot is saved in our main folder')
            elif 'hide' in query and ('files' in query or 'folder' in query):
                os.system('attrib +h /h /s /d')
                speak('sir, all the files in this folder are now hidden')
            elif 'visable' in query and ('files' in query or 'folder' in query):
                os.system('attrib -h /s /d')
                speak('sir, all the files in this folder are visible for everyone')
