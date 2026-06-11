initial_sum = 0


while True:
    price = int(input("Введите цену товара(для остановки 0): "))

    if price == 0:
        print("Цикл остановлен ")
        break

    if price < 0:
        print("Ошибка цены")
        break
    initial_sum += price
if initial_sum > 1000:
    initial_sum = initial_sum * 0.9
    print(f"Сумма к оплате со скидкой 10%: {initial_sum} ")
else:
    print(f"Сумма к опалате: {initial_sum} ")

