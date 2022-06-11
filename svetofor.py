from time import sleep
import os

def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
clear()

while True:
    print('RED | STOP | 15s')
    for i in range(1,16):
        print(i,'seconds')
        sleep(1)
    clear()
    print('YELLOW | WAIT... | 15s')
    for i in range(1,16):
        print(i,'seconds')
        sleep(1)
    clear()
    print('GREEN | START | 15s')
    for i in range(1,16):
        print(i,'seconds')
        sleep(1)
    clear()