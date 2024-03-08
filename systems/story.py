from random import randint

import main

Hero = __import__(main.Hero)

# Система истории и событий (общая)

def is_dead():
    if Hero.hp == 0:
        print('Вы умерли смертью храбрых...')


def random_event():
    variable = randint(1, 40)
    print(f' \n Вы упали и подвернули ногу, {Hero.name}"у больно! У вас отнимается {variable} здоровья')
    if Hero.hp - variable == 0:
        is_dead()
    else:
        Hero.hp -= variable
    print(f' \n Ваше здоровье - {Hero.hp}')
