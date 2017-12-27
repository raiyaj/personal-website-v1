##### Cmpt120 - Final Assignment
##### Author: Raiya Jessa
##### Student Id: 301281066
##### Planets, Aliens and Explosions Game




# ///////////////////////////// FUNCTIONS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ///////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def read_string_list_from_file(the_file):
    '''
    CODE PROVIDED TO INCORPORATE
    
    <file-name including extension .txt>(String) --> List of strings
    
    Assumptions:
    1) the_file is in the same directory as this program 
    2) the_file contains one planet data per line 
    3) after the data of each planet in the file  there is a return 
      (so that the next planet is in the next line), and also
      there is (one single) return after the last planet in the_file

    To call or invoke this function:
    listStrings = read_string_list_from_file(<file-name.txt in quotes>)
    using the data provided the call to this function would be:
    
    listStrings = read_string_list_from_file("planetsData1.txt")
    '''
    
    fileRef = open(the_file,"r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list
        
    fileRef.close()  

    #........
    #print ("\n JUST TO TRACE, the local list of strings is:\n")
    #for element in localList:
    #    print (element)
    #print ()
    #........
        
    return localList


def create_lists_board(listStrings):
    '''
    Assumptions:
    
    1) The listStrings parameter will have a list with the strings,
    2) each string corresponds to the data for one planet
    3) string for each planet is:  civlevel-fuel-rocks
    4) civlevel, fuel and rocks are integer numbers each

    (lis) --> (lis,lis,lis,lis)
    '''
    # RECOMMENDED THAT YOU IMPLEMENT THIS
    # your code will process the  parameter list and return 3 lists:
    # one to represent the board
    # one for the civilization level in each planet,
    # one for the fuel liters in each planet, etc.

    #!!!! NOTE: I return the 4 lists, but receive them in the top level
    #with only 1 variable. So my board data is stored in a matrix!!!!

    planetList=[]
    civList=[]
    fuelList=[]
    rocksList=[]
    for r in range(len(listStrings)):
        planetList.append(r)
        civList.append(int(listStrings[r][0]))
        if (listStrings[r][3].isdigit()):
            fuelList.append(int(listStrings[r][2:4]))
            rocksList.append(int(listStrings[r][5::]))
        else:
            fuelList.append(int(listStrings[r][2]))
            rocksList.append(int(listStrings[r][4::]))
    return planetList,civList,fuelList,rocksList


def showBoard(title,mat):
    '''
    Call this fxn each time board shown to user. Parameter 'title'
    indicates what board looks like at different points in the game
    (eg. 'after creation' or 'before turn x').

    (str,mat) --> ()
    '''
    print ("\nShowing board... " + title)
    print ("\n Currently, the board contains...")
    print ("\tPlanet#\t\t",end="")
    print ("Civ. Level\t",end="")
    print ("Fuel\t",end="")
    print ("\tRocks\t")
    for r in range(len(mat[0])):
        for c in range(len(mat)):
            if (c==3 and title != "just created"):
                if (player_position == mat[0][r]):
                    if (pythonPlanet == mat[0][r] and pythonPlanet != 0):
                        print ("\t",mat[c][r],"\t<=== PythonPlanet \
<--- Astronaut",end="")
                    else:
                        print ("\t",mat[c][r],"\t<--- Astronaut",end="")
                elif (pythonPlanet == mat[0][r] and pythonPlanet != 0):
                    print ("\t",mat[c][r],"\t<=== PythonPlanet",end="")
                else:
                    print ("\t",mat[c][r],"\t",end="")
            else:
                print ("\t",mat[c][r],"\t",end="")
        print()
    return 


def validate_data_file(st):
    '''
    Ensures user either types 'd' for default, or provides a filename ending
    with '.txt'
    
    Assumption: If user does type a '.txt' file name, that the file is
    in required format and located in same folder as this program
    
    (str) --> (str)
    '''
    while (st not in "dD" and st[-4::] != ".txt"):
        print ("\nWhat you typed is not what was expected; please retype.")
        st = input("Type name of board data file including '.txt' or \
type 'd' for default: ")
    return st


def createRangeSt(a,b):
    '''
    A productive fxn that creates a string version of the range of a to b,
    which are parameters. This fxn is called by validate_nums_in_range() below.
    
    (int,int) --> (st)
    '''
    range_string=""
    for i in range(a,b):
        range_string += str(i) + ","
    return range_string


def validate_nums_in_range(st,a,b,prompt):
    '''
    Fxn checks whether user types a positive integer in the correct range.
    Parameter 'st' referes to user's initial response, and parameter 'prompt'
    is the question re-asked for as long as an invalid response is given.
    Returns final answer.
    
    (str,int,int,str) --> (str)
    '''
    while (st not in createRangeSt(a,b) and st != str(b) or st in
           createRangeSt(0,a)):
        if (st.isdigit() and int(st) not in range(a,b+1)):
            print ("\nThe value isn't within the required range; please retype.")
            st = input(prompt)
        else:
            print ("\nWhat you typed isn't a positive integer; please retype.")
            st = input(prompt)
    return st


def validate_AorB(st,prompt,a,b):
    '''
    Called whenever user is asked to type either 'a' or 'b'. Paramet 'st'
    refers to the user's initial input, and parameter 'prompt' is the question
    re-asked for as long as an invalid response is given. Returns final answer.
    
    (str,str,str,str) --> (str)
    '''
    correct_answers = a + b + a.upper() + b.upper()
    while (st not in correct_answers):
        print ("\nWhat you typed isn't what was expected; please retype.")
        st = input(prompt)
    return st


def showAstronaut():
    '''
    Void fxn that simply prints the player's current info
    
    () --> ()
    '''
    print ("\nShowing astronaut's info... about to do turn num:",turnNumber)
    print ("\nThe astronaut",playerName,"has civilization level:",pCivLevel)
    print ("is in position:",player_position)
    print ("currently has:",pFuel,"fuel liters")
    print ("and until and including this turn, has collected",\
           pRocks,"rock specimens.")
    print ("So, she is alive and ready to keep moving!")
    return


def showAstronaut_EndOfGame():
    '''
    Void fxn that simply prints the player's current info (at end of game)
    
    () --> ()
    '''
    print ("\nShowing astronaut's info... end of game")
    print ("\nThe astronaut",playerName,"has civilization level:",pCivLevel)

    if (win_game == True):
        print ("currently has: 9999 fuel liters.")
        print ("and collected, during the whole game, 9999 rock specimens.")
        print ("So, she's very alive, and also reached PythonPlanet, so \
she won!!!")
    elif (lose_game == True):
        if (pFuel == 0):
            print ("But ran out of fuel and got stranded.")
        else:
            print ("But died in an amazing explosion!")
        print ("and collected, during the whole game,",pRocks,"rock specimens.")
        print ("And she cannot move anymore since the game is over.")
    else:
        print ("is in position",player_position)
        print ("currently has:",pFuel,"fuel liters.")
        print ("and collected, during the whole game,",pRocks,"rock specimens.")
        print ("So, she is very alive, but cannot move anymore since the \
game is over!")
    if (optionAmazExplo in "yY"):
        print (numberOfAmazExplos,"amazing explosions took place, \
each time eliminating a planet and adding rocks to nearby planets.")
    if (optionMildExplo in "yY"):
        print (numberOfMildExplos,"mild explosions took place, each time \
adding rocks to nearby planets.")
    return
                   

def advance_circularly_list(pos,advance):
    '''
    Productive fxn called by rollDieOrChoose() below (if user chooses to
    roll the die), that receives the list of planet positions as a parameter,
    and returns astronaut's new position. Parameter 'pos' is player's current
    position, and parameter 'advance' is result of rolling die.

    (lis,int,int) --> (int)
    '''
    if (pos < 0 or pos >= len(matrix[0])):
        res = -1
    else:
        res = (pos + advance) % len(matrix[0])
    return res


def rollDieOrChoose(old_pos):
    '''
    Fxn allows user to either roll die or choose which planet to go to next.
    Parameter 'old_pos' actually refers to player's current position.
    
    (int,lis) --> (int)
    '''
    option_Die_or_Choose=input("\nRoll the die, or choose \
which planet to travel to next (d/p)? ")
    option_Die_or_Choose=validate_AorB(option_Die_or_Choose,"Roll the \
die, or choose which planet to travel to next (d/p)? ","d","p")
    if (option_Die_or_Choose in "dD"):
        die = r.randint(1,6)
        print ("\n  the die was...",die)
        print ("  the previous position was...",old_pos)
        new_pos=advance_circularly_list(old_pos,die)
        print ("  and the next position is...",new_pos)
    else:
        #current length of board calculated in case amazing explosions took
        #place and board shrunk
        current_length_of_board = len(matrix[0]) - 1
        prompt = "Which planet should the astronaut go to (0.." + \
                 str(current_length_of_board) + ")? "
        new_pos=input(prompt)
        new_pos=validate_nums_in_range(new_pos,0,\
                                       current_length_of_board,prompt)
    return new_pos


def alienEncounter(mat,civlev,pos):
    '''
    Fxn called during each of player's turns. Depending on whether player's
    civilization level is > or < or = to planet's, player's fuel (pFuel,
    which is a global variable) is modified as necessary. The planet's amount
    of fuel is also adjusted as needed, but the matrix containing the board's
    info isn't a global variable because the parameter 'mat' acts as an
    alias for it.
    
    (lis,int,int) --> ()
    '''
    global pFuel
    if (mat[1][pos] == 0):
        print ("\n\nThere are no aliens on this planet, so its civilization \
level is 0")
    else:
        print ("\n\nThere are aliens on this planet, with civilization \
level",mat[1][pos])
    if (civlev < mat[1][pos]):  #player loses fuel
        fuel_lost_less = r.randint(1,pFuel)
        pFuel = pFuel - fuel_lost_less
        print ("\nOh no, the astronaut is less civilized than the aliens \
and lost",fuel_lost_less,"fuel liters!")
        print("\nThe astronaut now has",pFuel,"fuel liters.")
    elif (civlev == mat[1][pos]):  #player maybe loses fuel
        if (mat[1][pos] == 0):
            print ("\nHmmm...the astronaut is equally civilized as the \
planet,",end="")
        else:
            print ("\nHmmm...the astronaut is equally civilized as the \
aliens,",end="")
        if (pFuel == 1): #situation where pFuel = 1.
            #would result in empty range error! so randint(1,2) gives a 50%
            #chance of losing that 1 fuel liter.
            fuel_lost_equal = r.randint(1,2)
            if (fuel_lost_equal == 1):
                print (" and luckily doesn't lose any fuel.")
                print("\nThe astronaut still has",pFuel,"fuel liters.")
            else:
                pFuel = 0
                print (" but lost 1 fuel liter.")
                print("\nThe astronaut now has 0 fuel liters.")
        else:
            fuel_lost_equal = r.randint(1,pFuel//2)
            pFuel = pFuel - fuel_lost_equal
            print (" but lost",fuel_lost_equal,"fuel liters.")
            print("\nThe astronaut now has",pFuel,"fuel liters.")
    else:  #player collects fuel (if any on planet), planet loses fuel
        if (mat[1][pos] == 0):
            print ("\nGreat, the astronaut is more civilized than the planet!")
        else:
            print ("\nGreat, the astronaut is more civilized than the aliens!")
        if (mat[2][pos] == 0):
            print ("Too bad the planet has no fuel to give!")
            print("\nThe astronaut still has",pFuel,"fuel liters.")
        else:
            fuel_gained = r.randint(1,mat[2][pos]) 
            pFuel = pFuel + fuel_gained
            mat[2][pos] = mat[2][pos] - fuel_gained
            print ("\nThe astronaut won",fuel_gained,"fuel liters.")
            print ("The planet",pos,"now has",mat[2][pos],"fuel liters.")
            print("\nThe astronaut now has",pFuel,"fuel liters.")
    return


def collectRocks(mat,pos):
    '''
    If player is still alive after encountering aliens, this void fxn allows
    them to collect rocks from planet. Parameter 'pos' refers to astronaut's
    position. Here, pRocks is a global variable bc its value changes, and the
    planet's rocks are also modified, but via alias 'mat'

    (mat,int) --> ()
    '''
    global pRocks
    rocks_gained = mat[3][pos]//3
    pRocks.append(rocks_gained)
    mat[3][pos] = mat[3][pos] - rocks_gained
    if (mat[3][pos] == 0):
        print ("\nToo bad the planet has no rocks for the astronaut to collect!")
        print ("So, her rock collection is now",pRocks)
    elif (rocks_gained == 0):
        print ("\nAh well, the astronaut didn't collect any rocks.")
        print ("So, her rock collection is now",pRocks)
        print ("The planet",pos,"still has",mat[3][pos],"rocks.")
    else:
        print ("\nWoohoo, the astronaut collected",rocks_gained,"rocks!")
        print ("So, her rock collection is now",pRocks)
        print ("The planet",pos,"now has",mat[3][pos],"rocks.")
    return


def rocks_sum_decreasing(n,mat):
    '''
    A void fxn, called when a mild/amazing explosion takes place, to increase
    amount of rocks from planet 1 to the exploding planet. Called by
    explosions() below. Parameter 'n' is the exploding planet, and parameter
    'mat' is alias for the board's matrix. 

    (int,mat) --> ()
    '''
    for i in range(n-1):    #n-1 because we want to exclude planet 0
        inner_sum=0
        for r in range(i+1,n+1):    #i+1 because want to exclude planet 0, and
            #n+1 because want to include position of the exploding planet 
            inner_sum += mat[3][r]
        mat[3][i+1] = inner_sum    #i+1 because again excluding planet 0
    return
       

def explosions(mat):
    '''
    Productive fxn that calls rocks_sum_decreasing() and updates boaard.
    Then, if user wants amazing explosions, the exploding planet disappears.
    Global variables player_position, lose_game and pythonPlanet are needed
    as they must be updated when a planet disappears.

    Fxn is productive and returns the new matrix.
    
    (mat) --> (mat)
    '''
    global player_position
    global lose_game
    global pythonPlanet
    global numberOfMildExplos
    global numberOfAmazExplos
    
    #MILD EXPLOSIONS:
    if (len(mat[0]) > 1): #condition stops explosions from happening if planet 0
        #is the only planet left
        exploding_planet = r.randint(1,len(mat[0])*int(optionExploFrequency))
        if (exploding_planet < len(mat[0])):
            rocks_sum_decreasing(exploding_planet,mat)
            print ("\nOoooohh, a mild or amazing explosion is happening \
right now in planet #",exploding_planet)
            print ("More rock specimens might've been added to the board!")

            if (optionMildExplo in "yY"):
                numberOfMildExplos += 1
                mildExploTitle = "after mild explosion, still in turn num: " + \
                        str(turnNumber)
                showBoard(mildExploTitle,mat)
                return mat
            
            else:   #AMAZING EXPLOSIONS:
                numberOfAmazExplos += 1
                print ("\nWoah! An amazing explosion just took place in planet #",\
                       exploding_planet)
                print ("This planet will disappear, so the board will shrink.")
                if (player_position == exploding_planet):
                    #astronaut dies in amazing explosion
                    print ("Unfortunately, the astronaut was on that planet, \
and died in the explosion!")
                    lose_game = True
                    player_position = 10   #this is so that '<--- Astronaut'
                    #won't get printed on the board if astronaut dead in explosion
                elif (player_position > exploding_planet):
                    #astronaut's position decreases bc exploding planet disappears
                    print ("The astronaut wasn't there, but her position \
changed, and is now",player_position - 1)
                    player_position = player_position - 1
                else:
                    print ("Luckily, the astronaut wasn't there, so she wasn't \
affected.")
                if (exploding_planet == pythonPlanet):
                    pythonPlanet = len(mat[0])
                    print ("Oh no, PythonPlanet exploded and is now gone from \
the board!")
                if (pythonPlanet > exploding_planet):
                    #PythonPlanet's position decreases bc exploding
                    #planet disappears
                    pythonPlanet = pythonPlanet - 1


                #code to make exploding planet disappear.
                #this is done by creating a new list.
                new_mat_outer=[]
                for c in range(len(mat)):
                    new_mat_inner=[]
                    for row in range(len(mat[0])):
                        if (exploding_planet != row):
                            if (mat[0][row] > exploding_planet):
                                mat[0][row] = mat[0][row] - 1
                                #this if statement is to make the positions of
                                #planets bigger than exploding planet decrease
                                #by 1
                            new_mat_inner.append(mat[c][row])
                    new_mat_outer.append(new_mat_inner)

                
                amazExploTitle = "after amazing explosion, still in turn num: " + \
                str(turnNumber)
                showBoard(amazExploTitle,new_mat_outer)
                return new_mat_outer

        else:
            return mat
                                    

def convert_rocks_to_binary():
    '''
    Converts rocks list from final game board into a binary list. Displayed in
    the End of all games info.

    () --> (lis)
    '''
    res=[]
    for i in range(len(matrix[3])):
        res.append(matrix[3][i] % 2)
    return res


def convert_base2_to_base10():
    '''
    Productive fxn which uses list received from convert_rocks_to_binary()
    and calculates its corresponsing integer in base 10.

    () --> (int)
    '''
    res=0
    reverse_i = len(binary_list)
    for i in range(len(binary_list)):
        reverse_i = reverse_i-1
        res = res + binary_list[i] * (2**reverse_i)
    return res




# ///////////////////////////// TOP LEVEL \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ///////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import random as r
import sys

print ("\nWelcome to my Cmpt120 game! Good luck!")
print ("==================================================================")


#-----ask if user wants to play, w/ validation-----
optionPlay=input("\nDo you want to play (y/n)? ")
while (optionPlay != "y" and optionPlay != "Y"):
    if (optionPlay == "n" or optionPlay == "N"):
        print ("Consider playing next time, then! \nBye :)")
        sys.exit()  #ends program
    else:
        print ("\nWhat you typed is not what was expected; please retype.")
        optionPlay=input("Do you want to play (y/n)? ")      


#-----outer while loop containing the whole game (which can be played
#repeatedly if the user wants)-----

optionPlayAgain = "y"
gameNumber = 0
numberOfWins = 0
while (optionPlayAgain in "yY"):
    gameNumber += 1


    #-----set up initial board-----

    player_position=0
    optionData=input("\nType name of board data file including '.txt' or \
type 'd' for default: ")
    optionData=validate_data_file(optionData)
    if (optionData == "d"):
        initialStrings = read_string_list_from_file("planetsData1.txt")
    else:
        initialStrings = read_string_list_from_file(optionData)

    #board data stored in a matrix
    matrix=create_lists_board(initialStrings)
    showBoard("just created",matrix)
        
    pythonPlanet = input("\nWhich planet should be PythonPlanet (0..7, 0 having \
no effect)? ")
    pythonPlanet=validate_nums_in_range(pythonPlanet,0,7,"Which planet should \
be PythonPlanet (0..7, 0 having no effect)? ")
    pythonPlanet=int(pythonPlanet)

            
    #-----ask user initial player info, w/ validation-----

    print ("\nPlayer information...")
    playerName = input("Name? ")

    optionCivLevel = input("\nCivilization level (0..3)? ")
    optionCivLevel=validate_nums_in_range(optionCivLevel,0,3,"Civilization \
level (0..3)? ")

    optionFuel = input("\nInitial fuel liters (10..50)? ")
    optionFuel=validate_nums_in_range(optionFuel,10,50,"Initial fuel liters \
(10..50)? ")

    maxTurns = input("\nMaximum turns this game (1..10)? ")
    maxTurns=validate_nums_in_range(maxTurns,1,10,"Maximum turns this game \
(1..10)? ")


    #-----ask user about explosion preferences, w/ validation-----
    optionAmazExplo = input("\nAllow Amazing Explosions to occur (y/n)? ")
    optionAmazExplo=validate_AorB(optionAmazExplo,"Allow Amazing Explosions \
to occur (y/n)? ","y","n")
    if (optionAmazExplo in "yY"):
        optionMildExplo="n"
    else:
        optionMildExplo = input("Since you don't want amazing explosions \
to happen, would you allow Mild Explosions (y/n)? ")
        optionMildExplo=validate_AorB(optionMildExplo,"Allow Mild Explosions \
to occur (y/n)? ","y","n")
    if (optionAmazExplo in "yY" or optionMildExplo in "yY"):
        optionExploFrequency = input("\nFrequency of explosions (1..5)? ")
        optionExploFrequecy = validate_nums_in_range(optionExploFrequency,\
        1,5,"Frequency of explosions (1..5)? ")


    #-----prepare variables for board. Note: pCivLevel, pFuel, pRocks refer to
    #player's civ level, fuel and rocks. All of the board's data is stored
    #in a matrix, which was created above when setting up the initial board.-----
    turnNumber=1
    pCivLevel=int(optionCivLevel)
    pFuel=int(optionFuel)
    pRocks=[]
    win_game=False      #flag
    lose_game=False     #flag
    numberOfMildExplos = 0
    numberOfAmazExplos = 0


    #-----inner while loop containing the actual turns in the game-----
    while (turnNumber <= int(maxTurns) and win_game==False and lose_game==False):
        turnTitle="about to do turn num: "+str(turnNumber)
        showBoard(turnTitle,matrix)
        showAstronaut()
        if (optionAmazExplo in "yY" or optionMildExplo in "yY"):
            matrix = explosions(matrix)
            if (player_position == pythonPlanet and pythonPlanet != 0):
                print ("\n\nSweet! The astronaut arrived in PythonPlanet and \
has won the game!")
                win_game = True
                numberOfWins += 1
        if (win_game == False and lose_game == False):
            turnNumber+=1
            player_position=int(rollDieOrChoose(player_position))
            if (player_position == pythonPlanet and pythonPlanet != 0):
                print ("\n\nSweet! The astronaut arrived in PythonPlanet and \
has won the game!")
                win_game = True
                numberOfWins += 1
            else:
                alienEncounter(matrix,pCivLevel,player_position)
                if (pFuel == 0):
                    print ("\n\nUh oh, the astronaut has run out of fuel, so \
she's stranded and doesn't collect any rocks. Game over.")
                    lose_game = True
                else:
                    collectRocks(matrix,player_position)


    #-----End of game results displayed to user-----
    print ("\n\nRESULTS: END OF GAME")
    print ("\nGame number",gameNumber,"just took place.")

    if (lose_game == True):
        reason_game_ended = "the astronaut either got stranded or died."
    elif (win_game == True):
        reason_game_ended = "the astronaut reached PythonPlanet!"
    else:
        reason_game_ended = "the maximum number of turns was reached."
    print ("The game ended because",reason_game_ended)
    
    showBoard("end of game",matrix)
    showAstronaut_EndOfGame()

    optionPlayAgain = input("\nDo you want to play again (y/n)? ")
    optionPlayAgain = validate_AorB(optionPlayAgain,"Do you want \
to play again (y/n)? ","y","n")


#-----End of ALL games results + binary conversion -----
print ("\n\nRESULTS: END OF ALL GAMES")
print ("\nYou played",gameNumber,"games in total.")
print ("Of those, the astronaut won",numberOfWins)
print ("To conclude, my program will do a conversion from binary to decimal,\
 based off of the list of rock specimens from the last game board!")
print ("\n  List of rock specimens:",matrix[3])
binary_list = convert_rocks_to_binary()
print ("  Its corresponding binary list:",binary_list)
base_ten_list = convert_base2_to_base10()
print ("  Which, converted to base 10, is:",base_ten_list)

print ("\n\nFIN.")
