import pyttsx3
import speech_recognition as Sr
import webbrowser
from PIL import Image
import os
import datetime

Alice_M =  pyttsx3.init()
voice = Alice_M.getProperty('voices')# getProperty():lấy giọng 
Alice_M.setProperty('voice',voice[1].id) #SetProperty(): Chọn giọng 0: NAM, 1: NỮ

Master = "Master"
Alice_E = ""

def speak(audio):
    print('Alice: '+ audio)
    Alice_M.say(audio)
    Alice_M.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def Welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning"+ Master)
        
    elif hour>=12 and hour<18:
        speak("good afternoon " +  Master)
    else:
        speak("Good Evening" + Master)
    speak(" How may i help you? " + Master)

def Command():
    c = Sr.Recognizer()# Khởi tạo để nhận giọng nói 
    with Sr.Microphone() as source: #Giọng mình lấy từ đâu nguồn(source)
        c.pause_threshold = 1 # Nó sẽ dừng trong bao nhiêu giây trước khi nghe lệnh mới
        audio = c.listen(source)# Nghe cái nguồn cái nguoòn microphone
    try:
        query = c.recognize_google(audio, language = "EN") #truy vấn lệnh nhận nó gg
        print("Master : " + query) # print cái tên của mình ra
    except Sr.UnknownValueError: # nếu không nghe được
        print("Please repeat !!!")
        query= str(input('Your order is: '))# có thể gõ câu lệnh khi không nhận diện giọng nói
    return query 

if __name__ =="__main__":
    Welcome()
    while True:
        query = Command().lower()# lấy mệnh chuyển mệnh lệnh thành chữ không viết hoa để dễ nhận diện
        if 'google' in query.lower():
            speak("What should I search "+ Master)
            search=Command().lower() #để cho máy dễ nhận dạng
            url = f"https://www.google.com/search?q={search}"# cho nó vào thanh search của gg
            webbrowser.get().open(url) # để mở wed ra
            speak(f'Here is your {search} on google ') # nó tìm thấy cái gì
        if 'youtube' in query.lower():
            speak("What should I search "+ Master)
            search=Command().lower() #để cho máy dễ nhận dạng
            url = f"https://www.youtube.com/search?q={search}"# cho nó vào thanh search của ytb
            webbrowser.get().open(url) # để mở wed ra
            speak(f'Here is your {search} on youtube ') # nó tìm thấy cái gì
        elif 'image'in query.lower():
            me =r"D:\OLD_Windows\Pictures\Saved Pictures\me.jpg" #gọi link
            os.startfile(me) # chạy file
        elif 'time' in query:
            time()
        elif 'music' in query.lower():
            speak("What's the name of the song? "+ Master)
        elif 'record' in query.lower():
            speak("1 2 3 record," +Master)
            
        elif "bye" in query:
            speak("Bye Master")
            quit()

        