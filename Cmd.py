import pyttsx3
import speech_recognition as sr

import webbrowser
import os
import smtplib
import datetime
import wikipedia 

from main  import speak
from main  import wishME
from main  import takeComamand

Master = "Pal"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

speak(text)
wishME()
takeComamand()

query = takeComamand()

# logic for executing basic tasks as per the query


    
if 'youtube' in query.lower():
     webbrowser.open("youtube.com")

    #cách 2: webbrowser google chrome:
    

elif 'facebook' in query.lower():
    webbrowser.open("facebook.com")    

elif 'notion' in query.lower():
    webbrowser.open("notion.so")
    
elif 'google' in query.lower():
    url = 'https://www.google.com.vn/?hl=vi'
    chrome_path = 'C:\Program Files\Google\Chrome\Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)