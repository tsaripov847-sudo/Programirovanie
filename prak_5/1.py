TAX_RATE = 0.13

annual_income = int(input("Введите свой годовой доход: "))

tax = annual_income * TAX_RATE
tax_deduction = annual_income - tax

print(f"Общая сумма дохода {annual_income:.2f} руб.")
print(f"Сумма рассчитанного налога {tax:.2f} руб.")
print(f"Сумма «на руки» после вычета налога {tax_deduction:.2f} руб.")
