def battle_enemy(player, enemy, player_action=0):
    print(f'{player.name} вступает в бой с {enemy.name} \n')
    while True:
        if enemy.hp <= 0:
            print(f'{enemy.name} - поражен!')
            break
        if player_action == 1:
            current_damage = enemy.attack() - player.armor
            if current_damage <= 0:
                print('~Ваша броння сдерживает удар~')
            else:
                player.hp -= current_damage
                print(f'{enemy.name} наносит вам {enemy.damage} \n У вас осталось {player.hp} здоровья')
            print('\n ---------------------------------------------------------------------------------------------- \n')
            player_action = 0
        print(f'1 - {player.skill1}')
        chose = int(input('Выберите действие - '))
        match chose:
            case 1:
                player_action = 1
                player_damage = player.use_skill1() - enemy.armor
                if player_damage <= 0:
                    print('\n ---------------------------------------------------------------------------------------------- \n')
                    print(f'Вы не попадаете по {enemy.name}')
                else:
                    enemy.hp -= player_damage
                    print('\n ---------------------------------------------------------------------------------------------- \n')
                    print(f'Вы нанесли {enemy.name} - {player_damage} урона!')
                    if enemy.hp <= 0:
                        enemy.hp = 0
                    print(f'У {enemy.name} осталось {enemy.hp} здоровья')
                print('\n ---------------------------------------------------------------------------------------------- \n')
