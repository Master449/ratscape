import pygame
import random

pygame.init()

# - - - - - Variables - - - - -

# Screen
global TextLine1
global TextLine2
global TextLine3

TextLine1 = " "
TextLine2 = " "
TextLine3 = " "

WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
HOVER_GRAY = (175, 175, 175)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

pygame.display.set_caption('Ratscape')
CLOCK = pygame.time.Clock()

global FONT

FONT = pygame.font.SysFont("Arial", 26)
ButtonFont = pygame.font.SysFont("Arial", 12)



def DrawHUD():
    SCREEN.fill(WHITE)
    global TextLine1
    global TextLine2
    global TextLine3

    pygame.draw.rect(SCREEN, BLACK, (40, 570, 1200, 120))

    HealthBar = FONT.render("HP: ", 16, BLACK)
    MPBar = FONT.render("MP: ", 16, BLACK)
    GoldLabel = FONT.render("Gold: ", 16, BLACK)
    GoldAmount = FONT.render(str(gold), 1024, BLACK)

    Label = FONT.render(TextLine1, 1, WHITE)
    Label2 = FONT.render(TextLine2, 1, WHITE)
    Label3 = FONT.render(TextLine3, 1, WHITE)

    SCREEN.blit(GoldLabel, (800, 540))
    SCREEN.blit(GoldAmount, (866, 540))
    SCREEN.blit(MPBar, (400, 540))
    SCREEN.blit(HealthBar, (40, 540))

    SCREEN.blit(Label, (45, 575))
    SCREEN.blit(Label2, (45, 605))
    SCREEN.blit(Label3, (45, 635))

    ScreenCords = FONT.render(("( " + str(CordX) + "," + str(CordY) + " )"), 1, (0, 0, 0))
    SCREEN.blit(ScreenCords, (1000, 540))

    #Drawing the HP Bar
    pygame.draw.rect(SCREEN, GRAY, (84, 543, 200, 24))
    pygame.draw.rect(SCREEN, RED, (84, 543, Health, 24))

    #Drawing the MP Bar
    pygame.draw.rect(SCREEN, GRAY, (448, 543, 200, 24))
    pygame.draw.rect(SCREEN, BLUE, (448, 543, Magic, 24))

    pygame.draw.rect(SCREEN, GREEN, (590, 310, 50, 50))

    pygame.display.update()

# - - - - - - Classes - - - - - - - 
class Room:
    def __init__(x, y, enemy, moneyLoot, enemyLoot, blockFront, blockBack, blockRight, blockLeft, visited):
        self.x = x
        self.y = y
        self.enemy = enemy
        self.moneyLoot = moneyLoot
        self.enemyLoot = enemyLoot

        self.blockFront = blockFront
        self.blockBack = blockBack
        self.blockRight = blockRight
        self.blockLeft = blockLeft

        self.visited = visted

        
# - - - - - - Definitions - - - - - -
def genBool(b):
    b = random.choice([true, false])
    return b

def roomVisited(x, y):
    roomName = str(x) + "-" + str(y)
    exists = hasattr(roomName, 'visited')
    if (exists == False):
        print("generate room")
    else:
        print('fuck')
        
# Game
global CordX
global CordY
CordX = 0
CordY = 0

global Health
Health = 200

global Magic
Magic = 200

global gold
gold = 0

#  - - - - - - GAME LOOP - - - - -
is_running = True
while is_running:

    MOUSE = pygame.mouse.get_pos()
    CLICK = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                CordY += 1
                roomVisited(CordX, CordY)
            if event.key == pygame.K_s:
                CordY -= 1
                roomVisited(CordX, CordY)
            if event.key == pygame.K_a:
                CordX -= 1
                roomVisited(CordX, CordY)
            if event.key == pygame.K_d:
                CordX += 1
                roomVisited(CordX, CordY)
                
    DrawHUD()

    CLOCK.tick(20)
