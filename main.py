from character import classes
from random import randint
from systems import battle
from enemy import enemies
import copy

Hero = None


# Удобный импорт из character.classes классов для персонажа
def hero(chos_hero=None):
    name_hero = input('Имя вашего персонажа: ')
    age_hero = int(input('Возраст вашего персонажа: '))
    return getattr(classes.Heroes, chos_hero)(name=name_hero, age=age_hero)


while True:
    print(' Добро пожаловать в меню создания перосонажа! \n', 'Что вы хотите сделать?\n')
    print(' 1 - Создать персонажа \n', '2 - О персонаже \n', '3 - Махаться \n',
          '4 - Узнать информацию о персонаже \n', '9 - Выход \n')

    chose = int(input('Выберите действие: '))
    match chose:
        case 1:
            while True:

                print('Выберите класс для персонажа: \n 1. Воин \n 2. Маг \n 3. Лучник \n 9. Выход \n')
                chose = int(input('Выберите действие: '))
                match chose:
                    case 1:
                        Hero = hero('make_warrior')
                        break
                    case 2:
                        Hero = hero('make_mage')
                        break
                    case 3:
                        Hero = hero('make_archer')
                        break
                    case 9:
                        break

        case 2:
            print(
                f'\n Имя - {Hero.name} \n Возраст - {Hero.age} \n Оружие - {Hero.weapon} \n Класс - {Hero.spec_name} \n --------------------- \n Здоровье - {Hero.hp} \n Броня - {Hero.armor} \n Скорость - {Hero.speed} \n Урон - {Hero.damage} \n ')
        case 3:
            battle.battle_enemy(Hero, copy.copy(enemies.Goblins[randint(0, 2)]))
        case 9:
            break
