print("================"
      "✈️СТАТУС ЗАКАЗА✈️"
      "================")
status = input("Введите статус заказа(pending, processing, shipped, delivered, cancelled): ")
match status:
    case "pending":
        rus_status = "В ожидании"
        description = "Ваш заказа принят и находится в ожидании"
        emoji = "⏰"
        time = "До 1 дня"
    case "processing":
        rus_status = "В обработке"
        description = "Ваш заказ в обработке готовится к отправке"
        emoji = "📦"
        time = "1 - 2 дня"
    case "shipped":
        rus_status = "Отправлен"
        description = "Ваш заказ отправлен и едет к вам"
        emoji = "🚗"
        time = "2 - 7 дней"
    case "delivered":
        rus_status = "Доставлен"
        description = "Ваш заказ доставлен"
        emoji = "✅"
        time = "Доставка завершена"
    case "cancelled":
        rus_status = "Отменён"
        description = "Ваш заказ был отменён"
        emoji = "❌"
        time = "Нет"
    case _:
        print("Неверный статус заказа!")


print(f"Статус: {rus_status}")
print(f"Описание: {emoji} {description}")
print(f"Время ожидания: {time}")
print("===================================================")