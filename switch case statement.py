def employee_details(ID):
    switcher = {
        "0001": "Имя сотрудника: MD. Merei",
        "0002": "Имя сотрудника: Bektur Kiri",  
        "0003": "Имя сотрудника: Marselle Naz",
    }
    return switcher.get(ID, "nothing")

ID = input("Введите ID сотрудника: ")
print(employee_details(ID))
