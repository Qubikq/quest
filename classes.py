import weapon.weapon_bd


class MainCharacter:
    def __init__(self, name, age, weapon_type, spec_name, hp, armor, speed, damage):
        self.name = name
        self.age = age
        self.weapon = weapon_type
        self.spec_name = spec_name
        self.hp = hp
        self.armor = armor
        self.speed = speed
        self.damage = damage


class Warrior(MainCharacter):

    def __init__(self, name, age, weapon_type=weapon.weapon_bd.weapon_types[0].name, spec_name='Воин', hp=50, armor=5, speed=10, damage=weapon.weapon_bd.weapon_types[0].damage):
        super().__init__(name, age, weapon_type, spec_name, hp, armor, speed, damage)


class Mage(MainCharacter):

    def __init__(self, name, age, weapon_type=weapon.weapon_bd.mage_weapon_types[0].name, spec_name='Маг', hp=30, armor=2, speed=15, damage=weapon.weapon_bd.mage_weapon_types[0].damage):
        super().__init__(name, age, weapon_type, spec_name, hp, armor, speed, damage)


class Archer(MainCharacter):

    def __init__(self, name, age, weapon_type=weapon.weapon_bd.archer_weapon_types[0].name, spec_name='Лучник', hp=35, armor=4, speed=23, damage=weapon.weapon_bd.archer_weapon_types[0].damage):
        super().__init__(name, age, weapon_type, spec_name, hp, armor, speed, damage)


