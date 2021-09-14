# Imports
import pygame
from pygame.locals import *
import random
import time

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 1000
SPEED = 5

# Create a black screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")

# CONSTANTS
BLOCKSIZE = 20

# pieces layout
I = ["0010001000100010", "0000111100000000"]
O = ["0000011001100000"]
Z = ["0000001101100000", "0001001100100000"]
S = ["0000011000110000", "000100110010"]
L = ["0000011101000000", "0110001000100000", "0001011100000000", "0010001000110000"]
J = ["0000011100010000", "0011001000100000", "0000011100010000", "0010001001100000"]
T = ["0000011100100000", "0010011100100000", "0010011100000000", "0010001100100000"]
types = [I,O,Z,S,L,J,T]

class Piece(pygame.sprite.Sprite):
    def __init__(self):
        self.type = random.choice(types)
        self.rotation = 0
        self.x = 10
        self.y = 10 # adapt for different sized boards

    def rotate(self):
        self.rotation = (self.rotation+1) % len(self.type)

# Draw piece
def draw(piece, x, y, rotation):
    relX = 0
    relY = 0
    for i in piece.type[piece.rotation]:

        if i == "1":
            pygame.draw.rect(DISPLAYSURF, RED, ((piece.x+relX)*BLOCKSIZE,(piece.y+relY)*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE))
        relX+=1
        if relX == 4:
            relX = 0
            relY+=1
        if relY == 4:
            break

nextPiece = Piece()
# Game Loop

while True:


    # Keypressing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_RIGHT:
                draw(nextPiece, 1, 0, 0)
            elif event.key == pygame.K_LEFT:

            elif event.key == pygame.K_UP:






    pygame.display.update()
    FramePerSec.tick(FPS)
