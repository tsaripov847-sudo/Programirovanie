First_number = int(input("Введите первое число: "))

while True:
    Second_number = int(input("Введите второе число: "))
    if Second_number > First_number:
        break
    print("Ошибка введите заново второе число")

while True:
    Third_number = int(input("Введите третье число: "))
    if Third_number > Second_number:
        break
    print("Ошибка введите заново третье число")
print("Последовательность принята")