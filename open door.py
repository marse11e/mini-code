from re import T
from time import sleep

while True:
    for i in range(1,24):
        
        if i == 1:
            print('00:00','Магазин закрыт!')
        if i == 8:
            print('08:00','Магазин открылся!')
            
        # Так же с закрытием делать