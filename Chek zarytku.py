from time import sleep
import os
import psutil

def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
clear()
######################################
# pip install psutil <<< install the library
a = psutil.sensors_battery()
b = int(a.percent)

while True:
    percent = int(a.percent)
    print(f"Заряд батареи: {percent}%")
    for i in range(1,10):
        print(i,'seconds')
        sleep(1)
######################################
