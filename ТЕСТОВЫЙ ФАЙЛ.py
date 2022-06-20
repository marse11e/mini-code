from time import sleep
print('1 %')
while True:
    for i in range(2,101):
        sleep(10)
        print(i,'%')
        if i == 100:
            print('У вас сто процентов!')
        