maximum = 0


while True:
    numbers = int(input("Введите натуральное число: "))

    if numbers == 0:
        break

    if numbers >= maximum:
        maximum = numbers

if maximum > 0:
    print("Самое больщое число из тех что были введены: ", maximum)
else:
    print("Ничего не введено кроме нуля")




