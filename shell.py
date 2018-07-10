from core import *


def name():
    name = input('What is the name of player one? >>> ')
    return name


def name_of_next():
    name = input('What is the name of player two? >>> ')
    return name


def pick_class():
    print()
    print('1.Warrior\n2.Healer\n3.Loser')
    while True:
        class_type = input('Pick your class type number >>> ')
        if class_type == '1':
            return new_gladiator(100, 40, 10, 20)
        elif class_type == '2':
            return new_gladiator(120, 50, 8, 16)
        elif class_type == '3':
            return new_gladiator(30, 0, 1, 2)
        else:
            print('Come on dude, just pick a type.')


def print_moves():
    print('~~1.Attack\n~~2.Heal\n~~3.Quit\n~~4.Pass\n')


def player_one_fight(player_1, player_2, name_1, name_2):
    while True:
        response = input(
            'What would you like to do {}?\nPlease use 1, 2, 3, or 4 to answer.>>> '.
            format(name_1))
        print_moves()
        if response == '1':
            return attack(player_1, player_2)
        elif response == '2':
            return heal(player_1)
        elif response == '3':
            break
        elif response == '4':
            player_1['Rage'] = player_1['Rage'] + 30
            return None

        else:
            print('Invalid number input.')


def player_two_fight(player_1, player_2, name_1, name_2):
    while True:
        response = input(
            'What would you like to do {}?\nPlease use 1, 2, 3, or 4 to answer.>>> '.
            format(name_2))
        print_moves()
        if response == '1':
            attack(player_2, player_1)
        elif response == '2':
            return heal(player_2)
        elif response == '3':
            break
        elif response == '4':
            player_2['Rage'] = player_2['Rage'] + 30
            return None
        else:
            print('Invalid number input.')


def player_stats(player_1, player_2, name_1, name_2):
    print("^^^^^\n{}'s stats:\nHealth: {}\nRage: {}\n^^^^^\n".format(
        name_1, player_1['Health'], player_1['Rage']))
    print("^^^^^\n{}'s stats:\nHealth: {}\nRage: {}\n^^^^^".format(
        name_2, player_2['Health'], player_2['Rage']))


def battle_phase_1(player_1, player_2, name_1, name_2):
    player_stats(player_1, player_2, name_1, name_2)
    print_moves()
    player_one_fight(player_1, player_2, name_1, name_2)


def battle_phase_2(player_1, player_2, name_1, name_2):
    player_stats(player_1, player_2, name_1, name_2)
    print_moves()
    player_two_fight(player_1, player_2, name_1, name_2)


def victor(gladiator, gladiator_2, name_1, name_2):
    while True:
        if is_dead(gladiator) == False and is_dead(gladiator_2) == False:
            battle_phase_1(gladiator, gladiator_2, name_1, name_2)
            if is_dead(gladiator) == True:
                player_stats(gladiator, gladiator_2, name_1, name_2)
                print("{} wins!".format(name_2))
                break
            elif is_dead(gladiator_2) == True:
                player_stats(gladiator, gladiator_2, name_1, name_2)
                print("{} wins!".format(name_1))
                break
            battle_phase_2(gladiator, gladiator_2, name_1, name_2)
            if is_dead(gladiator) == True:
                player_stats(gladiator, gladiator_2, name_1, name_2)
                print("{} wins!".format(name_2))
                break
            elif is_dead(gladiator_2) == True:
                player_stats(gladiator, gladiator_2, name_1, name_2)
                print("{} wins!".format(name_1))
                break
        else:
            victor()


def main():
    name_1 = name()
    name_2 = name_of_next()
    player_1 = pick_class()
    player_2 = pick_class()
    victor(player_1, player_2, name_1, name_2)


if __name__ == '__main__':
    main()
