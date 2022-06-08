from time import sleep
import os
def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
vetrina = ['Coca cola','Fanta','Sprite','Coffe','Tea']
while True:
    a = int(input('1: Posmotret polku \n2: Dobavit v polku tovar \n>>> '))
    if a == 1:
        clear()
        print(vetrina)
    if a == 2:
        name_tovar = input("""VEDITE NAZVANIE TOVARA \n >>> """)
        vetrina.append(name_tovar)
        print('PODOJDITE 5s')
        sleep(5)
        clear()
        print('TOVAR DOBAVLEN')
    