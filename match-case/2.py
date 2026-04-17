num1 = float(input("Введите первое число(вещественное или целое): "))
num2 = float(input("Введите второе число(вещественное или целое): "))
operation = input("Введите операцию (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case "/":
        if num2 == 0:
           print ("Ошибка на ноль делить нельзя")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    case _:
        print("Ошибка ввода")


