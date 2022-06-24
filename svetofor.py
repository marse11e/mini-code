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
    print('YELLOW | WAIT... | 5s')
    for i in range(1,6):
        print(i,'seconds')
        sleep(1)
    clear()
    print('GREEN | START | 15s')
    for i in range(1,16):
        print(i,'seconds')
        sleep(1)
    clear()



# while True:
#     for i in range(1,31):
#         sleep(1)
#         clear()
#         print(f'''START \n red''',i)
#         if i==30:
#             clear()
#             for j in range(1,6):
#                 sleep(1)
#                 clear()
#                 print('yeallow',j)
#                 if j==5:
#                     clear()
#                     for a in range(1,31):
#                         sleep(1)
#                         clear()
#                         print('green',a)
#                         if a == 30:
#                             clear()
#                             for h in range(1,6):
#                                 sleep(1)
#                                 clear()
#                                 print('yeallow',h)



# def red():
#     a = 0
#     for i in range(1,31):
#         a += 1
#         print('red',a)
#         sleep(1)
#         clear()

# def yeallow():
#     a = 0
#     for i in range(1,6):
#         a += 1
#         print('yeallow',a)
#         sleep(1)
#         clear()
        
# def green():
#     a = 0
#     for i in range(1,31):
#         a += 1
#         print('green',a)
#         sleep(1)
#         clear()

# def injector():
#     print('Svetofor 2022 new modern siti Bishkek')
#     while True:
#         red()
#         clear()
#         yeallow()
#         clear()
#         green()
#         clear()
#         yeallow()
#         clear()
# injector()
