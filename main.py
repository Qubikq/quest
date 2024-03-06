import classes


Hero = None
while True:
    print(' Добро пожаловать в меню создания перосонажа! \n', 'Что вы хотите сделать?\n')
    print(' 1 - Создать персонажа \n', '2 - О персонаже \n', '3 - Редактор класса \n',
          '4 - Узнать информацию о персонаже \n', '9 - Выход \n')

    chose = int(input('Выберите действие: '))
    match chose:
        case 1:
            while True:
                print('Выберите класс для персонажа: \n 1. Воин \n 2. Маг \n 3. Лучник \n 9. Выход \n')
                chose = int(input('Выберите действие: '))
                match chose:
                    case 1:
                        Hero = classes.Warrior(input('Имя вашего персонажа: '), input('Возраст вашего персонажа: '))
                        break
                    case 2:
                        Hero = classes.Mage(input('Имя вашего персонажа: '), input('Возраст вашего персонажа: '))
                        break
                    case 3:
                        Hero = classes.Archer(input('Имя вашего персонажа: '), input('Возраст вашего персонажа: '))
                        break
                    case 9:
                        break

        case 2:
            print(
                f'Имя - {Hero.name} \n Возраст - {Hero.age} \n Оружие - {Hero.weapon} \n Класс - {Hero.spec_name} \n --------------------- \n Здоровье - {Hero.hp} \n Броня - {Hero.armor} \n Скорость - {Hero.speed} \n Урон - {Hero.damage} \n ')
        case 9:
            break
