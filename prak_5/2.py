ves, rost = map(float, input("Введите свой вес(кг) и рост(М): ").split())

imt = ves / (rost * rost)

print(f"Ваш ИМТ: {imt:.1f}")
