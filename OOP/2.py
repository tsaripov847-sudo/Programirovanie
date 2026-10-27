class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10):
        self.name = name
        self.hp = hp
        self.dmg = dmg


Monst1 = input("Введите данные первого монстра: ").split()
Monst2 = input("Введите данные первого монстра: ").split()

m1 = Monster(Monst1[0], Monst1[1], Monst1[2])
m2 = Monster(Monst2[0], Monst2[1], Monst2[2])

print(f"Монстр: {m1.name} \n HP: {m1.hp} \n DMG: {m1.dmg}")
print(f"Монстр: {m2.name} \n HP: {m2.hp} \n DMG: {m2.dmg}")

