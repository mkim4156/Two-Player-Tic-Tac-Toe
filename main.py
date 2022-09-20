import time

game_data = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]


def boardMaker():
    for i in range(len(game_data)):  # 0 < 9
        print(" | ", end="")
        print(game_data[i], end="")
        if i == 2:
            print(" |", end="")
            print()
        if i == 5:
            print(" |", end="")
            print()
        if i == 8:
            print(" |", end="")
            print()


def askingInput(symbol):
    choices = ["0" ,"1", "2"]
    user_input = input("For " + symbol + "'s Row [0-2]: ")
    while not user_input in choices:
        print("Please enter a number from 0 to 2! ")
        user_input = input("For " + symbol + "'s Row [0-2]: ")

    user_input2 = input("For " + symbol + "'s Column [0-2]: ")
    while user_input not in choices:
        print("Please enter a number from 0 to 2! ")
        user_input = input("For " + symbol + "'s Column [0-2]: ")

    user_input = int(user_input)
    user_input2 = int(user_input2)
    if user_input == 0 and user_input2 == 0:
        return 0
    elif user_input == 0 and user_input2 == 1:
        return 1
    elif user_input == 0 and user_input2 == 2:
        return 2
    elif user_input == 1 and user_input2 == 0:
        return 3
    elif user_input == 1 and user_input2 == 1:
        return 4
    elif user_input == 1 and user_input2 == 2:
        return 5
    elif user_input == 2 and user_input2 == 0:
        return 6
    elif user_input == 2 and user_input2 == 1:
        return 7
    elif user_input == 2 and user_input2 == 2:
        return 8

def inputingUserInput(symbol):
    index = askingInput(symbol)
    if game_data[index] == "X" or game_data[index] == "O":
        print("You cannot place it there! ")
        inputingUserInput(symbol)
    else:
        game_data[index] = symbol


def checkingWinCondition():
    symbol1 = "O"
    symbol2 = "X"
    if game_data[0] == symbol1 and game_data[1] == symbol1 and game_data[2] == symbol1:
        print(game_data[0] + " Won!")
        return True
    elif game_data[0] == symbol2 and game_data[1] == symbol2 and game_data[2] == symbol2:
        print(game_data[0] + " Won!")
        return True
    elif game_data[3] == symbol1 and game_data[4] == symbol1 and game_data[5] == symbol1:
        print(game_data[3] + " Won!")
        return True
    elif game_data[3] == symbol2 and game_data[4] == symbol2 and game_data[5] == symbol2:
        print(game_data[0] + " Won!")
        return True
    elif game_data[6] == symbol1 and game_data[7] == symbol1 and game_data[8] == symbol1:
        print(game_data[6] + " Won!")
        return True
    elif game_data[6] == symbol2 and game_data[7] == symbol2 and game_data[8] == symbol2:
        print(game_data[6] + " Won!")
        return True
    elif game_data[0] == symbol1 and game_data[3] == symbol1 and game_data[6] == symbol1:
        print(game_data[0] + " Won!")
        return True
    elif game_data[0] == symbol2 and game_data[3] == symbol2 and game_data[6] == symbol2:
        print(game_data[0] + " Won!")
        return True
    elif game_data[1] == symbol1 and game_data[4] == symbol1 and game_data[7] == symbol1:
        print(game_data[1] + " Won!")
        return True
    elif game_data[1] == symbol2 and game_data[4] == symbol2 and game_data[7] == symbol2:
        print(game_data[1] + " Won!")
        return True
    elif game_data[2] == symbol1 and game_data[5] == symbol1 and game_data[8] == symbol1:
        print(game_data[2] + " Won!")
        return True
    elif game_data[2] == symbol2 and game_data[5] == symbol2 and game_data[8] == symbol2:
        print(game_data[2] + " Won!")
        return True
    elif game_data[0] == symbol1 and game_data[4] == symbol1 and game_data[8] == symbol1:
        print(game_data[0] + " Won!")
        return True
    elif game_data[0] == symbol2 and game_data[4] == symbol2 and game_data[8] == symbol2:
        print(game_data[0] + " Won!")
        return True
    elif game_data[2] == symbol1 and game_data[4] == symbol1 and game_data[6] == symbol1:
        print(game_data[2] + " Won!")
        return True
    elif game_data[2] == symbol2 and game_data[4] == symbol2 and game_data[6] == symbol2:
        print(game_data[2] + " Won!")
        return True
    else:
        return False

def playGame():
    while user_input == "yes":
        inputingUserInput("X")
        boardMaker()
        if checkingWinCondition():
            break
        inputingUserInput("O")
        boardMaker()
        if checkingWinCondition():
            break


print("Welcome to the Game of TIC TAC TOE! ")
boardMaker()
time.sleep(0.3)
user_input = input("Would you like to play?: [Yes or No]: ").lower() or "s"

while user_input not in "no":
    if user_input == "yes":
        playGame()
        user_input = input("Would you like to play again?: [Yes or No]: ").lower()
    else:
        user_input = input("Please type either Yes or No: ") or "s"

print("Have a wonderful rest of your day! ")
