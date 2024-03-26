import random


class SimpleEnemy:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self):
        return random.randint(1, self.damage)

    def take_damage(self, damage):
        self.hp -= max(0, damage - self.armor)


Goblin = SimpleEnemy('Гоблин', 10, 2, 1)
GoblinRogue = SimpleEnemy('Гоблин-разбойник', 14, 3, 2)
GoblinWarrior = SimpleEnemy('Гоблин-разбойник', 20, 5, 4)
Goblins = [Goblin, GoblinRogue, GoblinWarrior]
