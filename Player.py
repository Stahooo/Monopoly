# -*- coding: utf-8 -*-

from Cards import Card

class Player:

    def __init__(self, name, balance = 1500, position = 0, imprisoned = False, bankrupt = False):
        self.__name = name
        self.__balance = balance
        self.__position = position
        self.__imprisoned = imprisoned
        self.__bankrupt = bankrupt
    
    @property
    def imprisoned(self):
        return self.__imprisoned
    @imprisoned.setter
    def imprisoned(self, newI):
        self.__iprisoned = newI
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, newbalance):
        self.__balance = newbalance
    
    @property
    def bankrupt(self):
        return self.__bankrupt
    
    @bankrupt.setter
    def bankrupt(self, newBankrupt):
        self.__bankrupt = newBankrupt
    
    @property
    def name(self):
        return self.__name

    def addCard(self,card):
       self.__cards.append(card)
       
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, pos):
        self.__position = pos
        
    def __str__(self):
        return "{0}\t{1}\t{2}\t{3}\t{4}".format(self.name, self.balance, self.position, self.imprisoned, self.bankrupt)
        
if __name__ == "__main__":
    a = Player("Stahoo")
    print(a)
    print(a.name)
   