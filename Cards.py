# -*- coding: utf-8 -*-

class Card:
    field = 0
    def __init__(self, name, colour, cost, rent, upgradeCost = 200, level = 0, owner = None, mortgaged = False):
        self.__name = name
        self.__colour = colour
        self.__cost = cost
        self.__rent = rent
        self.__fieldNumber = Card.field
        self.__level = level
        if(self.__fieldNumber <= 10 or colour != None):
            self.__upgradeCost = upgradeCost/4
        elif(self.__fieldNumber <= 20 or colour != None):
            self.__upgradeCost = upgradeCost/2*3
        elif(self.__fieldNumber <= 30 or colour != None):
            self.__upgradeCost = upgradeCost/2
        elif(self.__fieldNumber <= 40 or colour != None):
            self.__upgradeCost = upgradeCost
        else:
            self.__upgradeCost = 0                
        self.__owner = owner
        self.__mortgaged = mortgaged
        Card.field += 1
    
    @property
    def name(self):  #returns name of the card
        return self.__name
    @property
    def colour(self):  #returns colour of the card
        return self.__colour
    @property
    def cost(self):  #returns cost of the card
        return self.__cost
    @property
    def upgradeCost(self): #returns upgrade cost
        return self.__upgradeCost
    @property
    def fieldNumber(self):  #returns number of the field of the card
        return self.__fieldNumber
    @property
    def level(self):  #returns level of the card
        return self.__level
    @level.setter
    def level(self, number): #changes level of the card
        self.__level = number
    @property
    def rent(self):         # returns value of rent of the card
        return self.__rent    
    @property
    def owner(self):  #returns owner of the card
        return self.__owner
    @owner.setter
    def owner(self, newOwner):    #changes owner of the card
        self.__owner = newOwner
    @property
    def mortgaged(self): #returns if card is mortgaged
        return self.__mortgaged
    @mortgaged.setter
    def mortgaged(self, b): #changes value of the field mortgaged of the card
        self.__mortgaged = b    

    @property
    def mortgage(self): #returns amount of money for mortgage
        return self.__cost*0.5
    
    def isOwned(self): #checks if someone is an owner of this card
        return self.__owner != None 
    
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self.name, self.colour, self.cost, self.upgradeCost, self.level, self.rent, self.owner, self.mortgaged)

if __name__ == "__main__":
    a = Card("nazwa", "kolor", 200, 2000, 100) 
    print(a)
    print(a.isOwned())
    a.owner = "ja"
    print(a)
    print(a.isOwned())