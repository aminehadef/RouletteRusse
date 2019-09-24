# coding: utf-8
import threading

import player.player as player
import game.russianRoulette as russianRoulette


money = 1000
nbTower = 0

def newGame():
    Game = input("Voulez-vous continuer de jouer? appuiez sur o pour oui et n pour non ")
    if Game == 'o':
        croupier()
    elif Game == 'n':
        print("A bientot!")
    else:
        print("Vous devez appuiez sur o ou n")
        newGame()


def croupier():
    if nbTower == 0:
        print("Vous rentrer en tabele avec", money)
    nbTwoer = nbTower + 1
    betPlayer = player.betPlayer()
    wagerPlayer = player.wagerNumberRussianRoulette()
    wager = russianRoulette.russianRoulette()
    print("Les jeux sont faits!")
    print("Rien ne va plus")
    game(charge, 2, wagerPlayer, wager, betPlayer ,4)
    
def game(func, sec, wagerPlayer, wager, betPlayer ,i = 4):

    def func_wrapper():
        global money
        if wager % 2 == 0:
            color = "noir"
            pAndNP = "pairs"
        else:
            color = "rouge"
            pAndNP = "impairs"
        if i > 0:
            game(func, sec, wagerPlayer, wager, betPlayer ,i)
            func()
        else:
            if wagerPlayer == wager:
                print(wager, color, pAndNP, "et manque")
                print("vous avez gagnier ", betPlayer * 3, "euro ;)")
                money = money + (betPlayer * 3)
                print("vous avez ", money)
            else:
                print(wager, color, pAndNP, "et manque")
                print("vous avez perdu!")
                if wagerPlayer % 2 == 0 and wager % 2 == 0:
                    money = money - (betPlayer / 2)
                else:
                    money = money - betPlayer

                print("vous avez ", money,"euro")
                newGame()
            return
    i = i - 1
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def charge():
    print(".")

croupier()