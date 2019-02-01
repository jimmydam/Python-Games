#blackjack game by JImmy Dam  #blackjack game by JImmy Dam
 
import random


def dealDealerCards():
    dc.append(random.randint(1,11))

def dealPlayerCards():
    pc.append(random.randint(1,11))

def sumPc():
        return sum(pc)
def Hit():
     pc.append(random.randint(1,11))
     
def Hit2():
     dc.append(random.randint(1,11))

def blankScreen():
    i = 0
    while i <= 3:
        print ("                                                        ")
        i += 1
def blankScreen2():
    i = 0
    while i <= 1:
        print ("                                                        ")
        i += 1    
      
###main###########main######main###########main######main###########main###

dc = []
pc = []
counter = False
counter2 = False

while len(dc) != 2:
    dealDealerCards()
    
print ("the dealer has X and " + str(dc[1]))

while len(pc) != 2:
    dealPlayerCards()

print ("you were dealt " +  str(pc))

Player = sumPc()

print ("you  have " + str(Player) )
blankScreen()

 
###player hit
while ( (counter == False) and(sum(pc) <= 21) ):
    HitQ = input ("do you want to hit?") 
    if HitQ == "hit":
        Hit()
        blankScreen2()
        print ("you  have " + str(sum(pc)))
        print (pc)
        
        print ("the dealer has X and " + str(dc[1]))
        if sum(pc) == 21:
            print ("you are a winner")

        else:
            counter = False
            
    elif HitQ == "stay":
        counter = True
    elif sum(pc) == 21 :
        print ("you are a winner")
        print ("the dealer has " + str(dc))
        blankScreen2()
        
    else:
        counter = True

###dealer hit
while (counter2 == False):
    if ( sum(dc) < 17):
        print(dc)
        print ("dealer will hit")
        Hit2()
        blankScreen2()

        print(dc)
        print (sum(dc))

    elif (sum(pc)> sum(dc) and (sum(pc) <= 21)):
        print (" you are the winner")
        print ("the dealer has " + str(dc))

    else:       
        print ("you loose")
        counter2 = True
