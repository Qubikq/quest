class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class MeleeWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self):
        print(f'Вы бьете {self.name}ом на {self.damage} урона')


class MageWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self):
        print(f'Вы атакуете с помощью {self.name}а на {self.damage} урона')


class ArcherWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self):
        print(f'Вы стреляете с {self.name}а на {self.damage} урона')
