#Connect 4 Matrix logic

import numpy as np
import pygame
import sys
import math

BLUE = (0,0,155)
RED = (155,0,0)
BLACK = (0,0,0)
YELLOW = (250,250,10)

NUM_ROWS = 6
NUM_COLS = 7


def emptyBoard():
    board = np.zeros((NUM_ROWS,NUM_COLS))
    return board

def printBoard(board):
    print(np.flip(board, 0))

def dropPiece(board, row, move, token):
    board[row][move] = token

def checkLocation(board, move):
    return board[NUM_ROWS-1][move] == 0

def dropLocation(board, move):
    for rowCheck in range(NUM_ROWS):
        if board[rowCheck][move] == 0:
            return rowCheck


def checkWinner(board, token):
    #Horizontal check
    for c in range (NUM_COLS-3):
        for r in range(NUM_ROWS):
            if board[r][c] == token and board[r][c+1] == token and board[r][c+2] == token and board[r][c+3] == token:
                return True
    #check vertical
    for c in range (NUM_COLS):
        for r in range(NUM_ROWS-3):
            if board[r][c] == token and board[r+1][c] == token and board[r+2][c] == token and board[r+3][c] == token:
                return True    

    #check diagonal up
    for c in range (NUM_COLS-3):
        for r in range(NUM_ROWS-3):
            if board[r][c] == token and board[r+1][c+1] == token and board[r+2][c+2] == token and board[r+3][c+3] == token:
                return True

    #check diagonal down
    for c in range (NUM_COLS-3):
        for r in range(3, NUM_ROWS):
            if board[r][c] == token and board[r-1][c+1] == token and board[r-2][c+2] == token and board[r-3][c+3] == token:
                return True


def graphicBoard(board):
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS):
            pygame.draw.rect(screen, BLUE, (c*square, (r+1)*square, square, square))
            pygame.draw.circle(screen, BLACK, (int(c*square+square/2), int(r*square+square+square/2)), radius)
            
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*square+square/2), height-int(r*square+square/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*square+square/2), height-int(r*square+square/2)), radius)

    pygame.display.update()


board = emptyBoard()
printBoard(board)
endgame = False
turn = 0

pygame.init()

square = 100
radius = int(square/2.5)
width = NUM_COLS * square
height = (NUM_ROWS * square) + square
size = (width, height)

myfont = pygame.font.SysFont("monospace", 75)

screen = pygame.display.set_mode(size)
graphicBoard(board)
pygame.display.update()




while not endgame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, ((0,0, width, square)))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(square/2)), radius)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(square/2)), radius)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                
                posx = event.pos[0]
                move = int(math.floor(posx/square))
                if checkLocation(board, move):
                    row = dropLocation(board, move)
                    dropPiece(board, row, move, 1)
                    turn += 1
                    printBoard(board)
                    graphicBoard(board)

                    
                

                    if checkWinner(board, 1):
                        pygame.draw.rect(screen, BLACK, ((0,0, width, square)))
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        pygame.display.update()
                        print("player 1 wins")
                        endgame=True


            else:
                posx = event.pos[0]
                move = int(math.floor(posx/square))
                if checkLocation(board, move):
                    row = dropLocation(board, move)
                    dropPiece(board, row, move, 2)
                    turn -= 1
                    printBoard(board)
                    graphicBoard(board)
            
                    if checkWinner(board, 2):
                        pygame.draw.rect(screen, BLACK, ((0,0, width, square)))
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        pygame.display.update()
                        print("player 2 wins")
                        endgame=True


        if endgame:
            pygame.time.wait(3000)