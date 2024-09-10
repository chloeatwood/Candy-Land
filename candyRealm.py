# <Chloe Atwood>             <04/17/2024>
# <Assignment 6>
#Description: A copy of the game Candy Land using colorama



import random
import copy
import colorama
from colorama import Fore, Back, Style

#This function will print the main menu and the options as well as take the input
    #for what the user wants to do
def printOptions():
    #Printing out the main menu and options
    print()
    print("------------------------------------------------------------")
    print("MAIN MENU: What would you like to do?")
    #Asking what the user would like to do
    choice = str(input("[p]lay game, [i]nstructions, or [q]uit:"))
    #Returning the users decision
    return choice

#This Function will print all the title material for the game
def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("Candy Realm!")
    print()

    print("By: Chloe Atwood>")
    print("[COM S 127 <A>]")
    print()

#This function prints out all the instructions to the game
def printIntructions():
    print()
    print("-------------------------------------------")
    print("             Instructions")
    print("Players:\n")
    print("     May play with 2 - 4 human players or\n"
          "         1 human player against the computer\n")
    print("Playing the Game:\n")
    print("   1) Select a Character\n"
            '   2) Pick a card and move to the color on the\n'
            '          board closest to you that matches that color\n'
            '   3) The first person to reach the end wins!\n')
    print("Rules:\n"
          '   1) If you land on licorice your next turn gets skipped\n'
            '   2) If you land on a shortcut you will get moved further\n'
            '   3) If you draw a card with a location on it you will\n'
             '        get moved to that location even if that location is behind you\n'
            '   4) These are not shown on the board, They will be randomized surprises\n'
             '        each game\n')


#This function gets the amount of players that will be playing the game and
    #validates that information
def playerAmount():
    while True:
        try: 
            players = int(input("How many people will be playing? [1 - 4]:"))
            if players == 1 or players == 2 or players == 3 or players == 4:
                break
            else:
                print("ERROR: PLEASE INPUT AN INTEGER BETWEEN 1 AND 4")
        except:
            print("ERROR: PLEASE INPUT AN INTEGER BETWEEN 1 AND 4")
    return players
 
#Gets the players name   
def playerName(playerNum):
    player = str(input("Please enter the name of player {}: " .format(playerNum)))
    return player

#Creating the board
def createBoard():
    """Length of 52"""
    print("-------------------------------------------")
    print("          Welcome to Candy Land!!!")
    color = (Back.BLUE, Back.RED, Back.YELLOW, Back.GREEN)
    board = []

    for i in range(1, 51):
        c = color[random.randint(0,3)]
        if c == Back.BLUE:
            x = 'B'
            board.append(x)

        elif c == Back.RED:
            x = 'R'
            board.append(x)

        elif c == Back.YELLOW:
            x = 'Y'
            board.append(x)

        elif c == Back.GREEN:
            x = 'G'
            board.append(x)

    board.insert(0, "START")
    board[-1] = "GUMDROP PALACE!"
    board.insert(25, "  ")
    
    return board

#This function sets the foreground color to black
def foreBlack():
    print(Fore.BLACK, end='')

#Player Style
def playerStyle():
    print(Style.BRIGHT, end="")
    print(Back.BLACK, end="")
    print(Fore.WHITE, end="")

#This function resets all color settings
def resetColors():
    print(Style.RESET_ALL, end='')

#Printing the board 
def printBoard(board):
    foreBlack()
    print(Back.WHITE)
    print()
    for i in board:
        if i == "B":
            print(Back.BLUE + "B", end='|')
        elif i == "R":
            print(Back.RED + "R", end='|')
        elif i == 'Y':
            print(Back.YELLOW + 'Y', end='|')
        elif i == 'G':
            print(Back.GREEN + 'G', end='|')
        elif i == "START":
            print(Style.BRIGHT, Back.WHITE, "START", end='|')
        elif i == "GUMDROP PALACE!":
            print(Style.BRIGHT, Back.WHITE, "GUMDROP PALACE!")
            print()
        elif i == "  ":
            print(Back.WHITE)
            print()
        else:
            playerStyle()
            print(i, end='  ')
            print(end='|')
    resetColors()

#Putting players into a dictionary
def playersDict(player, dict):
    dict[player] = 0
    return dict

#Updating the board with the players locations
def updateBoard(board, futureLocation, player):
    board[futureLocation] = player
    return board

#Putting players names in a list
def playersList(p, playersList):
    playersList.append(p)

    return playersList

#creating a deck of cards
def createDeck():
    """Length = 158"""
    deck = []
    for i in range (0, 150):
        num = random.randint(0, 3)
        if num == 0:
            x = "B"
            deck.append(x)
        elif num == 1:
            x = "R"
            deck.append(x)
        elif num == 2:
            x = "G"
            deck.append(x)
        elif num == 3:
            x = "Y"
            deck.append(x)
        stuck = 'Licorice'
        tele = 'Teleporting Position'
    for i in range(0,5):
        deck.append(stuck) 
    for i in range(0,3):
        deck.append(tele)
    
    return deck

#Each players turn
def drawingOptions(deck, player):

    while True:
        deck = shuffleDeck(deck)
        print()
        print('{} what would you like to do?' .format(player))
        choice = str(input("1) Draw Card\n2) Shuffle Deck\n"))
        if choice == '1':
            print('Drawing card...')
            card = drawCard(deck)
            break
        elif choice == '2':
            shuffleDeck(deck)
            print("The deck has been shuffled. Your card is... \n")
            card = drawCard(deck)
            break
        else:
            print("INVALID INPUT: PLEASE SELECT EITHER 1 OR 2")

    return card

#Shuffle deck
def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

#Drawing a card. The deck is always shuffled first
def drawCard(deck):
    shuffleDeck(deck)
    x = deck[0]
    print(x)

    return x

#Getting the current location
def currentLocation(board, p):
    i = board.index(p)
    return i

#Getting the future location
def futureLocation(board, card, cL):
    i = 0
    for item in board:
        if i > cL and item == card:
            fL = i
            break
        i = i + 1
    return fL


#Updating board with new player location and replacing old location
def ReplacePlayerBoard(board, cL, card):
    board[cL] = card
    return board

#Each players first turn
def firstTurn(player, deck, board):
    cL = 0
    card = drawingOptions(deck, player)
    #Get future location
    if card == 'Licorice':
        while True:
            print('Draw again. You cannot draw licorice on the first turn')
            card = drawingOptions(deck, player)
            if card != "Licorice":
                board = firstTurn(player, deck, board)
                break
    else:

        if card == 'Teleporting Position':
            fL = random.randint(0, 51)
            card = dict[player]
        else:
            fL = futureLocation(board, card, cL)
        #remove from old location
        board = ReplacePlayerBoard(board, cL, 'START')
        board = updateBoard(board, fL, player)
        printBoard(board)
        return board, card

#turn after the first turn
def turnMechanics(player, deck, board, dict):
    win = False
    #Getting old card
    oldcard = dict[player]
    #Get current location
    cL = currentLocation(board, player)
    #get card
    card = drawingOptions(deck, player)
    #get future location
    if card == 'Licorice':
        fL = cL
        board = ReplacePlayerBoard(board, cL, oldcard)
        board = updateBoard(board, fL, player)
        printBoard(board)
    elif card == 'Teleporting Position':
        fL = random.randint(0, 51)
        card = dict[player]
        board = ReplacePlayerBoard(board, cL, oldcard)
        board = updateBoard(board, fL, player)
        printBoard(board)
    else:
        try:
            fL = futureLocation(board, card, cL)
            board = ReplacePlayerBoard(board, cL, oldcard)
            board = updateBoard(board, fL, player)
            printBoard(board)
        except IndexError:
            win = winCondition(board, card, cL)
            if win == True:
                winner(player) 
        except UnboundLocalError:
            win = winCondition(board, card, cL)
            if win == True:
                winner(player)
    return win

#Check Win
def winCondition(board, card, cL):
    i = 0 
    win = True
    for item in board:
        if i > cL and item == card:
            win = False
            break
        i = i + 1
    return win

#If the player wins
def winner(player):
    print()
    print('{} is the winner!!!' .format(player))
    
#Loops until someone wins
def loop(list, deck, board, dict):
    i = 0
    while i < len(list):
        win = turnMechanics(list[i], deck, board, dict)
        i = i + 1
        if win:
            break
    return win

#Single player loop
def loopForOne(player, deck, board, dict):
 
    win = turnMechanics(player, deck, board, dict)
    
    return win

#Computer turn
def computermechanics(dict, deck, board):
    win = False
    player = 'Computer'
    #Getting old card
    oldcard = dict[player]
    #Get current location
    cL = currentLocation(board, player)
    #get card
    deck = shuffleDeck(deck)
    card = deck[0]

    #get future location
    if card == 'Licorice':
        fL = cL
        board = ReplacePlayerBoard(board, cL, oldcard)
        board = updateBoard(board, fL, player)
        printBoard(board)
    elif card == 'Teleporting Position':
        fL = random.randint(0, 51)
        card = dict[player]
        board = ReplacePlayerBoard(board, cL, oldcard)
        board = updateBoard(board, fL, player)
        printBoard(board)
    else:
        try:
            fL = futureLocation(board, card, cL)
            board = ReplacePlayerBoard(board, cL, oldcard)
            board = updateBoard(board, fL, player)
            printBoard(board)
        except IndexError:
            win = winCondition(board, card, cL)
            if win == True:
                winner(player) 
        except UnboundLocalError:
            win = winCondition(board, card, cL)
            if win == True:
                winner(player)
    return win

#Main GamePlay
def initiateGamePlay(board, list, dict, deck):
    printBoard(board)
    i = 0
    while i < len(list):
        board, card = firstTurn(list[i], deck, board)
        player = list[i]
        #Updating dictionary to store old card
        dict[player] = card
        i = i + 1
    x = True
    while x:
        win = loop(list, deck, board, dict)
        if win:
            x = False
            
#Computers decision for card draw
def computerCardDrawTurnOne(deck, board):
    cL = 0
    player = 'Computer'
    deck = shuffleDeck(deck)
    card = deck[0]
    #Get future location
    if card == 'Licorice':
        while True:
            print('Draw again. You cannot draw licorice on the first turn')
            deck = shuffleDeck(deck)
            card = deck[0]
            if card != "Licorice":
                board = computerCardDrawTurnOne(deck, board)
                break
    else:

        if card == 'Teleporting Position':
            fL = random.randint(0, 51)
            card = dict[player]
        else:
            fL = futureLocation(board, card, cL)
        #remove from old location
        board = ReplacePlayerBoard(board, cL, 'START')
        board = updateBoard(board, fL, player)
        printBoard(board)
        return board, card

#Single player mode
def singlePlayer(player, deck, board, list, dict):
    #single player first turn
    board, pCard = firstTurn(player, deck, board)
    #Updating dict
    dict[player] = pCard
    #Computer first turn
    print()
    print("Computer is drawing card...")
    board, cCard = computerCardDrawTurnOne(deck, board)
    #updating dict
    dict['Computer'] = cCard
    print()
    print('Computer drew {}' .format(cCard))

    x = True
    win = False
    while x:
        if win:
            break
        win = loopForOne(player, deck, board , dict)
        if win:
            break
        else:
            win = computermechanics(dict, deck, board)

#Main function

def main():
    #printing the Title
    printTitleMaterial()

    while True:
        while True:
            #Taking input and validating that input
            choice = printOptions()
            if choice == "p" or choice == "P" or choice == "i" or choice == "I" or choice == "q" or choice =="Q":
                print()
                break
            else:
                print("INVALID ENTRY")
                print("Please enter either p, i, or q")

        if choice == "p" or choice == "P":
            print()
            #Ask how many players
            amountOfPlayers = playerAmount()
            dict = {}
            list = []
            #Create Board
            board = createBoard()
            #Create deck
            deck = createDeck()

            #Creating base location
            futureLocation = 0

            #Players Names
            if amountOfPlayers == 1:
                p1 = playerName(1)
                dict = playersDict(p1, dict)
                list = playersList(p1, list)
                p2 = "Computer"
                dict = playersDict(p2, dict)
                list = playersList(p2, list)
                print("You will be playing against the Computer")

            elif amountOfPlayers == 2:
                p1 = playerName(1)
                dict = playersDict(p1, dict)
                list = playersList(p1, list)
                p2 = playerName(2)
                dict = playersDict(p2, dict)
                list = playersList(p2, list)

            elif amountOfPlayers ==3:
                p1 = playerName(1)
                dict = playersDict(p1, dict)
                list = playersList(p1, list)
                p2 = playerName(2)
                dict = playersDict(p2, dict)
                list = playersList(p2, list)
                p3 = playerName(3)
                dict = playersDict(p3, dict)
                list = playersList(p3, list)
            
            elif amountOfPlayers == 4:
                p1 = playerName(1)
                dict = playersDict(p1, dict)
                list = playersList(p1, list)
                p2 = playerName(2)
                dict = playersDict(p2, dict)
                list = playersList(p2, list)
                p3 = playerName(3)
                dict = playersDict(p3, dict)
                list = playersList(p3, list)
                p4 = playerName(4)
                dict = playersDict(p4, dict)
                list = playersList(p4, list)

            #Putting the players in starting position
            board = updateBoard(board, futureLocation, list)
            if amountOfPlayers == 1:
                singlePlayer(p1, deck, board, list, dict)
            else:
                initiateGamePlay(board, list, dict, deck)


        elif choice == 'i' or choice == 'I':
            printIntructions()

        elif choice == 'q' or choice == 'Q':
            print("THANKS FOR PLAYING!!!!")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()



