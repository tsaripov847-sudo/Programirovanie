month_number = int(input("ВВедите номер месяца: "))

match month_number:
    case  12 | 1 | 2:
        season = "Зима"
        emoji = "❄️"
    case  3 | 4 | 5:
        season = "Весна"
        emoji = "🌿"
    case 6 | 7 | 8:
        season = "Лето"
        emoji = "☀️"
    case 9 | 10 | 11:
        season = "Осень"
        emoji = "🍂"
    case _:
        season = "Ошибка ввода"
        emoji = "❌"
print(f"Номер месяца №{month_number} - сезон {season} {emoji}")



