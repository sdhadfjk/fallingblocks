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
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

# Create a black screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("Game")

# pieces layout
I = ["""
0010
0010
0010
0010
""", """
0000
1111
0000
0000
"""]
O = ["""
0000
0110
0110
0000
"""]
Z = ["""
0000
0011
0110
0000
""", """
0001
0011
0010
0000
"""]
S = ["""
0000
0110
0011
0000
""", """
0001 
0011
0010
"""]
L = ["""
0000
0111
0100
0000
""", """
0110
0010
0010
0000
""", """
0001
0111
0000
0000
""", """
0010
0010
0011
0000
"""]
J = ["""
0000
0111
0001
0000
""", """
0011
0010
0010
0000
""", """
0000
0111
0001
0000
""", """
0010
0010
0110
0000
"""]
T = ["""
0000
0111
0010
0000
""", """
0010
0111
0010
0000
""", """
0010
0111
0000
0000
""", """
0010
0011
0010
0000
"""]

class Piece(pygame.sprite.Sprite):
    def __init__(self, type, position):
        self.type = type
        self.rotation = 0
        self.position = (5,20) # adapt for different sized boards

    def rotate(self):
        rotation = (rotation+1) % len(type)


def generate():
    types = [I,O,Z,S,L,J,T]
    return new(Piece(random.choice(types)))


#Game Loop
while True:
    nextPiece = generate()

    pygame.display.update()
    FramePerSec.tick(FPS)