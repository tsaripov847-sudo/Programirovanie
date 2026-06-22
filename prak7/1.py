print ("✌️Система рейтинга продуктов✌️")

rating = int(input("Введите рейтинг продукта(1-10): "))

match rating:
    case 9 | 10:
        text = "Отличный"
        emoji = "😁"
        recommendation = "Рекомендую"
    case 7 | 8:
        text = "Хороший"
        emoji = "😊"
        recommendation ="Можно попробовать"
    case 4 | 5 | 6:
        text = "Средний"
        emoji = "😐"
        recommendation = "Можно попробовать"
    case 1 | 2 | 3:
        text = "Плохой"
        emoji = "😣"
        recommendation = "НЕ РЕКОМЕНДУЮ"
    case _:
        print("Не коректный ввод")


print("============================================================")
print(f"Рейтинг: {rating} → {text} продукт {emoji} {recommendation}")
print("============================================================")