import random 



#check hands
'''
pair = 2 pt
3 of kind = 3 pt
straight = 4 pt
flush = 5 pt
4 of kind = 6pt
full house = 7pt





'''

        

def deck():
    deck = []
    id = 1
    for suit in [' Heart ',' Spade ','Diamond ','Clubs ']:
        for rank in ['Ace ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','11 ','12','13 ']:
            deck.append(rank + suit )
    

    print (deck)
    kk = 0
    while kk < 4 :
        print ("           ")
        kk += 1
        
    random.shuffle (deck)
    return deck

  
    
   
    


def dealCard1():
    p = 0
    player1.append(newDeck[p])
    p += 1
    print (p)
    
def dealCard2():
    q = 1
    player2.append(newDeck[q])
    q += 1
    print (q)
    
###  main    #### main    #### main    ####

newDeck = deck()
print (newDeck)

counter = 0
 
while counter < 5:
        print("                  ")
        counter += 1
        
player1 = []
player2 = []
i = 0

print(player1)

print(player2)

p = 0
q = 1
    
while i<10:
      
    player1.append(newDeck[p])
    p += 2
    print (p)
    
    i += 1
    
    player2.append(newDeck[q])
    q += 2
    print (q)
    
    i += 1

print(player1)

print(player2)

