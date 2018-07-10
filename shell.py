from core import *


def name():
    name = input('What is the name of player one? >>> ')
    return name


def name_of_next():
    name = input('What is the name of player two? >>> ')
    return name


def pick_class():
    #gladiator = {                      specials:
    #    'Health': health,              1 = healing
    #    'Rage': rage,                  2 = slash
    #    'Damage Low': damage_low,      3 = suicide
    #    'Damage High': damage_high,    4 = power erase
    #    'Magic': magic                 5 = steal
    #    'Special': special
    #}
    print()
    print('-----CHARACTERS-----')
    print(
        '1.Warrior\nHe is a strong character with average health.\nHis special ability is called slash in which he causes high damage to his opponent.'
    )
    print(
        '2. King\nThe king has high health to match his high status.\nWith his power he can take power from his opponents.'
    )
    print(
        '3.Common Man\nHe is just a man.\nDon\'t use this scared man\'s ability.'
    )
    print(
        '4.Healer\nThis mage has may have weaker attacks but starts with high power\nThe ability of powerful healing can be used to outlast his enemy\'s in battle.'
    )
    print(
        '5.Thief\nWith his sneaky ways, other character\'s stats can be used to his ability.\nHis special ability allows him to steal stats from his opponent and add to his own.'
    )
    print()
    while True:
        class_type = input('Pick your class type number >>> ')
        if class_type == '1':  #warrior
            return new_gladiator(100, 30, 10, 20, 0, 2)
        elif class_type == '2':  #king
            return new_gladiator(120, 50, 8, 16, 0, 4)
        elif class_type == '3':  #Common Man
            return new_gladiator(70, 0, 3, 6, 0, 3)
        elif class_type == '4':  #healer
            return new_gladiator(100, 0, 6, 15, 45, 1)
        elif class_type == '5':  #Thief
            return new_gladiator(100, 0, 7, 18, 15, 5)
        else:
            print('Come on dude, just pick a type.')
    print('-----')


def print_moves():
    print(
        '~~1.Attack (+15 Rage)\n~~2.Heal (-10 Power)\n~~3.Pass (+30 Rage and Power)\n~~4.Quit\n~~5.Special (-45 Power)\n'
    )


def player_one_fight(player_1, player_2, name_1, name_2):
    while True:
        response = input(
            'What would you like to do {}?\nPlease use 1 - 5 to answer >>> '.
            format(name_1))
        print_moves()
        if response == '1':
            print("{} uses an attack".format(name_1))
            return attack(player_1, player_2)
        elif response == '2':
            if player_1['Power'] >= 10:
                print("{} has healed themself".format(name_1))
                return heal(player_1)
            else:
                print('Not enough power')
        elif response == '4':
            print('Wow you just let player Two win')
            exit()
        elif response == '3':
            print("{} has skipped their turn".format(name_1))
            player_1['Rage'] = player_1['Rage'] + 30
            player_1['Power'] += 30
            return None
        elif response == '5':
            if player_1['Power'] > 45:
                print('{} used their special attack'.format(name_1))
                return special_move(player_1, player_2)
            else:
                print('Not enough power')

        else:
            print('Invalid number input.')


def player_two_fight(player_1, player_2, name_1, name_2):
    while True:
        response = input(
            'What would you like to do {}?\nPlease use 1-5 to answer >>> '.
            format(name_2))
        print_moves()
        if response == '1':
            print("{} uses an attack.".format(name_2))
            return attack(player_2, player_1)
        elif response == '2':
            if player_2['Power'] >= 10:
                print('{} has healed themself'.format(name_2))
                return heal(player_2)
            else:
                print('Not enough power')
        elif response == '4':
            print('Wow, you just let player one win.')
            exit()
        elif response == '3':
            print("{} has skipped their turn".format(name_2))
            player_2['Rage'] = player_2['Rage'] + 30
            player_2['Power'] += 30
            return None
        elif response == '5':
            if player_2['Power'] >= 45:
                print("{} used their special attack".format(name_2))
                return special_move(player_2, player_1)
            else:
                print('Not enough power')
        else:
            print('Invalid number input.')


def player_stats(player_1, player_2, name_1, name_2):
    print(
        "^^^^^\n{}'s stats:\nHealth: {}\nRage: {}\nPower: {}\n^^^^^\n".format(
            name_1, player_1['Health'], player_1['Rage'], player_1['Power']))
    print("^^^^^\n{}'s stats:\nHealth: {}\nRage: {}\nPower: {}\n^^^^^".format(
        name_2, player_2['Health'], player_2['Rage'], player_2['Power']))


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
