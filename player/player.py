# coding: utf-8

def wagerNumberRussianRoulette():
    wagerNb = input("Faites vos jeux! ")
    try:
        wagerNb = int(wagerNb)
        assert wagerNb > 0
        assert wagerNb < 49
    except ValueError:
        print("Vous n'avez pas saisi un nombre.")
        wagerNumberRussianRoulette()
    except AssertionError:
        print("Vous devez parier un nombre compris entre 0 et 49.")
        wagerNumberRussianRoulette()
    else:
        return wagerNb

def betPlayer():
    bet = input("Combien voulez-vous parier? ")
    try:
        bet = int(bet)
        assert bet > 20
    except ValueError:
        print("Vous n'avez pas saisi un nombre.")
        betPlayer()
    except AssertionError:
        print("Votre mise dois etre superieur a 20")
        betPlayer()
    else:
        return bet