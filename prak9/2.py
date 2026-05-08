name = input("Введите имя человека в очереди: ")
interval = 0
while name != "Александра":
    name = input("Введите имя человека в очереди: ")

while name != "Левон":
    interval = interval + 1
    name = input("Введите имя человека в очереди: ")

print(f"Количество людей в очереди {interval - 1}" )