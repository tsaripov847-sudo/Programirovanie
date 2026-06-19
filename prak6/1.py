NORMAL_TEMP_MIN = 36
NORMAL_TEMP_MAX = 37

NORMAL_PRESSURE_MIN = 110
NORMAL_PRESSURE_MAX = 130

NORMAL_PULSE_MIN = 60
NORMAL_PULSE_MAX = 100

temp = float(input("Введите температуру тела: "))
pressure  = int(input("Введите ваше давление: "))
pulse = int(input("Введите ваш пульс: "))

if temp < 35 or temp > 38 or pressure < 105 or pressure > 140 or pulse < 55 or pulse > 110:
    print("Состояние: Требуется врач")
elif NORMAL_TEMP_MIN <= temp <= NORMAL_TEMP_MAX and NORMAL_PRESSURE_MIN <= pressure <= NORMAL_PRESSURE_MAX  and NORMAL_PULSE_MIN <= pulse <= NORMAL_PULSE_MAX:
    print("Состояние: Нормальное")
else:
    print("Состояние: Легкое недомогание")


