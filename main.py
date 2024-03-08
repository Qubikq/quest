from character import classes
from random import randint
from systems import story

Hero = None


# Проверка на смерть
def is_dead():
    print('Вы умерли смертью храбрых...')
    Hero.hp = 0


# Случайное событие

def random_event():
    variable = randint(1, 40)
    if Hero.hp - variable <= 0:
        is_dead()
    else:
        print(f' \n Вы упали и подвернули ногу, {Hero.name}"у больно! У вас отнимается {variable} здоровья')
        Hero.hp -= variable
    print(f' \n Ваше здоровье - {Hero.hp}')
    return Hero.hp


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
            random_event()
        case 9:
            break
