class Weapon:
    def __init__(self, name, damage, weight, slots):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.slots = slots


class MeleeWeapon(Weapon):
    def __init__(self, name, damage, weight, slots=3, weapon_range=2):
        super().__init__(name, damage, weight, slots)
        self.range = weapon_range

    def attack(self):
        print(f'Вы бьете {self.name}ом на {self.damage} урона')


class MageWeapon(Weapon):
    def __init__(self, name, damage, weight, slots=2, weapon_range=5):
        super().__init__(name, damage, weight, slots)
        self.range = weapon_range

    def attack(self):
        print(f'Вы атакуете с помощью {self.name}а на {self.damage} урона')


class ArcherWeapon(Weapon):
    def __init__(self, name, damage, weight, slots=2, weapon_range=8):
        super().__init__(name, damage, weight, slots)
        self.range = weapon_range

    def attack(self):
        print(f'Вы стреляете с {self.name}а на {self.damage} урона')