# from datetime import datetime
# now = datetime.now()
# dt_string = now.strftime("%H:%M:%S")
# print("date and time =", dt_string)

# import wikipedia
# value=input("Enter what u want to search")
# m=wikipedia.search(value,3)
# print(wikipedia.summary(m[0],sentences=2))

# from PIL import Image
# im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")  

import simpleaudio as sa

filename = 'myfile.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done() 