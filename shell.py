import core


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
            format(name_1))
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
            format(name_2))
        print_moves()
        if response == '1':
            return attack(name_2, name_1)
        elif response == '2':
            return heal(name_2)
        elif response == '3':
            break


def battle_phase():
    while True:
        if is_dead(name_1) == False and is_dead(name_2) == False:
            print_moves()
            player_one_fight(name_1, name_2)
            print_moves()
            player_two_fight(name_1, name_2)
        elif is_dead(name_1) == True:
            print('Player two wins!')
        elif is_dead(name_2) == True:
            print('Player one wins')


def main():
    name_1 = name()
    name_2 = name_of_next()
    name_1 = new_gladiator(100, 0, 10, 20)
    name_2 = new_gladiator(100, 0, 10, 20)


if __name__ == '__main__':
    main()
