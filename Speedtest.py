import speedtest 
  
def speed():
    while True:
        s = speedtest.Speedtest() 
        option = input('''
        Выбери тип проверки:   

        1 - Скорость скачивания   
        2 - Скорость загрузки   
        3 - Пинг

        >>>: ''')
        

        if option == '1':   
            print(s.download())   
        elif option == '2':  
            print(s.upload())   
        elif option == '3':   
            servernames =[]   
            s.get_servers(servernames)   
            print(s.results.ping)     
        else: 
            print("Такой команды нет!")
speed()