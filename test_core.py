from core import *
billy = {'Health': 100, 'Rage': 0, 'Damage Low': 25, 'Damage High': 75}
joe = {'Health': 70, 'Rage': 80, 'Damage Low': 40, 'Damage High': 90}


def test_new_gladiator():
    assert new_gladiator(100, 0, 25, 75) == {
        'Health': 100,
        'Rage': 50,
        'Damage Low': 25,
        'Damage High': 75
    }
    assert new_gladiator(0, 0, 0, 0) == {
        'Health': 0,
        'Rage': 0,
        'Damage Low': 0,
        'Damage High': 0
    }


def test_heal():
    assert heal(joe) == {
        'Health': 75,
        'Rage': 70,
        'Damage Low': 40,
        'Damage High': 90
    }
    assert heal(billy) == {
        'Health': 100,
        'Rage': 0,
        'Damage Low': 25,
        'Damage High': 75
    }


lilly = {'Health': 0}
jojo = {'Health': 9}


def test_is_dead():
    assert is_dead(lilly) == True
    assert is_dead(jojo) == False
