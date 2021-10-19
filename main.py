# Imports
import copy

import pygame
from pygame.locals import *
import random
import math

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

COLORS = [BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

# Other Variables for use in the program
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
SPEED = 200

# Create a black screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")

# CONSTANTS
BLOCKSIZE = 40
BOARD_WIDTH = 10  # Minimum 4, 10 is recommended
BOARD_HEIGHT = 20  # Stars at 0, 20 is recommended

# pieces layout
I = [[0,0,1,0,
      0,0,1,0,
      0,0,1,0,
      0,0,1,0],
     [0,0,0,0,
      1,1,1,1,
      0,0,0,0,
      0,0,0,0]]
O = [[0,0,0,0,
      0,1,1,0,
      0,1,1,0,
      0,0,0,0]]
Z = [[0,0,0,0,
      0,0,1,1,
      0,1,1,0,
      0,0,0,0],
     [0,0,1,0,
      0,0,1,1,
      0,0,0,1,
      0,0,0,0]]
S = [[0,0,0,0,
      0,1,1,0,
      0,0,1,1,
      0,0,0,0],
     [0,0,0,1,
      0,0,1,1,
      0,0,1,0,
      0,0,0,0]]
L = [[0,0,0,0,
      0,1,1,1,
      0,1,0,0,
      0,0,0,0],
     [0,1,1,0,
      0,0,1,0,
      0,0,1,0,
      0,0,0,0],
     [0,0,0,1,
      0,1,1,1,
      0,0,0,0,
      0,0,0,0],
     [0,0,1,0,
      0,0,1,0,
      0,0,1,1,
      0,0,0,0]]
J = [[0,0,0,0,
      0,1,1,1,
      0,0,0,1,
      0,0,0,0],
     [0,0,1,1,
      0,0,1,0,
      0,0,1,0,
      0,0,0,0],
     [0,0,0,0,
      0,1,0,0,
      0,1,1,1,
      0,0,0,0],
     [0,0,1,0,
      0,0,1,0,
      0,1,1,0,
      0,0,0,0]]
T = [[0,0,0,0,
      0,1,1,1,
      0,0,1,0,
      0,0,0,0],
     [0,0,1,0,
      0,0,1,1,
      0,0,1,0,
      0,0,0,0],
     [0,0,1,0,
      0,1,1,1,
      0,0,0,0,
      0,0,0,0],
     [0,0,1,0,
      0,1,1,0,
      0,0,1,0,
      0,0,0,0]]

#types = [0,I, O,J,L,Z,S,T]
types = [0,I,I,I,I,I,I,I]
board = []


def generate_board():
    for i in range(BOARD_HEIGHT):
        sublist = []
        for j in range(BOARD_WIDTH):
            sublist.append(0)
        board.append(sublist)


def delete_line(line):
    del board[line]
    sublist = []
    for j in range(BOARD_WIDTH):
        sublist.append(0)
    board.insert(0,sublist)


class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.typenum = random.randint(1, 7)
        self.rotation = 0
        self.x = math.floor(BOARD_WIDTH/2)-2  # adapt for different sized boards
        self.y = 0
        self.numrots = len(types[self.typenum])

    def move(self, dx, dy, rotate):
        if not(self.collision(dx,dy,rotate)):
            self.x += dx
            self.y += dy
            self.rotation = (self.rotation + rotate) % self.numrots
            self.draw()

    def add_position(self):
        relX = 0
        relY = 0
        for i in types[self.typenum][self.rotation]:  # in type list
            if i != 0:
                board[self.y + relY][self.x + relX] = self.typenum
            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break
        # delete line
        for i in range(BOARD_HEIGHT):
            full = True
            for j in range(BOARD_WIDTH):
                if board[i][j] == 0:
                    full = False
                    break
            if full:
                delete_line(i)

    def collision(self, dx, dy, drot):
        """Return True if collision
        Return false if no collision"""
        x = self.x+dx
        y = self.y+dy
        rotate = (self.rotation + drot) % self.numrots

        relX = 0
        relY = 0
        for i in types[self.typenum][rotate]:  # in type list
            try:
                if i != 0 and board[y+relY][x+relX] != 0:  # if current square on board
                    if dy != 0:  # if move down, new piece
                        self.add_position()
                        generate_piece()
                    return True
            except IndexError:
                if relY == 3:
                    self.add_position()
                    generate_piece()
                return True

            # If sides
            if i != 0 and (x+relX < 0 or x+relX >= BOARD_WIDTH):
                return True
            # If hit bottom
            if i != 0 and y+relY >= BOARD_HEIGHT-1:
                self.add_position()
                generate_piece()
                return True

            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break
        return False

    def draw(self):
        tempboard = copy.deepcopy(board)

        relX = 0
        relY = 0
        for i in types[self.typenum][self.rotation]:  # in type list
            if i != 0:
                tempboard[self.y + relY][self.x + relX] = self.typenum
            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                pygame.draw.rect(DISPLAYSURF, COLORS[tempboard[i][j]], (j*BLOCKSIZE, i*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))


def generate_piece():
    pygame.time.wait(50)
    global currentPiece
    currentPiece = Piece()


generate_board()
currentPiece = Piece()
down = USEREVENT + 1
pygame.time.set_timer(down, SPEED)

# Game Loop
while True:
    # Draw board
    for event in pygame.event.get():
        if event.type == down:
            currentPiece.move(0, 1, 0)
        # keyboard
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                currentPiece.move(-1, 0, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                currentPiece.move(1, 0, 0)
            if event.key == pygame.K_UP:
                currentPiece.move(0, 0, 1)
            if event.key == pygame.K_DOWN:
                currentPiece.move(0, 1, 0)
            if event.key == ord('q'):
                pygame.quit()

    pygame.display.update()
    FramePerSec.tick(FPS)
    pygame.event.pump()
