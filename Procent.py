from time import sleep
import os
def clear():
    if os.sys.platform == 'win32':
            os.system('cls')
    else:
        os.system('clear')

clear()
procent = 100 
print('U vas',procent,'% zaryadki')
while True:
    sleep(10)
    procent -= 1
    clear()
    print('U vas',procent,'%')
    
    if procent == 20:
        print('U vas',procent,'% zaryadki vklyuchaem energosberejenie')
        sleep(20)
    if procent == 1:
        print('OTKLYUCHENIE')
        break