numbers = [10, 20, 30, 40, 50]
meaning = int(input("Введите число"))

for i in range(len(numbers)):
    if numbers[i] == meaning:
        print(i)
        break
else:
     print("Нет такого числа")

