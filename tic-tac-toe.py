#!/usr/bin/python3

def p1_choice():

    choice = ''
    choice2 = ''

    while choice not in ['X','O']:
        choice = input("Player 1, please select X or O: ")

        if choice not in ['X','O']:
            print("Please choose either X or O!")

    if choice == 'X':
        choice2 = 'O'
    else:
        choice2 = 'X'
    print(f"\nPlayer 1 is {choice}, Player 2 is {choice2}")
    return choice


def p1_position(currentList):

    choice = 10

    while choice not in range(1,10):
        choice = int(input(f"\nPlayer 1, select a corresponding position on the number keypad (1-9):\n\n {currentList[6]}|{currentList[7]}|{currentList[8]} \n-------\n {currentList[3]}|{currentList[4]}|{currentList[5]} \n-------\n {currentList[0]}|{currentList[1]}|{currentList[2]}\n\n> "))

        if choice not in range(1,10):
            print("Please select numbers 1-9 only!")

    return choice


def p2_position(currentList):

    choice = 10

    while choice not in range(1,10):
        choice = int(input(f"\nPlayer 2, select a corresponding position on the number keypad (1-9):\n\n {currentList[6]}|{currentList[7]}|{currentList[8]} \n-------\n {currentList[3]}|{currentList[4]}|{currentList[5]} \n-------\n {currentList[0]}|{currentList[1]}|{currentList[2]}\n\n> "))

        if choice not in range(1,10):
            print("Please select numbers 1-9 only!")

    return choice


def display_board(boardList):

    #from IPython.display import clear_output
    #clear_output()

    import os
    os.system('clear')

    print("   |   |   ")
    print(f" {boardList[7]} | {boardList[8]} | {boardList[9]} ")
    print(f"___|___|___")
    print("   |   |   ")
    print(f" {boardList[4]} | {boardList[5]} | {boardList[6]} ")
    print(f"___|___|___")
    print("   |   |   ")
    print(f" {boardList[1]} | {boardList[2]} | {boardList[3]} ")
    print("   |   |   ")


def update_board(boardList,position,choice):

    boardList[position]=choice

    return boardList


def check_win(board,player):

    from collections import Counter

    #board = ['#', 'O', 'O', 'O', 'O', 'X', 'Y', 'X', 'X', 'O']

    win1 = (board[7],board[8],board[9])
    win2 = (board[4],board[5],board[6])
    win3 = (board[1],board[2],board[3])
    win4 = (board[7],board[4],board[1])
    win5 = (board[8],board[5],board[2])
    win6 = (board[9],board[6],board[3])
    win7 = (board[7],board[5],board[3])
    win8 = (board[1],board[5],board[9])

    #createListTuple = [eval('win'+str(i)) for i in range(1,9)]
    createListTuple = [win1,win2,win3,win4,win5,win6,win7,win8]

    for a,b,c in createListTuple:
        #print(a,b,c)
        if a == b == c == 'X' or a == b == c == 'O':
            print(f'Player {player} [{a}], wins!')
            #print('False')
            return False

    if Counter(board)['O'] + Counter(board)['X'] == 9:
        print("It's a tie!")
        return False

    return True


def used_position_check(currentList,position):

    import os

    if position in currentList:
        #currentList.remove(position)
        currentList[position-1] = '-'
        return False
    else:
        os.system('clear')
        print("Please select an unsed position!")
        return True


def play_again():

    choice = ''

    while choice not in ['Y','N']:
        choice = input('Play again? (Y,N): ')

        if choice not in ['Y','N']:
            print("Please select [Y]es or [N]o only!")

    if choice == 'Y':
        return True
    else:
        return False


currentBoardList = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
available_items = [1,2,3,4,5,6,7,8,9]
game_on = True
playagain = True
p1choice = p1_choice()

if p1choice == 'X':
    p2choice = 'O'
else:
    p2choice = 'X'

while game_on or playagain:
    listChecker = True
    while listChecker:
        p1position = p1_position(available_items)
        listChecker = used_position_check(available_items,p1position)
        if listChecker == False:
            break
    currentBoardList = update_board(currentBoardList,p1position,p1choice)
    display_board(currentBoardList)
    game_on = check_win(currentBoardList,'1')

    if not game_on:
        playagain = play_again()
        if not playagain:
            break
        else:
            currentBoardList = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            available_items = [1,2,3,4,5,6,7,8,9]
            p1choice = p1_choice()
            if p1choice == 'X':
                p2choice = 'O'
            else:
                p2choice = 'X'
            continue

    listChecker = True
    while listChecker:
        p2position = p2_position(available_items)
        listChecker = used_position_check(available_items,p2position)
        if listChecker == False:
            break
    currentBoardList = update_board(currentBoardList,p2position,p2choice)
    display_board(currentBoardList)
    game_on = check_win(currentBoardList,'2')

    if not game_on:
        playagain = play_again()
        if not playagain:
            break
        else:
            currentBoardList = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            available_items = [1,2,3,4,5,6,7,8,9]
            p1choice = p1_choice()
            if p1choice == 'X':
                p2choice = 'O'
            else:
                p2choice = 'X'
            continue
