import pygame

pygame.init()

# - - - - - Variables - - - - -

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

FONT = pygame.font.SysFont("Arial", 26)
ButtonFont = pygame.font.SysFont("Arial", 12)

is_running = True

CLOCK = pygame.time.Clock()

# - - - - - - Definitions - - - - -

def DrawHUD():
    pygame.display.set_caption('Ratscape')

    SCREEN.fill(WHITE)

    #Hover effect on the positional keys

    if 1150 + 50 > MOUSE[0] > 1150 and 400 + 50 > MOUSE[1] > 400:
        pygame.draw.rect(SCREEN, HOVER_GRAY, (1150, 400, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1150, 500, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1100, 450, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1200, 450, 50, 50))
    elif 1150 + 50 > MOUSE[0] > 1150 and 500 + 50 > MOUSE[1] > 500:
        pygame.draw.rect(SCREEN, GRAY, (1150, 400, 50, 50))
        pygame.draw.rect(SCREEN, HOVER_GRAY, (1150, 500, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1100, 450, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1200, 450, 50, 50))
    elif 1100 + 50 > MOUSE[0] > 1100 and 450 + 50 > MOUSE[1] > 450:
        pygame.draw.rect(SCREEN, GRAY, (1150, 400, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1150, 500, 50, 50))
        pygame.draw.rect(SCREEN, HOVER_GRAY, (1100, 450, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1200, 450, 50, 50))
    elif 1200 + 50 > MOUSE[0] > 1200 and 450 + 50 > MOUSE[1] > 450:
        pygame.draw.rect(SCREEN, GRAY, (1150, 400, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1150, 500, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1100, 450, 50, 50))
        pygame.draw.rect(SCREEN, HOVER_GRAY, (1200, 450, 50, 50))
    else:
        pygame.draw.rect(SCREEN, GRAY, (1150, 400, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1150, 500, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1100, 450, 50, 50))
        pygame.draw.rect(SCREEN, GRAY, (1200, 450, 50, 50))


    #Drawing the Labels
    UpButtonText = ButtonFont.render("UP", 1, (0, 0, 0))
    DownButtonText = ButtonFont.render("DOWN", 1, (0, 0, 0))
    RightButtonText = ButtonFont.render("RIGHT", 1, (0, 0, 0))
    LeftButtonText = ButtonFont.render("LEFT", 1, (0, 0, 0))

    HealthBar = FONT.render("HP: ", 16, BLACK)
    MPBar = FONT.render("MP: ", 16, BLACK)
    GoldLabel = FONT.render("Gold: ", 16, BLACK)
    GoldAmount = FONT.render(str(gold), 1024, BLACK)

    SCREEN.blit(UpButtonText, (1167, 420))
    SCREEN.blit(DownButtonText, (1155, 520))
    SCREEN.blit(LeftButtonText, (1110, 470))
    SCREEN.blit(RightButtonText, (1205, 470))

    SCREEN.blit(GoldLabel, (800, 540))
    SCREEN.blit(GoldAmount, (866, 540))
    SCREEN.blit(MPBar, (400, 540))
    SCREEN.blit(HealthBar, (40, 540))

    #Drawing the main text box
    pygame.draw.rect(SCREEN, BLACK, (40, 570, 1200, 120))

    Label = FONT.render(TextLine1, 1, (255, 255, 255))
    SCREEN.blit(Label, (45, 575))
    Label2 = FONT.render(TextLine2, 1, (255, 255, 255))
    SCREEN.blit(Label2, (45, 605))
    Label3 = FONT.render(TextLine3, 1, (255, 255, 255))
    SCREEN.blit(Label3, (45, 635))

    ScreenCords = FONT.render(("( " + str(CordX) + " , " + str(CordY) + " ) "), 1, (0, 0, 0))
    SCREEN.blit(ScreenCords, (1000, 540))

    #Drawing the HP Bar
    pygame.draw.rect(SCREEN, GRAY, (84, 543, 200, 24))
    pygame.draw.rect(SCREEN, RED, (84, 543, Health, 24))

    #Drawing the MP Bar
    pygame.draw.rect(SCREEN, GRAY, (448, 543, 200, 24))
    pygame.draw.rect(SCREEN, BLUE, (448, 543, Magic, 24))

    pygame.draw.rect(SCREEN, GREEN, (590, 310, 50, 50))

    pygame.display.update()

# Thanks Anthony for fixing the text bugs!

def HealthCheck():
    if Health <= 0:
        TextLine1 = "Game Over"
        Label = FONT.render(TextLine1, 1, (255, 255, 255))
        SCREEN.blit(Label, (45, 575))


def RoomCheck():
    if CordY == 1 and CordX == 1:
        TextLine1 = "Give Succ"
        TextLine2 = " "
        TextLine3 = " "

    if CordY != 1 or CordX != 1:
        TextLine1 = "Welcome to Ratscape, You are currently in the starting room."
        TextLine2 = "Use the controls off to the right hand side to move to different rooms."
        TextLine3 = "As you progress you will aquire treasure and fight monsters"

def RedrawScreen():
    SCREEN.fill(WHITE)
    DrawHUD()

#  - - - - - - GAME LOOP - - - - -

while is_running:

    MOUSE = pygame.mouse.get_pos()
    CLICK = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif 1150 + 50 > MOUSE[0] > 1150 and 400 + 50 > MOUSE[1] > 400 and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(SCREEN, HOVER_GRAY, (1150, 400, 50, 50))
                CordY = CordY + 1
        elif 1150+50 > MOUSE[0] > 1150 and 500+50 > MOUSE[1] > 500 and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(SCREEN, HOVER_GRAY, (1150, 500, 50, 50))
            CordY = CordY - 1
        elif 1100+50 > MOUSE[0] > 1100 and 450+50 > MOUSE[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(SCREEN, HOVER_GRAY, (1100, 450, 50, 50))
            CordX = CordX - 1
        elif 1200+50 > MOUSE[0] > 1200 and 450+50 > MOUSE[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(SCREEN, HOVER_GRAY, (1200, 450, 50, 50))
            CordX = CordX + 1

    RedrawScreen()
    RoomCheck()
    HealthCheck()

    CLOCK.tick(60)