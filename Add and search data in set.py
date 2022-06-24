# Добавить и найти данные в наборе


# Определяем набор
numbers = {23, 90, 56, 78, 12, 34, 67}
 
# Добавляем новые
numbers.add(50)
# Вывести заданные значения
print(numbers)

message = "Число не найдено"

# Принять числовое значение для поиска
search_number = int(input("Введите число:"))
# Поиск числа в наборе
for val in numbers:
    if val == search_number:
        message = "Число найдено"
        break

print(message)
