from core import *


def name():
    name = input('What is the name of player one? >>> ')
    return name


def name_of_next():
    name = input('What is the name of player two? >>> ')
    return name


def print_moves():
    print('1.Attack\n2.Heal\n3.Quit\n')


def player_one_fight(name_1, name_2):
    while True:
        response = input(
            'What would you like to do {}? Please use 1,2, or 3 to answer.'.
            format('Player One'))
        print_moves()
        if response == '1':
            return attack(name_1, name_2)
        elif response == '2':
            return heal(name_1)
        elif response == '3':
            break


def player_two_fight(name_1, name_2):
    while True:
        response = input(
            'What would you like to do {}? Please use 1,2, or 3 to answer.'.
            format('Player 2'))
        print_moves()
        if response == '1':
            return attack(name_2, name_1)
        elif response == '2':
            return heal(name_2)
        elif response == '3':
            break


def player_stats(name_1, name_2):
    print('Player One:\n{}\n{}\n'.format(name_1['Health'], name_1['Rage']))
    print('Player two:\n{}\n{}\n'.format(name_2['Health'], name_2['Rage']))


def battle_phase_1(name_1, name_2):
    player_stats(name_1, name_2)
    print_moves()
    player_one_fight(name_1, name_2)


def battle_phase_2(name_1, name_2):
    player_stats(name_1, name_2)
    print_moves()
    player_two_fight(name_1, name_2)


def victor(gladiator, gladiator_2):
    while True:
        if is_dead(gladiator) == False and is_dead(gladiator_2) == False:
            battle_phase_1(gladiator, gladiator_2)
            if is_dead(gladiator) == True:
                player_stats(gladiator, gladiator_2)
                print('Player two wins!')
                break
            elif is_dead(gladiator_2) == True:
                player_stats(gladiator, gladiator_2)
                print('Player one wins')
                break
            battle_phase_2(gladiator, gladiator_2)
            if is_dead(gladiator) == True:
                player_stats(gladiator, gladiator_2)
                print('Player two wins!')
                break
            elif is_dead(gladiator_2) == True:
                player_stats(gladiator, gladiator_2)
                print('Player one wins')
                break
        else:
            victor()

    #while True:
    #    if is_dead(gladiator) == False and is_dead(gladiator_2) == False:
    #        battle_phase(gladiator, gladiator_2)
    #    elif is_dead(gladiator) == True:
    #        print('Player two wins!')
    #        break
    #    elif is_dead(gladiator_2) == True:
    #        print('Player one wins')
    #        break


def main():
    #name_1 = name()
    #name_2 = name_of_next()
    name_1 = new_gladiator(100, 0, 10, 20)
    name_2 = new_gladiator(100, 0, 10, 20)
    victor(name_1, name_2)


if __name__ == '__main__':
    main()
