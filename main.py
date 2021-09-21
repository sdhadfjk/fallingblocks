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

COLORS = [BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

# Other Variables for use in the program
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 1000
SPEED = 1000

# Create a black screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game")

# CONSTANTS
BLOCKSIZE = 40
BOARD_WIDTH = 10  # Starts at 0, 9 is recommended
BOARD_HEIGHT = 20  # Stars at 0, 19 is recommended

# pieces layout
I = [[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0], [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0]]
O = [[0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0]]
Z = [[0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0], [0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0]]
S = [[0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0], [0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0]]
L = [[0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0], [0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0], [0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0]]
J = [[0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0], [0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0], [0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0]]
T = [[0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0], [0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0], [0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0]]
types = [0,I, O, Z, S, L, J, T]
board = []


def generateBoard():
    for i in range(BOARD_HEIGHT):
        sublist = []
        for j in range(BOARD_WIDTH):
            sublist.append(0)
        if i==10:
            board.append([1,1,1,1,1,1,1,1,1,1])
        board.append(sublist)
    print(board)


class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.typenum = random.randint(1, 7)
        self.rotation = 0
        self.x = 3  # adapt for different sized boards
        self.y = 0
        self.addPosition()
        self.numrots = len(types[self.typenum])

    def move(self, dx, dy, rotate):
        if self.collision(self.x+dx, self.y+dy, (self.rotation+rotate)%self.numrots):
            self.deletePosition()
            self.x += dx
            self.y += dy
            self.rotation = (self.rotation + rotate) % self.numrots
            self.addPosition()
        # check for collision if bad don't move

    def deletePosition(self):
        """Deletes piece from board"""
        relX = 0
        relY = 0
        for i in types[self.typenum][self.rotation]:  # in type list
            if i != 0:
                board[self.y + relY][self.x + relX] = 0
            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break

    def addPosition(self):
        """adds piece to board"""
        relX = 0
        relY = 0
        print(self.typenum,self.rotation)
        for i in types[self.typenum][self.rotation]:  # in type string
            if i != 0:
                board[self.y + relY][self.x + relX] = self.typenum
            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break

    def collision(self,x,y,rotate):
        """Check for collisions"""
        relX = 0
        relY = 0
        for i in types[self.typenum][rotate]: # in type string
            if ((i != 0) and (board[y+relY][x+relX] != 0 and board[y+relY][x+relX] != self.typenum)) or ((i != 0 and i != self.typenum) and (x+relX<0 or x+relX>BOARD_WIDTH)):
                return False

            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break
        return True

generateBoard()
currentPiece = Piece()
down = USEREVENT + 1
pygame.time.set_timer(down, SPEED)
# Game Loop

while True:

    # Draw board
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            pygame.draw.rect(DISPLAYSURF, COLORS[board[i][j]], (j * BLOCKSIZE, i * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE))

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
            if event.key == ord('q'):
                pygame.quit()

    pygame.display.update()
    FramePerSec.tick(FPS)
    pygame.event.pump()
