import pygame
import sys
import constants
from spritesheet_functions import SpriteSheet
from bperson import BirdPerson

pygame.init()
clock = pygame.time.Clock()
lunar = pygame.image.load('lunar.png')

def StartScreen():

    titleFont = pygame.font.Font('freesansbold.ttf', 85)
    titleSurf1 = titleFont.render('Scroll With', True, constants.blue)
    titleSurf2 = titleFont.render('Sprites', True, constants.blue)
    screen = pygame.display.set_mode(constants.size)
    # -- Set Start and Change

    bperson = BirdPerson()
    start_sprites = pygame.sprite.Group()
    start_sprites.add(bperson)

    bperson.rect.x = 50
    bperson.rect.y = 450


    bperson.change_x = 5

    # -- Text
    titleRect1x = 300
    titleRect1y = 50

    titleRect2x = 335
    titleRect2y = 115


    while True:

        #bperson.rect.x += bperson_change_x
        bperson.boundary_right = 450
        bperson.boundary_left = 50

        #if bperson.rect.x > 500 or bperson.rect.x < 50:
            #bperson_change_x = bperson_change_x * -1


        screen.blit(pygame.transform.scale(lunar,(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)), (0,0))

        titleRect1 = titleSurf1.get_rect()
        titleRect1.topleft = (titleRect1x, titleRect1y)

        titleRect2 = titleSurf2.get_rect()
        titleRect2.topleft = (titleRect2x, titleRect2y)

        screen.blit(titleSurf1, titleRect1)
        screen.blit(titleSurf2, titleRect2)

        start_sprites.update()
        start_sprites.draw(screen)
        #screen.blit(start_sprites, [bperson.rect.x, bperson.rect.y])

        clock.tick(60)

        pygame.display.flip()




        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        clock.tick(constants.frame_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def checkForKeyPress():
    if len(pygame.event.get(pygame.QUIT)) > 0:
        pygame.quit()
    keyUpEvents = pygame.event.get(pygame.KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
        pygame.quit()
    return keyUpEvents[0].key
