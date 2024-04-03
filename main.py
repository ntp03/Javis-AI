import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

print("Initialing jarvis")


# Speak funtion will pronuonce the string which is passsed to it
Master = "Pal"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronouncr the string which is passed to it
def speak(text = ''): # do text là hàm Str nên cần nháy đơn '' để nhận diện Str
    engine.say(text)
    engine.runAndWait()


#speak("good boy")
    
# This function will wish you as per the current time
def wishME():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("good morning"+ Master)
        
    elif hour>=12 and hour<18:
        speak("good afternoon " +  Master)
    else:
        speak("Good Evening" + Master)
    speak(" i am Jarvi. How may i help you?")

#This funtion will take command from the microphone
def takeComamand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-US')
        print(f"user said:{query}\n")

    except Exception as e:
        print("say that again please")
        query = None

    return query
    

#Main progarm star here.
speak("Initialing jarvis...")
wishME()
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
    url = 'https://www.google.com'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' # lỗi do / phải là gạch / mới chịu
    webbrowser.get(chrome_path).open(url)
print("anything else?" + Master)
speak("anything else?" + Master)