from platform import python_branch
from time import sleep
import os
import webbrowser
def clear():
    if os.sys.platform == 'win32':
            os.system('cls')
    else:
        os.system('clear')
clear()
while True:
    browser = input(' 1: Anime \n 2: Wikipedia \n 3: Python \n 4: Instagram \n 5: Exit \n >>> ')
    if browser == '1':
        clear()
        webbrowser.open('https://v2.vost.pw/', new=2)
    if browser == '2':
        clear()
        webbrowser.open('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0', new=2)
    if browser == '3':
        clear()
        webbrowser.open('https://www.python.org/', new=2)
    if browser == '4':
        clear()
        webbrowser.open('https://www.instagram.com/marselle.naz/', new=2)
    if browser == '5':
        print('Пожалуйста подождите!')
        sleep(3)
        clear()
        break
    