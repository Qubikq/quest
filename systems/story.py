from random import randint

import main

hp = getattr(main.Hero, 'hp')


# Система истории и событий (общая)

def is_dead():
    if hp == 0:
        print('Вы умерли смертью храбрых...')


def random_event():
    variable = randint(1, 40)
    print(f' \n Вы упали и подвернули ногу, {main.Hero.name}"у больно! У вас отнимается {variable} здоровья')
    if main.Hero.hp - variable == 0:
        is_dead()
    else:
        main.Hero.hp -= variable
    print(f' \n Ваше здоровье - {main.Hero.hp}')
