# Thư viện 
import pyttsx3
import speech_recognition as Sp
from datetime import datetime


# Khởi tạo
Robot_M = pyttsx3.init() #khởi tạo để nói
Robot_E = Sp.Recognizer()# Khởi tạo để nghe
Robot_B = ''



Master = "Master"
Robot_T = " Can I help you ,"
Robot_M.say(Robot_T + Master)
Robot_M.runAndWait() 


while True: # cho vô vòng lặp để có thể hỏi liên tục
 
    with Sp.Microphone() as mic: # tương đương nó sẽ bằng mic = Sp.Microphone()
        print("Robot: I'm Listening") # khi dùng with thì nó sẽ  khởi tạo cái mic bật cái mic lên để nghe lại 
        audio = Robot_E.listen(mic)#sau đấy khi đã nghe xong sẽ tăt mic đi
    print("robot: ...")
    try:#eror catching try except để tránh nhận lỗi nói linh ta linh tinh
        #runtime error lỗi sinh ra khi chạy
        #try khi mà nó chạy dòng "you = Robot_E.recognize_google(audio)" . Nếu nó có lỗi nó sẽ không báo cáo speech_recognition.exceptions.UnknownValueError mà..
        you = Robot_E.recognize_google(audio) #hàm được xây dựng bằng GG (tạo file âm thanh) (..., language = "ngôn ngữ ")
    except:# mà nó biến thành dòng này
        you = "" 

    print("You:" + you)

    #Main 
    if you == "today":
        today = datetime.today()
        Robot_B = today.strftime("%B %d, %Y")
    elif you == "time":
        now = datetime.now()
        Robot_B  = now.strftime("%H:%M:%S")
    elif you == "bye":
        Robot_B = "Bye, " + Master
        print("robot:" , Robot_B)
        Robot_M.say(Robot_B)
        Robot_M.runAndWait() 
        break

    print("robot:" , Robot_B)
    Robot_M.say(Robot_B)
    Robot_M.runAndWait() 
    