marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
print("Список оценок", marks)
five =  0
couple = 0

for m in marks:
    if m == 5:
        five += 1
    elif m == 2:
        couple += 1


print(f"Количество пятерок: {five}")
print(f"Количество двоек: {couple}")