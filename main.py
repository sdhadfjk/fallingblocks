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
YELLOW = (255, 255, 0)
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
BOARD_WIDTH = 20  # Minimum 4, 10 is recommended
BOARD_HEIGHT = 20  # Stars at 0, 20 is recommended

# pieces layout
I = [[0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0], [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0]]
O = [[0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0]]
Z = [[0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0], [0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0]]
S = [[0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0], [0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0]]
L = [[0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0], [0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0], [0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0]]
J = [[0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0], [0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0], [0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0]]
T = [[0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0], [0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0], [0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0]]
types = [0,I, O, Z, S, L, J, T]
board = []


def generateBoard():
    for i in range(BOARD_HEIGHT):
        sublist = []
        for j in range(BOARD_WIDTH):
            sublist.append(0)
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
    def __del__(self):
        """delete piece"""
    def move(self, dx, dy, rotate):
        if not(self.collision(dx,dy,rotate)):
            self.deletePosition()
            self.x += dx
            self.y += dy
            self.rotation = (self.rotation + rotate) % self.numrots
            self.addPosition()
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
        for i in types[self.typenum][self.rotation]:  # in type string
            if i != 0:
                board[self.y + relY][self.x + relX] = self.typenum
            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break

    def collision(self,dx,dy,rot):
        x = self.x+dx
        y = self.y+dy
        rotate = (self.rotation + rot) % self.numrots
        """Check for no collisions"""
        relX = 0
        relY = 0
        for i in types[self.typenum][rotate]: # in type string
            # if hit a piece
            if i != 0 and board[y+relY][x+relX] != 0:
                try:
                    if types[self.typenum][rotate][(relY)*4+relX+dx] == 0:
                        return True
                    elif types[self.typenum][rotate][(relY+dy)*4 + relX] == 0:
                        generatePiece()
                        return True
                    print(types[self.typenum][rotate][(relY)*4+relX+dx])
                except IndexError:
                    if relY==3:
                        generatePiece()
                    return True


            # If sides
            elif i != 0 and (x+relX<0 or x+relX >= BOARD_WIDTH-1):
                print(y+relY, x+relX, self.typenum, "sides")
                return True
            # If hit bottom
            elif y+relY >= BOARD_HEIGHT-1:

                generatePiece()
                return True


            relX += 1
            if relX == 4:
                relY += 1
                relX = 0
            if relY == 4:
                break
        return False
def generatePiece():
    global currentPiece
    currentPiece = Piece()

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
            if event.key == pygame.K_DOWN:
                currentPiece.move(0,1,0)
            if event.key == ord('q'):
                pygame.quit()

    pygame.display.update()
    FramePerSec.tick(FPS)
    pygame.event.pump()
