
 #I, Hung Dam  ID 000736057, declare that all the work presented in here  are my 
#originalwork and codes, and also haven't allowed my work to be copied by anyone
#
#prizes values, #6 is the center postion for start off
#1 = 0
#2 = 100
#3 = 50 
#4 = 1000
#5 = 500
#6 = 0 
#7 = 10000
#8 = 1000 
#9 = 50
#10= 100
#11= 0
#
#
#
#problem 4: Plinko
#welcome to plinko
#you have x many tries, good luck

# tick = from 1-50
# tock 50+ = 50-100

import random
randomNumber = random.randint (1,6)

print ("wheel spinning...")

prizeCount = 6
tries = 0
counter = 0
print ("you have " + str(randomNumber) + " tries, good luck \n (puck drops!)")

prizeDollar = 0

while tries < 5 :
   
    tries +=1
    while counter < randomNumber :
        counter += 1
        genNumber100 = random.randint (1,100)
        prizeCount = 6
        
        if genNumber100 > 50:
            prizeCount += 1
            print ("tock, tick,tock, tick,")
        else:
            prizeCount -= 1
            print ("tick,tock, tick, tock")
            
        if prizeCount == 1:
            print ("you got $0 ")
            prizeDollar += 0
            
        if prizeCount == 2:
            print ("you got $100 ")
            prizeDollar += 100
            
        if prizeCount == 3:
            print ("you got $50 ")
            prizeDollar += 50
           
        if prizeCount == 4:
            print (" you got $1000 ")
            prizeDollar += 1000
            
        if prizeCount == 5:
            print (" you got $500 ")
            prizeDollar += 500
            
        if prizeCount == 6:
            print (" you got $0 ")
            prizeDollar += 0
            
        if prizeCount == 7:
            print (" you got $10000 ")
            prizeDollar += 10000
            
        if prizeCount == 8:
            print ("you got  $1000 ")
            prizeDollar += 1000
            
        if prizeCount == 9:
            print ("you got  $50 ")
            prizeDollar += 50
            
        if prizeCount == 10:
            print ("you got  $100 ")
            prizeDollar += 100
            
        if prizeCount == 11:
            print ("you got  $0 ")
            prizeDollar += 0
            
print (" you won a total of $" + str(prizeDollar) + " dollars, congratulations !")
        
