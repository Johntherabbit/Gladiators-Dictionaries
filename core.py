from random import randint
from random import randrange


def new_gladiator(health, rage, damage_low, damage_high):
    gladiator = {
        'Health': health,
        'Rage': rage,
        'Damage Low': damage_low,
        'Damage High': damage_high
    }
    return gladiator


def attack(attacker, defender):
    damage = defender[health] - randint(attacker[damage_low],
                                        attacker[damage_high])
    critical = randrange(1, 100)
    if critical <= attacker['Rage']:
        attacker['Health'] = damage * 2
        attacker['Rage'] = 0
    elif attacker['Rage'] < critical:
        attacker['Health'] = damage
        attacker['Rage'] = attacker['Rage'] + 15


def heal(gladiator):
    if gladiator['Health'] < 100:
        gladiator['Rage'] = gladiator['Rage'] - 10
        gladiator['Health'] = gladiator['Health'] + 5
        return gladiator
    else:
        return gladiator


def is_dead(gladiator):
    if gladiator["Health"] == 0:
        return True
    else:
        return False
