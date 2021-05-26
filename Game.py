# -*- coding: utf-8 -*-

import random
from Player import Player, Card

class Game:
    def __init__(self):
        self.turn = 0
        self.players = []
        self.cards = [] 
        self.losers = []
    
    def addPlayer(self, name):
        self.players.append(Player(name)) 
    
    def auction(self):
        pass
    
    def checkBankruptcy(self, playerQuantity):
        for i in self.players:
            if i.balance < 0:
                return True
    #kasa, parking -1 Podatek -2 Szansa -3 Podatek -4 Wiezienie -5
    def initiateCards(self):
        tab = [("Start", "Orange2", 0, None),("Warszawa", "LightSalmon4", 60, {0:2,1:10,2:30,3:90,4:160,5:250})
               ,("Kasa", "DodgerBlue2", -1, None),("Kraków", "LightSalmon4", 60, {0:4,1:20,2:60,3:180,4:320,5:450})
               ,("Podatek doch", "AntiqueWhite2", -2, None),("Dworzec Mik", "black", 200, 25)
               ,("Popowo", "Royalblue3", 100, {0:6, 1:30, 2:90, 3:270, 4:400, 5:550}),("Szansa", "firebrick3", -3, None)
               ,("Deli", "Royalblue3", 100, {0:6, 1:30, 2:90, 3:270, 4:400, 5:550}),("Kamieńsk", "Royalblue3", 120, {0:8,1:40,2:100,3:300,4:450,5:600})
               ,("Wiezienie", "goldenrod3", -5, None),("Nowy dwór", "magenta3", 140, {0:10, 1:50, 2:150, 3:450, 4:625 ,5:750})
               ,("Elektrownia", "white", 150, 4),("Muchobór", "magenta3",  140, {0:10, 1:50, 2:150, 3:450, 4:625 ,5:750})
               ,("Szczepin", "magenta3", 160, {0:12, 1:60, 2:180, 3:500, 4:700 ,5:900}),("Dworzec Głw", "black", 200, 25)
               ,("Pawłowo", "DarkOrange2", 180, {0:14, 1:70, 2:200, 3:550, 4:750, 5:950}),("Kasa", "DodgerBlue2", -1, None)
               ,("Wrocław", "DarkOrange2", 180, {0:14, 1:70, 2:200, 3:550, 4:750, 5:950}),("Góra", "DarkOrange2", 180, {0:14, 1:70, 2:200, 3:550, 4:750, 5:950})
               ,("Parking", "red4", -1, None),("Błoto", "red4", 220,{0:18, 1:90, 2:250, 3:700, 4:875, 5:1050})
               ,("Szansa", "firebrick3", -3, None),("Pawłowo", "red4", 240,{0:20, 1:100, 2:300, 3:750, 4:925, 5:1100})
               ,("Piaski", "red4", 220,{0:18, 1:90, 2:250, 3:700, 4:875, 5:1050}),("Dworzec Pop", "black", 200, 25)
               ,("Sosnowiec", "yellow", 260,{0:22, 1:110, 2:330, 3:800, 4:975, 5:1150}),("Leszno", "yellow",  260,{0:22, 1:110, 2:330, 3:800, 4:975, 5:1150})
               ,("Wodociagi", "white", 150, 4),("Rawicz", "yellow",  280,{0:24, 1:120, 2:360, 3:850, 4:1025, 5:1200})
               ,("Idz do\nwiezienia", "royal blue", -4, None),("Bełchatów", "green", 300, {0:26, 1:130, 2:390, 3:900, 4:1100, 5:1275})
               ,("Wąsosz", "green", 300, {0:26, 1:130, 2:390, 3:900, 4:1100, 5:1275}),("Kasa", "DodgerBlue2", -1, None)
               ,("Środa Wlkp", "green", 320, {0:28,1:150, 2:450, 3:1000, 4:1200, 5:1500}),("Dworzec Cent", "black", 200, 25)
               ,("Szansa", "firebrick3", -3, None),("Bydgoszcz", "RoyalBlue4", 350, {0:35,1:175,2:500,3:1100,4:1300,5:1500})
               ,("Podatek luks", "AntiqueWhite2", -2, None),("Śmigiel","RoyalBlue4", 400, {0:50,1:200,2:600,3:1400,4:1700,5:2000})]
        for i in tab:
            self.cards.append(Card(i[0],i[1],i[2],i[3]))
        
            
if __name__ == "__main__":
    game = Game()
    game.initiateCards()
    game.addPlayer("name")
    game.addPlayer("ds")
    game.addPlayer('sad')
    for i in game.players:
        print(i)
        game.move(i)
        print(i)
    print(game.cards[1])