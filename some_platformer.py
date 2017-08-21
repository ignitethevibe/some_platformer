import pygame
import sys
import constants
import levels
from player import Player
#from start_screen import StartScreen
from bperson import BirdPerson



lunar = pygame.image.load('lunar.png')

def main():
    global screen, font, clock
    # -- Main Program ----

    pygame.init()

    # Set the screen dimensions

    screen = pygame.display.set_mode(constants.size)

    pygame.display.set_caption("Arcade-Platformer")

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 25)



    #while True:
        #StartScreen()
    runGame()


    # -- Main Program Loop ---
def runGame():
    # create player




    # init Player
    player = Player()


    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))


    # set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level

    # Sprite Groups
    active_sprite_list = pygame.sprite.Group()


    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

     #-- Timer Display Setup
    frame_count = 0

    start_time = 45


    # loop until the user clicks the close button
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()





            # update the player
        active_sprite_list.update()

            #update items in the level
        current_level.update()
        #coin_list.update()



            # If the player gets near the right side, shift world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

            # if player gets near left side, shift world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

            # If player gets to end of level, go to next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # -- Win Screen once player reaches end
        #if current_level_no > len(level_list)-2:
            #done = True
            #winScreen()

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)



        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = frame_count // constants.frame_rate

        #Calculate for Going Down ---
        #total_seconds = start_time - (frame_count // constants.frame_rate)
        #if total_seconds < 0:
            #total_seconds = 0

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # use remainder to get seconds
        seconds = total_seconds % 60

        # Python string formatting to format into leading zeros
        output_string = "Time Wasted: {0:02}:{1:02}".format(minutes, seconds)

        #blit to screen
        text_time = font.render(output_string, True, constants.red)
        screen.blit(text_time, [15, 5])
        # -------------------Timer-----------
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
            # limit to 60 frames per second
        clock.tick(constants.frame_rate)

            # update screen
        pygame.display.flip()


        # Add GamesOver Screen
        #if total_seconds == 0:
            #done = True
            #gameOver()


    # to avoid exit errors
    pygame.quit()

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


        clock.tick(constants.frame_rate)

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



if __name__ == '__main__':
    main()
