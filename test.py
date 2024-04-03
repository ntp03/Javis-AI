#Khai báo thư viện
import pyttsx3
import speech_recognition as Sp
from datetime import datetime

#Khởi tạo 
Robot_M = pyttsx3.init()
Robot_E = Sp.Recognizer()
Robot_B = ''

# lời chào và kích hoạt
Master = "Master"
Robot_T = " Can I help you ,"
Robot_M.say(Robot_T + Master)
Robot_M.runAndWait() 

with Sp.Microphone() as mic:
    print("Robot: I'm Listening") 
    audio = Robot_E.listen(mic)
print("robot: ...")

try:
    you = Robot_E.recognize_google(audio)
except:
    you = ""
print("You:" + you )

# main
if you == "today":
    today = datetime.today()
    Robot_B = today.strftime("%B %d, %Y")
elif you == "time":
    now = datetime.now()
    Robot_B  = now.strftime("%H:%M:%S")
print("robot:" , Robot_B)


