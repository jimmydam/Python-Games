# I Hung Dam, student 000736057, certify that all code submitted is my own work;
# that I have not copied from any other source. I also certify that I have not 
#allowed my work to be copied by others.

## lab 9

### Tic  Tac  Toe Game ####

############################################################################
############################################################################

def intro():
    print ("Welcome to: \n Tic  Tac  Toe")
    
def ttt():
    print ("Tic  Tac  Toe")

def printScore():

    print (row1)
    print (row2)
    print (row3)

    
##### check  O winner function  ##### check  O winner function   ##### check  O winner function
def checkO():
    #check  row
    if row1[0] == "O" and row1[1] == "O" and row1[2] == "O":
        blankSpace()
        blankSpace()
        printScore()
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        
        exit()

    if row2[0] == "O" and row2[1] == "O" and row2[2] == "O":
        
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        exit()
        
    if row3[0] == "O" and row3[1] == "O" and row3[2] == "O":
        
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        exit()
        
     #check column   
    if row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
        
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        exit()

    if row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
        
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        exit()

    if row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
        
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        exit()
        
     #check diagonal   
    if row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        exit()
        
    if row3[0] == "O" and row2[1] == "O" and row1[2] == "O":
        
        print ( str(player2) + " is the winner !!")
        winner = "yes"
        exit()

    if   playerCounter == 10:
        print ("u loose")

    

    
    
##### check  X winner function  ##### check  X winner function

    #check row
def checkX():
    if row1[0] == "X" and row1[1] == "X" and row1[2] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()

    if row2[0] == "X" and row2[1] == "X" and row2[2] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()
        
    if row3[0] == "X" and row3[1] == "X" and row3[2] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()

     #check column   
    if row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()

    if row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()

    if row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()
        
     #check diagonal   
    if row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()
        
    if row3[0] == "X" and row2[1] == "X" and row1[2] == "X":
        
        print ( str(player1) + " is the winner !!")
        winner = "yes"
        exit()
    if   playerCounter == 10:
        print ("u loose")
    


        
######## insert  and remove function  ###### #########
def checkLetter():
    if choice == "a" and letter[0] == "a":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "b" and letter[1] == "b":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "c" and letter[2] == "c":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "d" and letter[3] == "d":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "e" and letter[4] == "e":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "f" and letter[5] == "f":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "g" and letter[6] == "g":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "h" and letter[7] == "h":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2
    if choice == "i" and letter[8] == "i":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2


    
    else:      
    
        blankSpace()
        blankSpace()
        printScore()
        print ("WARNING !!!! the letter '" + str(choice) + "' has been chosen pick another letter ")
                
        checkX()
        checkO()


            
################## x's turn , perform these function ######### ######## x's turn , perform these function ###################################################################    
def xTurn():
    tries = 0
    while tries < 1:
        print ("it is " + str(player1) + "'s  turn" )
        p = "X"        
        choice = input ("pick a letter between a - i")
        if choice == "a" and letter[0] == "a":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2

        if choice == "b" and letter[1] == "b":  
            row1.remove ("b")
            row1.insert (1,p)
            letter[1] = "taken"
            tries +=2

        if choice == "c" and letter[2] == "c":
            row1.remove ("c")
            row1.insert (2,p)
            letter[2] = "taken"
            tries +=2

        if choice == "d" and letter[3] == "d":
            row2.remove ("d")
            row2.insert (0,p)
            letter[3] = "taken"
            tries +=2

        if choice == "e" and letter[4] == "e":
            row2.remove ("e")
            row2.insert (1,p)
            letter[4] = "taken"
            tries +=2

        if choice == "f" and letter[5] == "f":
            row2.remove ("f")
            row2.insert (2,p)
            letter[5] = "taken"
            tries +=2

        if choice == "g" and letter[6] == "g":
            row3.remove ("g")
            row3.insert (0,p)
            letter[6] = "taken"
            tries +=2

        if choice == "h" and letter[7] == "h":
            row3.remove ("h")
            row3.insert (1,p)
            letter[7] = "taken"
            tries +=2

        if choice == "i" and letter[8] == "i":
            row3.remove ("i")
            row3.insert (2,p)
            letter[8] = "taken"
            tries +=2


    
        else:      
        
            blankSpace()
            blankSpace()
            printScore()
            print ("WARNING !!!! the letter '" + str(choice) + "' has been chosen pick another letter ")
                    
            checkX()
            checkO()
        
            
                 
######## o's turn , perform these function ######### ######## 0's turn , perform these function ######### 
def oTurn():
    tries = 0
    while tries < 1:
        print ("it is " + str(player2) + "'s  turn" )
        p = "O"        
        choice = input ("pick a letter between a - i")
        if choice == "a" and letter[0] == "a":
            row1.remove ("a")
            row1.insert (0,p)
            letter[0] = "taken"
            tries +=2

        if choice == "b" and letter[1] == "b":  
            row1.remove ("b")
            row1.insert (1,p)
            letter[1] = "taken"
            tries +=2

        if choice == "c" and letter[2] == "c":
            row1.remove ("c")
            row1.insert (2,p)
            letter[2] = "taken"
            tries +=2

        if choice == "d" and letter[3] == "d":
            row2.remove ("d")
            row2.insert (0,p)
            letter[3] = "taken"
            tries +=2

        if choice == "e" and letter[4] == "e":
            row2.remove ("e")
            row2.insert (1,p)
            letter[4] = "taken"
            tries +=2

        if choice == "f" and letter[5] == "f":
            row2.remove ("f")
            row2.insert (2,p)
            letter[5] = "taken"
            tries +=2

        if choice == "g" and letter[6] == "g":
            row3.remove ("g")
            row3.insert (0,p)
            letter[6] = "taken"
            tries +=2

        if choice == "h" and letter[7] == "h":
            row3.remove ("h")
            row3.insert (1,p)
            letter[7] = "taken"
            tries +=2

        if choice == "i" and letter[8] == "i":
            row3.remove ("i")
            row3.insert (2,p)
            letter[8] = "taken"
            tries +=2
        


    
        else:      
        
            blankSpace()
            blankSpace()
            printScore()
            print ("WARNING !!!! the letter '" + str(choice) + "' has been chosen pick another letter ")
                    
            checkX()
            checkO()
        
### this is the funniest function ever ###  ### this is the funniest function ever ###   ### this is the funniest function ever ###
def blankSpace():
    print ("                                        \
                                                     \
                                                \
                                                                \
                                                ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")
    print ("                                        \
                                                         \
                                                    \
                                                                    \
                                                    ")


 
####### Main############# Main ######## Main ############# Main############# Main ######## Main ########### Main############# Main ######## Main #########        
####### Main############# Main ######## Main ############# Main############# Main ######## Main ########### Main############# Main ######## Main #########
####### Main############# Main ######## Main ############# Main############# Main ######## Main ########### Main############# Main ######## Main #########

row1 = ["a","b","c"]
row2 = ["d","e","f"]
row3 = ["g","h","i"]

winner = "no"
playerCounter = 0
letter = ["a","b","c","d","e","f","g","h","i"]

intro()

player1= input("Welcome player 1, what is your name?")
player2 = input("Welcome player 2, what is your name?")

################################################################################################################
        
while True:
    turnCounter = 1
    if   playerCounter == 10: break
    ##X turn
    turnCounter += 1
    if playerCounter == 1 or playerCounter == 3 or playerCounter == 5 \
       or playerCounter == 7 or playerCounter == 9:
        
        xTurn()
    ## O turn
    if playerCounter == 2 or playerCounter == 4 or playerCounter == 6 \
       or playerCounter == 8:
        
        oTurn()
    
    blankSpace()
    blankSpace()
    ttt()
    printScore()
    checkX()
    checkO()
    
        
    
    
    

    
        
    playerCounter += 1
    
        
if  playerCounter == 10:    print ("Sorry, you both had better days... insert 2 more quarters to continue!!")   
    
    
    
    
#################################    
    
    
    

    



