import pyttsx3

engine = pyttsx3.init()
engine.save_to_file('I love you so much, My 300000000' , 'test.mp3') # save to mp3
engine.runAndWait()