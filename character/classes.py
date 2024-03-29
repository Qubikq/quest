from weapon import weapon_bd
from random import randint
from systems import locales
output = locales.localization
output_s = locales.filter_sort.rename
language = locales.language


class MainCharacter:
    def __init__(self, name, weapon_type, spec_name, strength, agility, intelligence, damage, precision=10, level=1, expirience=0,
                 inventory=10, hp=10, armor=0, initiation=5):
        self.name = name
        self.weapon_type = weapon_type
        self.spec_name = spec_name
        self.level = level
        self.expirience = expirience
        self.inventory = inventory
        self.hp = hp + strength * 2
        self.armor = armor + agility * 2
        self.initiation = initiation + intelligence * 2
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.damage = damage
        self.precision = precision


class Warrior(MainCharacter):

    def __init__(self, name, strength=5, agility=3, intelligence=2, weapon_type=weapon_bd.weapon_types[0].name,
                 spec_name=output['specialization']['warrior'][language],
                 damage=weapon_bd.weapon_types[0].damage,
                 skill1=output_s('skills', 'warrior_skill_1', language, weapon_bd.weapon_types[0].name),
                 skill2=output_s('skills', 'warrior_skill_2', language, weapon_bd.weapon_types[0].name)):
        super().__init__(name, weapon_type, spec_name, strength, agility, intelligence, damage)
        self.skill1 = skill1
        self.skill2 = skill2

    def use_skill1(self):
        return randint(1, self.damage)

    def use_skill2(self):
        return self.damage + self.strength


class Mage(MainCharacter):

    def __init__(self, name, strength=5, agility=3, intelligence=2, weapon_type=weapon_bd.weapon_types[0].name,
                 spec_name=output['specialization']['mage'][language], damage=weapon_bd.weapon_types[0].damage, skill1='Простой удар',
                 skill2='Сильный удар'):
        super().__init__(name, weapon_type, spec_name, strength, agility, intelligence, damage)
        self.skill1 = skill1
        self.skill2 = skill2

    def use_skill1(self):
        return randint(1, self.damage)

    def use_skill2(self):
        return self.damage + self.intelligence


class Archer(MainCharacter):

    def __init__(self, name, strength=5, agility=3, intelligence=2, weapon_type=weapon_bd.weapon_types[0].name,
                 spec_name=output['specialization']['archer'][language], damage=weapon_bd.weapon_types[0].damage, skill1='Простой удар',
                 skill2='Сильный удар'):
        super().__init__(name, weapon_type, spec_name, strength, agility, intelligence, damage)
        self.skill1 = skill1
        self.skill2 = skill2

    def use_skill1(self):
        return randint(1, self.damage)

    def use_skill2(self):
        return self.damage + self.intelligence


class Heroes(Warrior, Mage, Archer):
    @staticmethod
    def make_warrior(name):
        return Warrior(name)

    @staticmethod
    def make_mage(name):
        return Mage(name)

    @staticmethod
    def make_archer(name):
        return Mage(name)
