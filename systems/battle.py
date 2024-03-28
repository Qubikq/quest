from systems import locales

language = 'ru'
output = locales.output.referenece


def battle_enemy(player, enemy, player_action=0):
    output('battle', 'fight_start', language, player.name, enemy.name)
    while True:
        if enemy.hp <= 0:
            output('battle', 'enemy_dead', language, enemy.name)
            break
        if player.hp <= 0:
            output('battle', 'player_dead', language, player.name)
        if player_action == 1:
            current_damage = enemy.attack() - player.armor
            if current_damage <= 0:
                output('battle', 'enemy_attack_fail', language)
            else:
                player.hp -= current_damage
                output('battle', 'enemy_attack_success', language, enemy.name, enemy.damage)
            player_action = 0
            output('battle', 'player_hp_remain', language, player.name, player.hp)
        print(f'1 - {player.skill1}')
        chose = int(input('Выберите действие - '))
        match chose:
            case 1:
                player_action = 1
                player_damage = player.use_skill1() - enemy.armor
                if player_damage <= 0:
                    output('battle', 'player_attack_fail', language, player.name)
                else:
                    enemy.hp -= player_damage
                    output('battle', 'player_attack_success', language, player.name, player_damage)
                    if enemy.hp <= 0:
                        enemy.hp = 0
                    output('battle', 'enemy_hp_remain', language, enemy.name, enemy.hp)
