attempts = 0

while attempts < 3:
    password = input("Введите пароль: ")
    if password == "admin":
        print("Доступ разрешен")
        break
    attempts += 1
else:
    print("Вход заблокирован")
