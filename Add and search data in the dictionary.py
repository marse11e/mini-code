#Добавлять и искать данные в словаре



# Определение словаря
customers = {'06753':'Mehzabin Afroze','02457':'Md. Ali',
'02834':'Mosarof Ahmed','05623':'Mila Hasan', '07895':'Yaqub Ali'}

# Добавьте новые данные
customers['05634'] = 'Mehboba Ferdous'

print("The customer names are:")
# Выведите значения из словаря
for customer in customers:
    print(customers[customer])

# Возьмите идентификатор клиента в качестве входных данных для поиска
name = input("Enter customer ID:")

# Найдите идентификатор в словаре
for customer in customers:
    if customer == name:
        print(customers[customer])
        break
