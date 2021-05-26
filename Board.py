# -*- coding: utf-8 -*-

import random
from tkinter import *
import tkinter as tk
from Game import Player, Game

fields=[]


class Board():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("monopol")
        self.root.geometry("+300+50")
        self.root.configure(bg="light sky blue")
        self.root.resizable(False,False)
        self.board = tk.Frame(self.root)    
        self.board.configure(bg="light sky blue")
        self.menubar = tk.Menu(self.board)
        self.optmenu = tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Options",menu=self.optmenu)
        self.optmenu.add_command(label="Save", command=self.saveToFile)
        self.optmenu.add_command(label="Load", command=self.loadFromFile)
        self.optmenu.add_command(label="Ranking",command=self.ranking)
        self.optmenu.add_separator()
        self.optmenu.add_command(label="Exit", accelerator="CTRL+Q", command=self.iExit)
        self.root.bind("<Control-q>", self.iExit)
        self.root.config(menu=self.menubar)
        
        but = tk.Button(self.board, text="\n" + game.cards[0].name, width=10,height=5)
        but.grid(row=10, column=0)
        fields.append(but)
        
        for i in range(1,10):
            but = tk.Button(self.board, text="\n"+ game.cards[i].name, width=10,height=3,command=lambda i=i: self.showCard(i))
            but.grid(row=10-i,column=0)
            fields.append(but)
        
        but = tk.Button(self.board, text="\n"+ game.cards[10].name,  width=10,height=5)
        but.grid(row=0, column=0)
        fields.append(but)
        
        for i in range(1,10):
            but = tk.Button(self.board, text="\n"+ game.cards[i].name, width=10,height=5, command=lambda i=i: self.showCard(10+i))
            but.grid(row=0,column=i)    
            fields.append(but)
        
        but = tk.Button(self.board, text="\n"+ game.cards[20].name,  width=10,height=5)
        but.grid(row=0, column=10)
        fields.append(but)

        for i in range(1,10):
            but = tk.Button(self.board, text="\n"+ game.cards[i].name, width=10,height=3, command=lambda i=i: self.showCard(20+i))
            but.grid(row=i, column=10)
            fields.append(but)
            
        but = tk.Button(self.board, text="\n"+ game.cards[30].name,  width=10,height=5)
        but.grid(row=10, column=10)
        fields.append(but)
        
        for i in range(1,10):
            but = tk.Button(self.board, text="\n"+ game.cards[i].name, width=10,height=5, command=lambda i=i: self.showCard(30+i))
            but.grid(row=10,column=10-i)
            fields.append(but)
        
        for i in range(0,len(fields)):
            if game.cards[i].colour == "black":
                fields[i].configure(fg="white")
            fields[i].configure(bg=game.cards[i].colour, text="\n" + game.cards[i].name)
       
        self.btnStart = tk.Button(self.board, text="Start",width=10,height=2, command=lambda: self.startGame())
        self.btnPlayers = tk.Button(self.board, text="Players",width=10, height=2,command=lambda: [self.btnStart.destroy(),self.btnPlayers.destroy(),self.addPlayer()])
        self.btnPlayers.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.btnStart.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        
        
        self.board.grid()
        self.root.mainloop()
        
    #Players Management Buttons
    def addPlayer(self):
        self.name_var = tk.StringVar()
        entryPlayer = tk.Entry(self.board, textvariable=self.name_var, width=30)
        entryPlayer.insert(0,"Wprowadz nazwe gracza")
        
        listNames = tk.Listbox(self.board)
        self.showPlayers(listNames)
        
        btnAdd = tk.Button(self.board, text="Add Player",width=10, height=2,command=lambda: [self.add(), entryPlayer.delete(0, tk.END),self.showPlayers(listNames)])  
        btnRemove = tk.Button(self.board, text="Remove Player",width=10, height=2, command=lambda: [self.remove(),entryPlayer.delete(0, tk.END),self.showPlayers(listNames)])
        btnBack = tk.Button(self.board, text="Back",width=10, height=2, command=lambda:[self.back(),btnAdd.destroy(),btnRemove.destroy(),
                                                                                     listNames.destroy(),btnBack.destroy(),entryPlayer.destroy()])
     
        listNames.place(relx=0.75,rely=0.5,anchor=tk.CENTER,width=200)
        entryPlayer.place(relx=0.5,rely=0.4,anchor=tk.CENTER)
        btnAdd.place(relx=0.44, rely=0.5, anchor=tk.CENTER)
        btnRemove.place(relx=0.56, rely=0.5, anchor=tk.CENTER)
        btnBack.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    
    #Removing players
    def remove(self):
        for i in game.players:
            if(i.name == self.name_var.get()):
                game.players.remove(i)
                
    #Adding players    
    def add(self):
        isin = False
        for i in game.players:
            if self.name_var.get() == i.name:
                isin = True
        if self.name_var.get() != "" and len(game.players) < 8 and not isin and len(self.name_var.get()) < 15:
            game.addPlayer(self.name_var.get())
            tk.messagebox.showinfo("Succesful", "Player Added")   
        elif isin:
            tk.messagebox.showinfo("Error", "Player Already Added")
        elif not len(self.name_var.get()) < 15:
            tk.messagebox.showinfo("Error", "Too Long Name")
        elif not len(game.players) < 8:
            tk.messagebox.showinfo("Error", "Too Many Players")
        else:
            tk.messagebox.showinfo("Error", "Wrong Name")
    
    #Show players in listbox           
    def showPlayers(self, ln):
        listNames = ln
        listNames.delete(0,tk.END)
        for i in range(len(game.players)):
            listNames.insert(i,str(i+1) +": " + game.players[i].name)
    
    #Go back to start    
    def back(self):
        self.btnStart = tk.Button(self.board, text="Start",width=10,height=2, command=lambda: self.startGame())
        self.btnPlayers = tk.Button(self.board, text="Players",width=10, height=2,command=lambda: [self.btnStart.destroy(),self.btnPlayers.destroy(),self.addPlayer()])
        self.btnStart.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.btnPlayers.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
  
    #Game Start
    def startGame(self):
        if len(game.players) > 1:
            self.btnStart.destroy()
            self.btnPlayers.destroy()
                   
            for i in range(0,len(game.players)):     
                oldtext = fields[game.players[len(game.players)-i-1].position]['text']
                oldtext = str(len(game.players)-i) + oldtext
                fields[game.players[len(game.players)-i-1].position].configure(text=oldtext) 
            
            self.labRoll = tk.Label(self.board, width=20, font="32",bg="light sky blue", text="Position = " + str(0))
            self.labBalance = tk.Label(self.board, width=20, font="16",bg="light sky blue", text="Balance = " + str(game.players[game.turn].balance))
            self.labTurn = tk.Label(self.board, font="32",bg="light sky blue", text= str(game.turn+1) + " Player: "+ game.players[game.turn].name +" Turn")
            self.btnRoll = tk.Button(self.board,width=10,height=2, text="Roll",command=self.roll)
            self.btnOwns = tk.Button(self.board,width=10,height=2, text="Owns", command=self.owns)
            
            self.labTurn.place(relx=0.5,rely=0.25, anchor=tk.CENTER)
            self.btnRoll.place(relx=0.4,rely=0.5, anchor=tk.CENTER)
            self.labRoll.place(relx=0.5,rely=0.30, anchor=tk.CENTER)
            self.labBalance.place(relx=0.5,rely=0.35, anchor=tk.CENTER)
            self.btnOwns.place(relx=0.6,rely=0.5, anchor=tk.CENTER)
        else:           
            tk.messagebox.showinfo("Error", "Add players")
   
    def roll(self):
        i = 0
        dice1 = 0
        dice2 = 0 
        oldPosition = game.players[game.turn].position
        newPosition = 0
            
        oldtext = fields[oldPosition]['text']
        oldtext = oldtext.replace(str(game.turn+1),"")
        fields[oldPosition].configure(text=oldtext)
        
        while (i < 3 and dice1 == dice2):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            newPosition += dice1 + dice2
            i+=1
            
        
        
        if(i == 3 and dice1 == dice2):
            game.players[game.turn].position = 30 #going to prison
            game.players[game.turn].imprisoned = True
        else:
            newPosition += oldPosition
            game.players[game.turn].balance += 200 * int(newPosition / 40)
            newPosition %= 40
            game.players[game.turn].position = newPosition
            if newPosition == 30:
                game.players[game.turn].position = 10 #going to prison
                newPosition = game.players[game.turn].position
                game.players[game.turn].imprisoned = True
            
        oldtext = fields[newPosition]['text']
        oldtext = str(game.turn+1) + oldtext
        fields[newPosition].configure(text=oldtext) 
              
        if game.cards[newPosition].cost > 0:
            if game.cards[newPosition].owner == None:
                doBuy = tk.messagebox.askyesno(title="Confirmation", message="Do you want to buy it for " + str(game.cards[newPosition].cost))
                if doBuy:
                    if game.players[game.turn].balance > game.cards[newPosition].cost: 
                        game.cards[newPosition].owner = game.players[game.turn].name
                        game.players[game.turn].balance -=  game.cards[newPosition].cost   
                    else:
                        tk.messagebox.showinfo("Error", "Not Enough Money")
                        
        if game.cards[newPosition].owner != None and game.cards[newPosition].owner != game.players[game.turn].name:
            self.payRent()
            
        if game.players[game.turn].position == 4 or game.players[game.turn].position == 38:
            tk.messagebox.showinfo("Tax", "You are paying to the bank")
            game.players[game.turn].balance -= 100
     
        self.checkBalance()
        
        self.labTurn.destroy()
        self.labRoll.destroy()
        self.labBalance.destroy()
        self.labBalance = tk.Label(self.board, width=20, font="16",bg="light sky blue", text="Balance = " + str(int(game.players[(game.turn+1)%len(game.players)].balance)))
        self.labTurn = tk.Label(self.board, font="32",bg="light sky blue", text="Player: "+ game.players[(game.turn+1)%len(game.players)].name +" Turn")
        self.labRoll = tk.Label(self.board, width=20, font="32",bg="light sky blue", text="Position = " + str(game.players[(game.turn+1)%len(game.players)].position))
        self.labTurn.place(relx=0.5,rely=0.25, anchor=tk.CENTER)
        self.labBalance.place(relx=0.5,rely=0.35, anchor=tk.CENTER)
        self.labRoll.place(relx=0.5,rely=0.30, anchor=tk.CENTER)
             
        game.turn += 1
        game.turn %= len(game.players)
    
    def owns(self):
        top = tk.Toplevel(bg="Light sky blue")
        top.grab_set()
        top.geometry("+650+300")
        top.resizable(False,False)
        for i in game.cards:
            if i.owner == game.players[game.turn].name:
                tk.Label(top,font="16", bg="Light sky blue",text=str(i.fieldNumber) + " " + i.name + " " + i.colour).pack()
                
    def payRent(self):
        railroadsOwned = 0
        actualCard = game.cards[game.players[game.turn].position]
        if actualCard.colour != "black":
            amount = int(actualCard.rent[actualCard.level])
            game.players[game.turn].balance -= amount
        else:
            for i in range(5,39,10):
                if actualCard.owner == game.cards[i].owner:
                    railroadsOwned += 1
                amount = {1:25,2:50,3:100,4:200}[railroadsOwned]
                
        tk.messagebox.showinfo("Pay Rent", "You are paying " + str(amount))     
        for i in game.players:
            if i.name == actualCard.owner:
                i.balance += amount
        
    #Showing clicked cards                
    def showCard(self, cardNumber):
        top = tk.Toplevel(bg=game.cards[cardNumber].colour)
        top.grab_set()
        top.geometry("200x500+650+200")
        top.resizable(False,False)
        
        if game.cards[cardNumber].colour == "black":
            
            if game.cards[cardNumber].owner != None:    
                tk.Label(top,fg ="white",text=game.cards[cardNumber].owner, bg=game.cards[cardNumber].colour).pack()
            else:
                tk.Label(top,fg ="white",text="No owner", bg=game.cards[cardNumber].colour).pack()
           
            tk.Label(top,text="Cost of the card: " + str(game.cards[cardNumber].cost),fg ="white", bg=game.cards[cardNumber].colour).pack()
            tk.Label(top,text="1 Rails owned rent: 25", fg="white", bg="black").pack()
            tk.Label(top,text="2 Rails owned rent: 50", fg="white", bg="black").pack()
            tk.Label(top,text="3 Rails owned rent: 100", fg="white", bg="black").pack()
            tk.Label(top,text="4 Rails owned rent: 200", fg="white", bg="black").pack()      
       
        elif game.cards[cardNumber].colour == "white":
            if game.cards[cardNumber].owner != None:    
                tk.Label(top,text=game.cards[cardNumber].owner, bg=game.cards[cardNumber].colour).pack()
            else:
                tk.Label(top,text="No owner", bg=game.cards[cardNumber].colour).pack()
           
            tk.Label(top,text="Cost of the card: " + str(game.cards[cardNumber].cost), bg=game.cards[cardNumber].colour).pack()     
        elif (game.cards[cardNumber].cost > 50 ):
            
            if game.cards[cardNumber].owner != None:
                tk.Label(top, text=game.cards[cardNumber].owner, bg=game.cards[cardNumber].colour).pack()
            else:
                tk.Label(top, text="No owner", bg=game.cards[cardNumber].colour).pack()
            
            tk.Label(top,text="Card Level: " +str(game.cards[cardNumber].level), bg=game.cards[cardNumber].colour).pack()
            tk.Label(top,text="Cost of the card: " + str(game.cards[cardNumber].cost), bg=game.cards[cardNumber].colour).pack()
           
            for i in range (0,6):
                tk.Label(top,text="Level " + str(i) + " rent: " + str(game.cards[cardNumber].rent[i]), bg=game.cards[cardNumber].colour).pack()
            tk.Label(top, text="Upgrade Cost: " + str(game.cards[cardNumber].upgradeCost), bg=game.cards[cardNumber].colour).pack()
            tk.Label(top, text="Is mortgaged: " + str(game.cards[cardNumber].mortgaged), bg=game.cards[cardNumber].colour).pack()
        
        but = tk.Button(top, text="Close",width=10,command=lambda: top.destroy())      
        but.pack(side=tk.BOTTOM)  
        
        if len(game.players) != 0:
            if game.players[game.turn].name == game.cards[cardNumber].owner:
                self.btnBuild = tk.Button(top, text="  Build  ",width=10,command=lambda: self.build(cardNumber)).pack(side=tk.BOTTOM)
                self.btnDemolish= tk.Button(top, text="Demolish",width=10,command=lambda: self.demolish(cardNumber)).pack(side=tk.BOTTOM)
                self.btnMortgage = tk.Button(top, text="Mortgage",width=10,command=lambda: self.mortgage(cardNumber)).pack(side=tk.BOTTOM)
                self.btnRedeem= tk.Button(top, text="Redeem",width=10,command=lambda: self.redeem(cardNumber)).pack(side=tk.BOTTOM)
    
    def checkBalance(self):
        if game.players[game.turn].balance < 0:
            game.losers.append(game.players[game.turn])
            game.players.remove(game.players[game.turn])
            print(game.players)
            if len(game.players) == 1:
                tk.messagebox.showinfo("Congratulations", "You won " + game.players[0].name)
                self.root.destroy()
    
    #Buy card
    def build(self, cardNumber):
        if game.cards[cardNumber].colour == "white" or game.cards[cardNumber].colour == "black" :
            tk.messagebox.showinfo("Error","Can't upgrade this card")
        elif(game.cards[cardNumber].level < 5 ):
            if game.players[game.turn].balance > game.cards[cardNumber].upgradeCost:
                game.players[game.turn].balance -= game.cards[cardNumber].upgradeCost
                game.cards[cardNumber].level+=1
                tk.messagebox.showinfo("Successful", "Card Upgraded")
            else:
                tk.messagebox.showinfo("Error","Not Enough Money")
        else:
            tk.messagebox.showinfo("Error", "Max Card Level")
            
    #Level down        
    def demolish(self, cardNumber):
        if(game.cards[cardNumber].level > 0):
            game.cards[cardNumber].level -= 1
            game.players[game.turn].balance += game.cards[cardNumber].upgradeCost
            tk.messagebox.showinfo("Successful", "Level Down")
        else:
            tk.messagebox.showinfo("Error", "Card Already At Level 0")
            
    #Mortgage place
    def mortgage(self, cardNumber):
        if(game.cards[cardNumber].level == 0):
            game.cards[cardNumber].mortgaged = True
            game.players[game.turn].balance += game.cards[cardNumber].cost/2
            tk.messagebox.showinfo("Successful", "Card Mortgaged")
        else:
            tk.messagebox.showinfo("Error", "Card level Is Not 0")  
    
    #Redeem mortgaged        
    def redeem(self, cardNumber):
        amount = 1.1*game.cards[cardNumber].cost/2
        
        if game.cards[cardNumber].mortgaged == True and game.players[game.turn].balance > amount:
            game.cards[cardNumber].mortgaged = False
            game.players[game.turn].balance -= amount
            tk.messagebox.showinfo("Successful", "Card Redeemed")
        elif game.cards[cardNumber].mortgaged == False:
            tk.messagebox.showinfo("Error", "Card not mortgaged")
        else:
            tk.messagebox.showinfo("Error", "Not enough money")
    
    
    def saveToFile(self):
        top = tk.Toplevel(bg="light sky blue")
        top.grab_set()
        top.geometry("200x300+650+300")
        top.resizable(False,False)
       
        answer = tk.messagebox.askyesno("Confirm","Do You Really Want To Save Game?")
        if answer: 
            listNames = tk.Listbox(top)
            for i in range(1, 10):    
                listNames.insert(i-1,"zapis_" + str(i))
            
            
            btnLoad = tk.Button(top, text="Save", command=lambda: self.save(listNames))
            btnClose =  tk.Button(top, text="Close", command=lambda: top.destroy())
            tk.Label(top,bg="light sky blue").pack()    
            listNames.pack()
            tk.Label(top,bg="light sky blue").pack()
            
            btnLoad.pack()
            btnClose.pack()
        else:
            top.destroy()
    
    def save(self, listNames):
        for i in listNames.curselection():
            file = open(listNames.get(i)+".txt","w")
        file.write(str(game.turn)+ "\n")
        for i in game.players:
            file.write("P\t" + i.name +"\t"+ str(int(i.balance)) +"\t"+ str(i.position) +"\t"+ str(i.imprisoned) +"\t"+ str(i.bankrupt) + "\n")
        for i in game.cards:
            file.write("C\t" + str(i.fieldNumber) +"\t"+ str(i.level) +"\t"+  str(i.owner) +"\t"+ str(i.mortgaged) +"\n")
        file.close()
        
    def loadFromFile(self):
        top = tk.Toplevel(bg="light sky blue")
        top.grab_set()
        top.geometry("200x300+650+300")
        top.resizable(False,False)
       
        answer = tk.messagebox.askyesno("Confirm","Do You Really Want To Load Game?")
        if answer: 
            listNames = tk.Listbox(top)
            for i in range(1, 10):    
                listNames.insert(i-1,"zapis_" + str(i))
            
            
            btnLoad = tk.Button(top, text="Load", command=lambda: self.load(listNames))
            btnClose =  tk.Button(top, text="Close", command=lambda: top.destroy())
            tk.Label(top,bg="light sky blue").pack()    
            listNames.pack()
            tk.Label(top,bg="light sky blue").pack()
            
            btnLoad.pack()
            btnClose.pack()
        else:
            top.destroy()
     
    #Load Game        
    def load(self, listNames):
        for i in listNames.curselection():
            try:
                file = open(listNames.get(i)+".txt","r")
            except:
                tk.messagebox.showinfo("Error","There is no such file")
        try:
            game.players.clear()
            line = file.readline() 
            game.turn = int(line)           
            while line:
                tokens = line.split("\t")
                if tokens[0] == "P":
                    if tokens[4] == "True":
                        tokens[4] = True
                    else:
                        tokens[4] = False
                    
                    if tokens[5] == "True":
                        tokens[5] = True
                    else:
                        tokens[5] = False                  
                    game.players.append(Player(tokens[1],int(tokens[2]),int(tokens[3]),int(tokens[4]), tokens[5]))
                elif tokens[0] == "C":
                    nr = int(tokens[1])
                    game.cards[nr].level = int(tokens[2])
                    if tokens[3] == "None":
                        tokens[3] = None
                    game.cards[nr].owner = tokens[3]
                    if tokens[4] == True:
                        game.cards[nr].mortgaged = True
                    else:
                        game.cards[nr].mortgaged = False
                line = file.readline()               
            print(line)
            file.close()
        except:
            pass
    
    def ranking(self): 
        winners = []
        money = []
        for i in range(0,len(game.players)):
            money.append(game.players[i].balance)
            winners.append(game.players[i])
        for i in game.cards:
            for j in range(0,len(game.players)):
                if i.owner == game.players[j].name:
                    money[j] = i.cost + money[j]
                    
        for i in range(0, len(money)):
            for j in range(0, len(money)):
                if(money[i] > money[j]):
                    a = money[i]
                    money[i] = money[j]
                    money[j] = a
                    b = winners[i]
                    winners[i] = winners[j]
                    winners[j] = b
                    
        top = tk.Toplevel(bg="Light sky blue")
        top.grab_set()
        top.geometry("400x300+650+300")
        top.resizable(False,False)
        for i in range(0, len(money)):
            tk.Label(top,bg="Light sky blue", font="20", text=str(i+1)+ " Place " + winners[i].name + " " + str(money[i])).pack()
        for i in game.losers:
            tk.Label(top,bg="Light sky blue", font="20", text="Bankrupt " + i.name).pack()
            
    #Exit program
    def iExit(self, event=None):
        iExit = tk.messagebox.askyesno("Exit","Do you really want to exit?")
        if iExit > 0:
            self.root.destroy()
        
        
if __name__ == "__main__":
    game = Game()
    game.initiateCards()
    board = Board()
    
