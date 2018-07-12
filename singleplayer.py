from shell import *
from core import *
from random import *
from time import sleep


def player_name():
    print('What is your name hero? ')
    response = input('>>> ')
    return response


def make_enemy_name(names):
    shuffle(names)
    return names.pop()


def player_enemy():
    class_type = randrange(1, 7)
    if class_type == 1:  #warrior
        return new_gladiator(100, 30, 10, 20, 0, 2)
    elif class_type == 2:  #king
        return new_gladiator(120, 50, 8, 16, 0, 4)
    elif class_type == 3:  #Common Man
        return new_gladiator(70, 0, 3, 6, 0, 3)
    elif class_type == 4:  #healer
        return new_gladiator(100, 0, 6, 15, 15, 1)
    elif class_type == 5:  #Thief
        return new_gladiator(100, 0, 7, 18, 15, 5)
    elif class_type == 6:  # Vampire
        return new_gladiator(100, 15, 8, 17, 15, 6)


def player_battle(name, hero, enemy, enemy_name):
    while True:
        player_stats(hero, enemy, name, enemy_name)
        print_moves()
        response = input(
            'What would you like to do {}?\nPlease use 1 - 5 to answer >>> '.
            format(name))
        print_moves()
        if response == '1':
            print("{} uses an attack".format(name))
            print("END OF TURN\n")
            return attack(hero, enemy)
        elif response == '2':
            if hero['Power'] >= 10:
                print("{} has healed themself".format(name))
                print('END OF TURN\n')
                return heal(hero)
            else:
                print('Not enough power')
        elif response == '4':
            print('Wow you just let your enemy win')
            exit()
        elif response == '3':
            print("{} has skipped their turn".format(name))
            print('END OF TURN')
            hero['Rage'] = hero['Rage'] + 30
            hero['Power'] += 30
            return None
        elif response == '5':
            if hero['Power'] > 44:
                print('{} used their special attack'.format(name))
                print('END OF TURN\n')
                return special_move(hero, enemy)
            else:
                print('Not enough power')

        else:
            print('Invalid number input.')


def enemy_battle(enemy_name, enemy, hero):
    print('{} is thinking.'.format(enemy_name))
    while True:
        sleep(.300)
        print('.', '.', '.')
        response = choice([1, 1, 1, 2, 2, 3, 5])
        if response == 1:
            print("{} uses an attack".format(enemy_name))
            print('END OF TURN\n')
            return attack(enemy, hero)
        elif response == 2:
            if enemy['Power'] >= 10:
                print("{} has healed themself".format(enemy_name))
                print('END OF TURN\n')
                return heal(enemy)
            else:
                print('Not enough power')
        elif response == 3:
            print("{} has skipped their turn".format(enemy_name))
            print('END OF TURN\n')
            enemy['Rage'] = enemy['Rage'] + 30
            enemy['Power'] += 30
            return None
        elif response == 5:
            if enemy['Power'] > 44:
                print('{} used their special attack'.format(enemy_name))
                print('END OF TURN\n')
                return special_move(hero, enemy)
            else:
                print('Not enough power')
        print()


def game_winner(hero, name, names):
    enemy_name = make_enemy_name(names)
    enemy = player_enemy()
    while True:
        if is_dead(hero) == False and is_dead(enemy) == False:
            player_battle(name, hero, enemy, enemy_name)
            if is_dead(hero) == True:
                player_stats(hero, enemy, name, enemy_name)
                print("{} wins!".format(enemy_name))
                break
            elif is_dead(enemy) == True:
                player_stats(hero, enemy, name, enemy_name)
                print("{} wins!".format(name))
                return next_round(hero, name, names)
            enemy_battle(enemy_name, enemy, hero)
            if is_dead(hero) == True:
                player_stats(hero, enemy, name, enemy_name)
                print("{} wins!".format(enemy_name))
                break
            elif is_dead(enemy) == True:
                player_stats(hero, enemy, name, enemy_name)
                print("{} wins!".format(name))
                return next_round(hero, name, names)
        else:
            victor()


def next_round(hero, name, names):
    if len(names) > 0:
        print('You advance to the next boss')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print()
        return game_winner(hero, name, names)
    else:
        print('You have beaten all the bosses')


def main():
    names = [
        'Ching Ching', 'Ricky Bobby the Destroyer', 'Lil Wayne',
        'Single Pringle', 'Saint Nick', 'Barbie'
    ]
    name = player_name()
    hero = pick_class()
    game_winner(hero, name, names)


if __name__ == '__main__':
    main()
