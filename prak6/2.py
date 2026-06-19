karman = int(input("Введите номер кармана: "))

if not 0 <= karman <= 36:
    print("Ошибка ввода")
elif karman == 0:
    print("Зеленый")
elif 1 <= karman <= 10 or 19 <= karman <= 28:
    if karman % 2:
        print("Красный")
    else:
        print("Черный")
else:
    if karman % 2:
        print("Черный")
    else:
        print("Красный")
