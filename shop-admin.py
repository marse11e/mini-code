napitki = ['Kola']
vypechka = ['Bulka']
jivachka = ['Dirol']
syhofrukt = ['Ris']
frukty = ['Grusha']
ovoshi = ['Morkovka']
myaso = ['Govyadina']
while True:
    tovary = napitki,vypechka,jivachka,syhofrukt,frukty,ovoshi,myaso 
    table = int(input('\n1: Товары\n2: Добавить Товар\n3: Удалить товар\n4: Выход\n\[=-=]/: '))
    if table == 1:
        tovar = int(input('\n1: Напитки \n2: Выпечки \n3: Живачки \n4: Сухо-фрукты \n5: Фрукты \n6: Овощи \n7: Мясо \n8: Все товары\n\[-=-]/: '))
        if tovar == 1:
            print(napitki,"Всего",len(vypechka),"напиток")
        elif tovar == 2:[print(vypechka,"Всего",len(vypechka),"выпичек")]
        elif tovar == 3:[print(jivachka,"Всего",len(jivachka),"живачек")]
        elif tovar == 4:[print(syhofrukt,"Всего",len(syhofrukt),"сухо-фруктов")]
        elif tovar == 5:[print(frukty,"Всего",len(frukty),"фруктов")]
        elif tovar == 6:[print(ovoshi,"Всего",len(ovoshi),"овощей")]
        elif tovar == 7:[print(myaso,"Всего",len(myaso),"мяс")]
        else:[print('Убедитесь что ввели правильную команду!')]
    elif table == 2:
        tovar = int(input('\n1: Добавить напиток \n2: Добавить выпечку \n3: Добавить живачку \n4: Добавить сухо-фрукт \n5: Добавить фрукт \n6: Добавить овощь \n7: Добавить мясо \n\[-=-]/: '))
        if tovar == 1:
            add_tovar = input('Введите название напитка: ')
            napitki.append(add_tovar)
        elif tovar == 2:
            add_tovar = input('Введите название выпечки: ')
            vypechka.append(add_tovar)
        elif tovar == 3:
            add_tovar = input('Введите название живачки: ')
            jivachka.append(jivachka)
        elif tovar == 4:
            add_tovar = input('Введите название сухо-фрукта: ')
            syhofrukt.append(syhofrukt)
        elif tovar == 5:
            add_tovar = input('Введите название фрукта: ')
            frukty.append(frukty)
        elif tovar == 6:
            add_tovar = input('Введите название овоща: ')
            ovoshi.append(ovoshi)
        elif tovar == 7:
            add_tovar = input('Введите название мясы: ')
            myaso.append(myaso)
        else:[print('Убедитесь что ввели правильную команду!')]
    elif table == 3:
        print('Панель для удаление, удаленные данные не подлежать востоновлении')
        tovar = int(input('\n1: Удалить напиток \n2: Удалить выпечку \n3: Удалить живачку \n4: Удалить сухо-фрукт \n5: Удалить фрукт \n6: Удалить овощь \n7: Удалить мясо \n\[-=-]/: '))
        if tovar == 1:
            print(napitki),print(f"Убедитесь что вводите название правильно!")
            delete_tovar  = input('\nНазвание товара: ')
            napitki.remove(delete_tovar)
        elif tovar == 2:
            print(napitki),print("Убедитесь что вводите название правильно!")
            delete_tovar  = input('\nНазвание товара: ')
            vypechka.remove(delete_tovar)
        elif tovar == 3:
            print(napitki),print("Убедитесь что вводите название правильно!")
            delete_tovar  = input('\nНазвание товара: ')
            jivachka.remove(delete_tovar)
        elif tovar == 4:
            print(napitki),print("Убедитесь что вводите название правильно!")
            delete_tovar = input('\nНазвание товара: ')
            syhofrukt.remove(delete_tovar)
        elif tovar == 5:
            print(napitki),print("Убедитесь что вводите название правильно!")
            delete_tovar = input('\nНазвание товара: ')
            frukty.remove(delete_tovar)
        elif tovar == 6:
            print(napitki),print("Убедитесь что вводите название правильно!")
            delete_tovar = input('\nНазвание товара: ')
            ovoshi.remove(delete_tovar)
        elif tovar == 7:
            print(napitki),print("Убедитесь что вводите название правильно!")
            delete_tovar = input('\nНазвание товара: ')
            myaso.remove(delete_tovar)
        else:[print('Убедитесь что ввели правильную команду!')]
    elif table == 4:
        print('Вы вышли из панели админа')
        break
    else:[print('Убедитесь что ввели правильную команду!')]
