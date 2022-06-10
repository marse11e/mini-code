from random import choice
import os
from time import sleep
def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
class Product:
    def __init__(self, name, category, price) -> None:
        self.name = name
        self.category = category
        self.price = price

class Shelf:
    def __init__(self, number, capacity, products:list) -> None:
        self.number = number
        self.capacity = capacity
        self.products = products
    def check_capacity(self):
        if self.capacity < len(self.products):
            return 'Перегруз'
        else:
            return 'Всё ок'
    def get_products(self):
        prod1 = []
        for i in self.products:
            prod1.append(i.name)
        return prod1


class Magazin:
    def __init__(self, name1, shelfs:list) -> None:
        self.name1 = name1
        self.shelfs = shelfs

    def get_products_all(self):
        prod = []
        for i in self.shelfs:
            prod.extend(i.get_products())
        return prod

    def get_products_price(self):
        d = {}
        for i in self.shelfs:
            for j in i.products:
                d.update({
                    j.name: j.price
                })

        return d
    def get_all_price(self):
        c = []
        for i in self.shelfs:
            for j in i.products:
                c.append(j.price)
        return f'Общая стоимость: {sum(c)}'
    def get_categories(self):
        list1 = []
        
        for i in self.shelfs:
            for j in i.products:
                list1.append(j.category)
        set1 = set(list1)
        return set1


class User:
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money
        self.products = []
     
    def buy_product(self, shop):
        print(f'У Покупателя {self.name} - {self.money} сом')
        a = shop.get_products_price()
        b =  choice(shop.get_products_all())
        
        for i in shop.shelfs:
            for j in i.products:
                if j.name == b:
                    self.products.append(j)
        self.money -= a[b]

        return f'{self.name} купил , {b} за {a[b]} сом в {shop.name1}, у покупателя осталось {self.money}'

    def get_info(self):
        return f"""
        Пользователь с именем {self.name}
        Счет  {self.money}
        Продукты {[i.name for i in self.products]}
        """


p = Product('Кола', 'Напиток', 45)
p1 = Product('Сникерс', 'Шоколад', 50)
p2 = Product('Сендвич', 'Еда', 70)
p3 = Product('Винстон', 'Сигареты', 100)
p4 = Product('Чай', 'Напитки', 190)
p5 = Product('Самса', 'Еда', 55)
p6 = Product('Вино', 'Алкоголь', 400)
p7 = Product('Пельмени', 'Еда', 300)
p8 = Product('Вареники', 'Еда', 180)
p9 = Product('Хлеб', 'Выпечка', 20)


s = Shelf(1, 4, [p, p1, p2, p3])
s1 = Shelf(2, 3, [p4, p5, p6])
sh2 = Shelf(3,3, [p7, p8, p9])



m = Magazin('Гастроном', [s, s1, sh2])

def create_user(name, money):
    return User(name, money)



user = None
while True:
    if user is None:    
        print('Вы в новой игре зарегистритруйтесь')
    
    a = input("""
        1) Что ты зарегистрироватся введите
        2) Exit
        >>> """  )
    
    
    
    if a == '1':
        clear()
        print('Otkryvaem bazu ...')
        sleep(5)
        name = input('Введите Имя: ')
        money = int(input('Введите Количество денег: '))
        user = create_user(name, money)
        clear()
        print('Vypolnyaem registratciyu ...')
        sleep(5)
        while True:
            b = input("""
            1) Посмотреть все товары 
            2) Информация о пользователе
            3) Купить случайный продукт
            >>> """)

            if b == '1':
                print(", ".join(m.get_products_all()))

            elif b == '2':
                if user is not None:
                    print(user.get_info())
                else:
                    print('Зарегистрируйтесь!!')

            elif b == '3':
                if user is not None:
                    print(user.buy_product(m))
                else:
                    print('Зарегистрируйтесь!!')
                    sleep(3)
    if a == '2':
        print('Vyhod iz magazina ...')
        sleep(4)
        break
    if a == 'admin-endless':
        while True:
            b = input("""
            1) Посмотреть все товары 
            2) Информация о пользователе
            3) Купить случайный продукт
            >>> """)

            if b == '1':
                print(", ".join(m.get_products_all()))

            elif b == '2':
                if user is not None:
                    print(user.get_info())
                else:
                    print('Зарегистрируйтесь!!')

            elif b == '3':
                if user is not None:
                    print(user.buy_product(m))
                else:
                    print('Зарегистрируйтесь!!')
                    sleep(3)