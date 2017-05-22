import pygame

pygame.init()

# - - - - - Variables - - - - -

global CordX
global CordY

CordX = 0
CordY = 0

MainText = "This is a variable"

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

CLOCK = pygame.time.Clock()


# - - - - - - Screen - - - - - - -
pygame.display.set_caption('Ratscape')

FONT = pygame.font.SysFont("Arial", 26)
ButtonFont = pygame.font.SysFont("Arial", 12)

pygame.draw.rect(SCREEN, BLACK, (40, 570, 1200, 120))
pygame.draw.rect(SCREEN, GREEN, (590, 310, 50, 50))

pygame.display.flip()

is_running = True

# - - - - - - Definitions - - - - -

#  - - - - GAME LOOP - - - -

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            print(event)

    MOUSE = pygame.mouse.get_pos()
    CLICK = pygame.mouse.get_pressed()


    #Top Button

    if 1150+50 > MOUSE[0] > 1150 and 400+50 > MOUSE[1] > 400 and CLICK[0] == 1:
        pygame.draw.rect(SCREEN, HOVER_GRAY, (1150, 400, 50, 50))
        CordY + 1
    elif 1150+50 > MOUSE[0] > 1150 and 400+50 > MOUSE[1] > 400:
        pygame.draw.rect(SCREEN, HOVER_GRAY, (1150, 400, 50, 50))
    else:
        pygame.draw.rect(SCREEN, GRAY, (1150, 400, 50, 50))

    #Bottom Button
    #button(1150, 500, 50, 50, HOVER_GRAY, GRAY)

    #Left Button
    #button(1100, 450, 50, 50, HOVER_GRAY, GRAY)

    # Right Button
    #button(1200, 450, 50, 50, HOVER_GRAY, GRAY)

    UpButtonText = ButtonFont.render("UP", 1, (0, 0, 0))
    DownButtonText= ButtonFont.render("DOWN", 1, (0, 0, 0))
    RightButtonText = ButtonFont.render("RIGHT", 1, (0, 0, 0))
    LeftButtonText = ButtonFont.render("LEFT", 1, (0, 0, 0))
    Label = FONT.render(MainText, 1, (255, 255, 255))

    SCREEN.blit(UpButtonText, (1167, 420))
    SCREEN.blit(DownButtonText, (1155, 520))
    SCREEN.blit(LeftButtonText, (1110, 470))
    SCREEN.blit(RightButtonText, (1205, 470))

    SCREEN.blit(Label, (45, 575))

    print(CLICK)

    pygame.display.update()
    CLOCK.tick(60)
