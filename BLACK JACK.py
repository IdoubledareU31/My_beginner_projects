#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class Bank:
    def __init__(self, balance=1000):
        self.balance=balance
    
    def loss(self, amount=100):
        self.balance-=amount
        print (f'You lost {amount} and now you have {self.balance}')
    
    def gain(self, amount=100):
        self.balance+=amount
        print (f'You won {amount} and now you have {self.balance}')

bank=Bank()
  

youdied=False
while youdied==False:
    
   
    
    
    # In[3]:
    print ('                               STARTING A NEW GAME...')
    
    #creating a card
    
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
                    'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1} 
    
    #don't forget to count Ace as 11 if needed!!!!
    class Card:
        
        def __init__ (self):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]
    
    
    # In[4]:
    
    
    #dealing with aces
    def how_many_aces(values):
        count_aces=0
        for (a,b) in values:
            if "Ace" in a:
                count_aces+=1
        return count_aces
            
                
    
    
    # In[5]:
    
    
    #creating a deck
    
    class Deck:
        
        
        def __init__ (self, belongs="common"):
            self.listofcards =[]
            self.listofvalues=[]
            self.listofall=[]
            self.belongs = belongs
            self.howmany = f"There are {len(self.listofall)} cards in the deck"
            self.totalvalue = []
            
        #adds a card to the deck and removes from thedeck     
        def addcard(self):
            self.listofall.append(thedeck.listofall[0])
            self.listofvalues.append(thedeck.listofvalues[0])
            self.listofcards.append(thedeck.listofcards[0])
            self.totalvalue=sum(self.listofvalues)
            thedeck.listofall.pop(0)
            thedeck.listofcards.pop(0)
            thedeck.listofvalues.pop(0)
            return self.listofall
            
        def buildfull(self):
            for suit in suits:
                for rank in ranks:
                    self.listofcards.append(suit + ' ' + rank)
                    self.listofvalues.append(values[rank])
            self.listofall = list(zip(self.listofcards, self.listofvalues))
            self.totalvalue=sum(self.listofvalues)
            return self.listofall
                    
        def shuffledeck(self):
            random.shuffle(self.listofall)
            self.listofcards=[item[0] for item in self.listofall]
            self.listofvalues=[item[1] for item in self.listofall]
            self.totalvalue=sum(self.listofvalues)
            return self.listofall
            #for item in fulldeck:
            #    print (item)
    
    
    # In[6]:
    
    
    thedeck=Deck()
    
    thedeck.buildfull()
    #print(thedeck.listofall, end="\n\n")
    thedeck.shuffledeck()
    #print(thedeck.listofall)
    #print(thedeck.listofvalues)
    #print(thedeck.totalvalue)
    #print(thedeck.listofall, end="\n\n")
    
    
    # In[7]:
    
    
    #building my deck of two card
    mydeck=Deck("user")
    mydeck.addcard()
    mydeck.addcard()
    print ('You draw two cards')
    print (mydeck.listofall)
    print(mydeck.listofvalues)
    print(mydeck.totalvalue)
    if mydeck.totalvalue<=21:
        possiblesums=[mydeck.totalvalue]
    if how_many_aces(mydeck.listofall)==0:
        print(f'Total value of your cards is {mydeck.totalvalue}\n')
    else:
        print(f'You have {how_many_aces(mydeck.listofall)} aces in your deck. Total value of your cards is at least {mydeck.totalvalue}')
        
        for item in range(1,how_many_aces(mydeck.listofall)):
            if item*10+mydeck.totalvalue<=21:
                possiblesums.append(item*10+mydeck.totalvalue)
        print(f'Your possible sums are {possiblesums}\n')
    print ('\n')
    
    
    # In[8]:
    
    
    #buildinng dealers deck of two cards one of which lies face down
    hisdeck=Deck("dealer")
    hisdeck.addcard()
    hisdeck.addcard()
    print ("Dealer draws two cards")
    print(f"{hisdeck.listofall[0]}, ('A card face down')\n")
#    print(f'Dealer has {how_many_aces(hisdeck.listofall)} aces in your deck. Total value of his cards is at least {hisdeck.totalvalue}')
    if hisdeck.totalvalue<=21:
        hispossiblesums=[hisdeck.totalvalue]
    for item in range(1,how_many_aces(hisdeck.listofall)):
        if item*10+hisdeck.totalvalue<=21:
            hispossiblesums.append(item*10+hisdeck.totalvalue)
#    print(f"Dealer's possible sums are {hispossiblesums}")
    print ('\n')
    
    
    # In[9]:
    
    #PLAYER'S TURN
    player_lost=False
    
    answer=""
    while player_lost==False:
        print('NOW IS YOUR TURN\n')
        answer=input("Hit or Stay? h/s: ").lower()
        if answer=="h":
            mydeck.addcard()
            print(mydeck.listofall)
            print(mydeck.listofvalues)
            if mydeck.totalvalue<=21:
                possiblesums=[mydeck.totalvalue]
            if how_many_aces(mydeck.listofall)==0:
                print(f'Total value of your cards is {mydeck.totalvalue}\n')
            else:
                print(f'You have {how_many_aces(mydeck.listofall)} aces in your deck. Total value of your cards is at least {mydeck.totalvalue}')
                
                for item in range(1,how_many_aces(mydeck.listofall)):
                    if item*10+mydeck.totalvalue<=21:
                        possiblesums.append(item*10+mydeck.totalvalue)
                print(f'Your possible sums are {possiblesums}\n')
    
            if mydeck.totalvalue>21:
                print ("YOU LOST")
                print(bank.loss())
                player_lost=True
        elif answer=='s':
            break
    
    
    # In[10]:
    #DEALER'S TURN
    
    if player_lost==False:
        print("\nNOW IT'S DEALER'S TURN\n")
        dealer_lost=False
        while dealer_lost==False and player_lost==False:
            decision=random.randint(0,1)
            if mydeck.totalvalue>=hisdeck.totalvalue:
                decision=1
                
            if hisdeck.totalvalue<21 and decision==1:
                print("Dealer decided to hit")
                hisdeck.addcard()
                print(hisdeck.listofall)
                print(hisdeck.totalvalue)
                if hisdeck.totalvalue<=21:
                    hispossiblesums=[hisdeck.totalvalue]
                
                #BELOW IS NEW!!!!!!!!!!!!
                if how_many_aces(hisdeck.listofall)==0:
                    print(f'Total value of his cards is {hisdeck.totalvalue}')
                    print("\n")
                else:
                    print(f'Dealer has {how_many_aces(hisdeck.listofall)} aces in your deck. Total value of his cards is at least {hisdeck.totalvalue}')
                    
                    for item in range(1,how_many_aces(hisdeck.listofall)):
                        if item*10+hisdeck.totalvalue<=21:
                            hispossiblesums.append(item*10+mydeck.totalvalue)
                    print(f"Dealer's possible sums are {hispossiblesums}")
                    print("\n")
                
                
                
        if hisdeck.totalvalue<=21 and decision==0:
            print(hisdeck.listofall)
            print(hisdeck.totalvalue)
            print("\nDealer decided to Stay\n")
            print("\n")
            break
        elif hisdeck.totalvalue>21:
            print("\nDealer lost! You won\n")
            bank.gain()
            dealer_lost=True
        break
    if max(hispossiblesums)==max(possiblesums):
        print ("\nIt's a draw. You gain or loose nothing!\n")
        dealer_lost=True
        break
    elif max(hispossiblesums)>max(possiblesums):
        print("\nDealer won!\n")
        bank.loss()
        player_lost=True
    elif max(hispossiblesums)<max(possiblesums):
        print("\nYou won!\n")
        bank.gain()
        dealer_lost=True
    
    
    # In[ ]:
    playagain=""
    if bank.balance>0:
        while youdied==False:
            playagain=input('DO YOU WANT TO PLAY AGAIN? y/n: ').lower()
            print("\n\n\n\n")
            if playagain=="y":
                break
            elif playagain=="n":
                input("OK SEE YA, SPACE COWBOY!")
                youdied=True
            else:
                print("I DIDN'T GET IT. TRY AGAIN")
                
    else: 
        input("YOU LOST ALL YOUR MONEY! SEE YA, SPACE BUM!")
        youdied=True

    
    
    
