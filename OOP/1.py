class Monster:
    def __init__(self, name = "Неизвестная тварь", hp = 100, dmg = 100):
        self.name = name
        self.hp = hp
        self.dmg = dmg


m1 = Monster ("Дракула", 120, 35)
m2 = Monster ("Люкан", 100, 40)

print(f"Монстр: {m1.name} \n HP: {m1.hp} \n DMG: {m1.dmg}")
print(f"Монстр: {m2.name} \n HP: {m2.hp} \n DMG: {m2.dmg}")
