# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:40:12 2020

@author: danie
"""
#Input library

from IPython.display import clear_output
import random

#Draw the board
def disaply_board(board):
    print('\n')
    clear_output()
    print( board[7] + '|' + board[8] +'|' + board[9])
    print("______")
    print( board[4] + '|' + board[5] +'|' + board[6])
    print("_____")
    print( board[1] + '|' + board[2] +'|' + board[3])  
    
    
#To test if the board works   



def player_input():
    player1 = ' '
    
    #ask player one for there marker, if they do not 
    #chose X or O keep asking
   
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1 Chose X or O: ")
    
    #For player 2
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    #Return a tuple (that way we can do tuple unpacking)
        
    return(player1,player2)

#Check the player_input 
#Here we use tuple unpacking
    

#print(player_input())

#Write a function that takes in the board list object
#a marker ('x' or 'O') and a desiered position
def place_marker(board,marker,position):
    board[position] = marker
    disaply_board(board)
    
#To Test if the place_marker is working


#A function that takes in a board and a mark (X or ))
#Then checks to see if that marker has won
def win_check(board,marker):
   if(board[7] == marker and board[8] == marker and board[9] == marker):
       return True
   elif(board[4] == marker and board[5] == marker and board[6] == marker):
       return True
   elif(board[1] == marker and board[2] == marker and board[1] == marker):
       return True
   elif(board[7] == marker and board[4] == marker and board[1] == marker):
       return True
   elif(board[8] == marker and board[5] == marker and board[2] == marker):
       return True
   elif(board[9] == marker and board[6] == marker and board[3] == marker):
       return True
   elif(board[7] == marker and board[5] == marker and board[3] == marker):
       return True
   elif(board[9] == marker and board[5] == marker and board[1] == marker):
       return True
   else:
       return False



#Chose wich player goes first

def choose_first():
    first_move = random.randint(1,3)
    if(first_move == 1):
        print('Player 1 goes first')
        return player1_marker
        
    else:
        print('Player 2 Goes first')
        return player2_marker
#First player


#To check if a space on the board is free
#If free it returns true
def space_check(board, position):
    if(board[position] != ' '):
        return False
    else:
        return True

#Returns True if the board is full ,else returns False
def full_board_check(board):
    
    for x in board:
        if(x == ' '):
            return True
    else:
        return False
        print("The Board is Full")
  
#Ask the user what position they would like
#if it has already been entered it will re-ask the user 
def player_choice(board):
    pos = int(input("Next player Enter a position : "))
    while(space_check(test_board, pos) == False or pos not in [1,2,3,4,5,6,7,8,9]):
        pos = int(input("Next player Enter a position : "))   
    place_marker(test_board,move,pos)
    #test_board[pos] = move
    #disaply_board(test_board)
    


def replay():
    next_round = input("Enter Y to play again and N to exit: ")
    while(next_round != 'Y' and next_round != 'N'):
        next_round = input("Enter Y to play again and N to exit: ")
    if(next_round == 'Y'):
        return True
    else:
        return False
    


##The final function
print("Welcome to tick Tack toe")
x = True

while x:
    test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    disaply_board(test_board)
    player1_marker, player2_marker = player_input()
    
    move = choose_first()
    game_on = full_board_check(test_board)
    
    while game_on:
        player_choice(test_board)
        
        if(move == player1_marker):
            if(win_check(test_board,player1_marker)):
                print("Congrats player 1 you win")
                game_on = False
            else:
                game_on = full_board_check(test_board)
            move = player2_marker
            
        elif(move == player2_marker):
            if(win_check(test_board,player2_marker)):
                print("Congrats player2 you win ")
                game_on = False
            else:
                game_on = full_board_check(test_board)
            move = player1_marker
        else:
            game_on = full_board_check(test_board)
   
    if(replay()):
        x = True
    else:
        x = False
    
print("Thank you for playing")
    
    
    

    
    
        