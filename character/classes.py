from weapon import weapon_bd
from random import randint


class MainCharacter:
    def __init__(self, name, age, level, strength, agility, intelligence, inventory, weapon_type, spec_name, hp, armor, speed, damage, skill1='Простой удар'):
        self.name = name
        self.age = age
        self.level = level
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.inventory = inventory
        self.weapon = weapon_type
        self.spec_name = spec_name
        self.hp = hp
        self.armor = armor
        self.speed = speed
        self.damage = damage
        self.skill1 = skill1

    def use_skill1(self):
        return randint(0, self.damage)


class Warrior(MainCharacter):

    def __init__(self, name, age, level=1, strength=5, agility=3, intelligence=1, inventory=10, weapon_type=weapon_bd.weapon_types[0].name, spec_name='Воин', hp=50,
                 armor=5, speed=10, damage=weapon_bd.weapon_types[0].damage):
        super().__init__(name, age, level, strength, agility, intelligence, inventory, weapon_type, spec_name, hp, armor, speed, damage)


class Mage(MainCharacter):

    def __init__(self, name, age, level=1, strength=2, agility=2, intelligence=5, inventory=10, weapon_type=weapon_bd.mage_weapon_types[0].name, spec_name='Маг', hp=30,
                 armor=2, speed=15, damage=weapon_bd.mage_weapon_types[0].damage):
        super().__init__(name, age, level, strength, agility, intelligence, inventory, weapon_type, spec_name, hp, armor, speed, damage)


class Archer(MainCharacter):

    def __init__(self, name, age, level=1, strength=2, agility=5, intelligence=2, inventory=10, weapon_type=weapon_bd.archer_weapon_types[0].name, spec_name='Лучник',
                 hp=35, armor=4, speed=23, damage=weapon_bd.archer_weapon_types[0].damage):
        super().__init__(name, age, level, strength, agility, intelligence, inventory, weapon_type, spec_name, hp, armor, speed, damage)


class Heroes(Warrior, Mage, Archer):
    @staticmethod
    def make_warrior(name, age):
        return Warrior(name, age)

    @staticmethod
    def make_mage(name, age):
        return Mage(name, age)

    @staticmethod
    def make_archer(name, age):
        return Mage(name, age)
