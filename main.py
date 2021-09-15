# Imports
import pygame
from pygame.locals import *
import random

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

COLORS = [BLACK,RED,YELLOW,GREEN,CYAN,BLUE,PURPLE,WHITE]

# Other Variables for use in the program
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 1000
SPEED = 5

# Create a black screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")

# CONSTANTS
BLOCKSIZE = 20
BOARD_WIDTH = 10 # Starts at 0, 9 is recommended
BOARD_HEIGHT = 20 # Stars at 0, 19 is recommended

# pieces layout
I = ["0010001000100010", "0000111100000000"]
O = ["0000011001100000"]
Z = ["0000001101100000", "0001001100100000"]
S = ["0000011000110000", "000100110010"]
L = ["0000011101000000", "0110001000100000", "0001011100000000", "0010001000110000"]
J = ["0000011100010000", "0011001000100000", "0000011100010000", "0010001001100000"]
T = ["0000011100100000", "0010011100100000", "0010011100000000", "0010001100100000"]
types = [0,I,O,Z,S,L,J,T]
board = []

def generateBoard():
    for i in range(0,BOARD_HEIGHT):
        sublist=[]
        for j in range(0,BOARD_WIDTH):
           sublist.append(0)
        board.append(sublist)

class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.typenum = random.randint(1,7)
        self.rotation = 0
        self.x = 3 # adapt for different sized boards
        self.y = 0
        self.addPosition()
    def move(self, dx, dy):
        self.deletePosition()
        self.x+=dx
        self.y+=dy
        self.addPosition()
    def deletePosition(self):
        relX = 0
        relY = 0
        for i in types[self.typenum][self.rotation]:  # in type string
            if i != 0:
                board[self.y + relY][self.x + relX] = 0
            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break

    def addPosition(self):
        relX = 0
        relY = 0
        for i in types[self.typenum][self.rotation]: # in type string
            if i !=0:
                board[self.y + relY][self.x + relX] = int(i)
            relX+=1
            if relX == 4:
                relY+=1
                relX=0
            if relY == 4:
                break


generateBoard()
currentPiece = Piece()

# Game Loop

while True:
    # Draw board
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            pygame.draw.rect(DISPLAYSURF, COLORS[board[i][j]], (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                currentPiece.move(-1, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                currentPiece.move(1, 0)

            if event.key == ord('q'):
                pygame.quit()

    pygame.display.update()
    FramePerSec.tick(FPS)
    pygame.event.pump()
