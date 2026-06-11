initial = 1
while True:
    Number = int(input("Введите число: "))

    if Number < 0:
        break

    if Number > 0:
        initial *= Number

print(initial)