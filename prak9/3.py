num = int(input("Введите цену за услугу ведьмака: "))
i = 0

while  num >= 25:
    num -= 25
    i += 1
while num >= 10 :
    num -= 10
    i += 1
while num >= 5 :
    num -= 5
    i += 1
while num >= 1 :
    num -= 1
    i += 1

print(f"Количество чеканных монет для оплаты {i}")
