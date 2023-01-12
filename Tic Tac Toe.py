#!/usr/bin/env python
# coding: utf-8

# In[1]:


#THE GAME OF TIC TAC TOE (VS PLAYER)


# In[2]:


class Board():
    def __init__(self):
        self.emptycell="|_|"
        self.row3=[self.emptycell for item in range(3)]
        self.row2=[self.emptycell for item in range(3)]
        self.row1=[self.emptycell for item in range(3)]
        self.values=[["|7|","|8|","|9|"], ["|4|", "|5|", "|6|"], ["|1|", "|2|", "|3|"]]

    def move(self,position,symbol):
        if symbol=="|x|":
            print("\nFirst player does his move\n")
        elif symbol=="|o|":
            print("\nSecond player does his move\n")
            
        if position <=9 and position >6:
            self.values[0][position-7]=symbol


        elif position <=6 and position >3:
            self.values[1][position-4]=symbol

        elif position <=3:
            self.values[2][position-1]=symbol
        
                



    def printboard(self):
        print("""
        
        
""")
        for item1 in self.values:
            for item2 in item1:
                print (item2, end=" ")
            print("\n")

    def checkrows(self):
    
        for item in self.values:
            if item ==["|x|", "|x|", "|x|"]:
                print("First player wins")
                #global game
                return False
                break

            if item ==["|o|", "|o|", "|o|"]:
                print ("Second player wins!")
                #global game
                return False
                break

    def checkcolumns (self):
        counter=0
        
        while counter<3:
            
            column=[item[counter] for item in self.values]
            
            if column ==["|x|", "|x|", "|x|"]:
                print("First player wins!!")
                #global game
                return False
                break

            if column ==["|o|", "|o|", "|o|"]:
                print ("Second player wins!!!")
                #global game
                return False
                break
            counter+=1
    
    def checkdiagonal(self):
        
#first diagonal assessment
        diagonal1=[]
        counter=0
        while counter<3:
            for item in self.values:
                diagonal1.append(item[counter])
                counter+=1
    
#second diagonal assesment
        counter=2      
        diagonal2=[]
        while counter>-1:
            
            for item in self.values:
                diagonal2.append(item[counter])
                counter-=1
#        print("First diagonal is {} and second is {}".format(diagonal1, diagonal2))
                
        if diagonal1 ==['|x|', '|x|', '|x|'] or diagonal2==['|x|', '|x|', '|x|']:
                print("First player wins!!")
                #global game
                return False
            
        if diagonal1 == ["|o|", "|o|", "|o|"] or diagonal2 ==["|o|", "|o|", "|o|"]:
                print ("Second player wins!!!")
                #global game
                return False


# In[3]:


def gameloop(): 
    print("\n              STARTING A NEW GAME\n\n")
#turn counter
    turn=1
#create myboard    
    myboard=Board()
    myboard.printboard()
#Start the gameplay loop

    while True:
#First player turn
        while True:
            a=int(input("\nFirst player, enter your position: "))
            if (a <=9 and a >6) and (myboard.values[0][a-7]=='|x|' or myboard.values[0][a-7]=='|o|'):
                print(f"\n{myboard.values[0][a-7]}")
                print ("This square is already occupied!!! Try again!!!")
                myboard.printboard()
                continue
            elif (a <=6 and a >3) and (myboard.values[1][a-4]=='|x|' or myboard.values[1][a-4]=='|o|'):
                print(f"\n{myboard.values[1][a-4]}")
                print ("This square is already occupied!!! Try again!!!")
                myboard.printboard()
                continue
            elif a <=3 and (myboard.values[2][a-1]=='|x|' or myboard.values[2][a-1]=='|o|'):
                print(f"\n{myboard.values[2][a-1]}")
                print ("This square is already occupied!!! Try again!!!")
                myboard.printboard()
                continue
            else:
                myboard.move(a, "|x|")
                myboard.printboard()
                break
                
#check if the square is not already occupied
        if turn>=3 and (myboard.checkcolumns()==False or myboard.checkrows()==False or myboard.checkdiagonal()==False):

            break

        
#Second player turn
        while True:
            b=int(input("\nSecond player enter your position: "))
            if (b <=9 and b >6) and (myboard.values[0][b-7]=='|x|' or myboard.values[0][b-7]=='|o|'):
                print(f"\n{myboard.values[0][b-7]}")
                print ("This square is already occupied!!! Try again!!!")
                myboard.printboard()
                continue
            elif (b <=6 and b >3) and (myboard.values[1][b-4]=='|x|' or myboard.values[1][b-4]=='|o|'):
                print(f"\n{myboard.values[1][b-4]}")
                print ("This square is already occupied!!! Try again!!!")
                myboard.printboard()
                continue
            elif b <=3 and (myboard.values[2][b-1]=='|x|' or myboard.values[2][b-1]=='|o|'):
                print(f"\n{myboard.values[2][b-1]}")
                print ("This square is already occupied!!! Try again!!!")
                myboard.printboard()
                continue
            else:
                myboard.move(b, "|o|")
                myboard.printboard()
                break
                

#check if the square is not already occupied
        if turn==3 and (myboard.checkcolumns()==False or myboard.checkrows()==False or myboard.checkdiagonal()==False):
            break
        
        turn+=1

    
        


# In[4]:


gameloop()
while True:
    answer=input("\nDo you wat to play again? y/n: ")
    if answer[0].lower() =="y":
        gameloop()
    else:
        input("\nSee ya!")
        break


# In[ ]:





# In[ ]:




