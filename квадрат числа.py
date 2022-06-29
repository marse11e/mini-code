from time import sleep
import os
def clear():
    if os.sys.platform == 'win32':
            os.system('cls')
    else:
        os.system('clear')
clear()

a = lambda a: a * a
print('Подождите !')
sleep(5)
print(a(int(input('Ввдите число >>> '))))
# Функция, возвращающая квадрат любого числа