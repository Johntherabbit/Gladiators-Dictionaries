from random import randint
from random import randrange


def new_gladiator(health, rage, damage_low, damage_high, power, special):
    gladiator = {
        'Health': health,
        'Rage': rage,
        'Damage Low': damage_low,
        'Damage High': damage_high,
        'Power': power,
        'Special': special
    }
    return gladiator


def attack(attacker, defender):
    damage = defender['Health'] - randint(attacker['Damage Low'],
                                          attacker['Damage High'])
    crit_damage = defender['Health'] - (randint(attacker['Damage Low'],
                                                attacker['Damage High'])) * 2
    critical = randrange(1, 100)
    if critical <= attacker['Rage']:
        print('CRITICAL!')
        defender['Health'] = crit_damage
        attacker['Rage'] = 0
        attacker['Power'] += 30
        return defender['Health']
    elif attacker['Rage'] < critical:
        defender['Health'] = damage
        attacker['Rage'] = attacker['Rage'] + 15
        attacker['Power'] += 15
        return defender['Health']


def heal(gladiator):
    if gladiator['Power'] < 10:
        return None
    elif gladiator['Power'] <= 0:
        gladiator['Power'] = 0
    elif gladiator['Health'] > 0:
        gladiator['Power'] = gladiator['Power'] - 10
        gladiator['Health'] = gladiator['Health'] + 10
        return gladiator
    else:
        return gladiator


def is_dead(gladiator):
    if gladiator["Health"] <= 0:
        gladiator['Health'] = 0
        return True
    else:
        return False


#special moves
# 1 = healing
# 2 = slash
# 3 = suicide
# 4 = power erase


def special_move(gladiator, gladiator_2):
    if gladiator['Special'] == 1:
        if gladiator['Power'] > 44:
            gladiator['Health'] += randint(30, 50)
            gladiator['Power'] -= 45
            gladiator['Rage'] += 25
            return gladiator
    elif gladiator['Special'] == 2:
        if gladiator['Power'] > 44:
            gladiator_2['Health'] -= 45
            gladiator['Power'] = gladiator['Power'] - 45
            return gladiator
    elif gladiator['Special'] == 3:
        if gladiator['Power'] >= 45:
            gladiator['Health'] -= gladiator['Health']
            return gladiator
    elif gladiator['Special'] == 4:
        if gladiator['Power'] >= 44:
            gladiator_2['Power'] = 0
            gladiator['Power'] -= 45
            return gladiator
    elif gladiator['Special'] == 5:
        if gladiator['Power'] >= 44:
            gladiator['Power'] -= 45
            gladiator_2['Power'] -= 20
            gladiator_2['Rage'] -= 20
            gladiator['Power'] += 20
            gladiator['Rage'] += 20
            if gladiator_2['Power'] <= 0:
                gladiator_2['Power'] = 0
                return gladiator_2
            if gladiator_2['Rage'] <= 0:
                gladiator_2['Rage'] <= 0
                return gladiator_2
    elif gladiator['Special'] == 6:
        if gladiator['Power'] >= 45:
            gladiator_2['Health'] -= 20
            gladiator['Health'] += 20
            gladiator['Power'] -= 45
        return gladiator


def name_of_class(gladiator):
    if gladiator == new_gladiator(100, 30, 10, 20, 0, 2):
        return 'Warrior'
    elif gladiator == new_gladiator(120, 50, 8, 16, 0, 4):
        return 'King'
    elif gladiator == new_gladiator(70, 0, 3, 6, 0, 3):
        return 'Common man'
    elif gladiator == new_gladiator(100, 0, 6, 15, 15, 1):
        return 'Healer'
    elif gladiator == new_gladiator(100, 0, 7, 18, 15, 5):
        return 'Thief'
