import os
from pprint import pprint
import time
def clear():
        if os.sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
clear()

while True:
    a = input("Пожалуйста введите какое либо число для обредериние:\n>>> ")
    if a % 2:
        clear()
        print("Ваше число является четной")
    else:
        clear()
        print("Ваше число не четная!")
    