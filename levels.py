import pygame

import constants
import platforms
from coin import Coin

class Level():
    # generic super class used to define level

    def __init__(self, player):
        # Constructor. Pass in a handle to player. needed for when collides

        # Lists of sprites used in all levels
        # Add or Remove Lists needed for game
        self.platform_list = None
        self.enemy_list = None
        self.coin_list = None

        # Background Image
        self.background = None

        # How far this world has been scrolled to left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.player = player


    # update everything on this level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.coin_list.update()

        coin_collect = pygame.sprite.spritecollide(self.player, self.coin_list, True)
        for coin in coin_collect:
            coin.kill()


    def draw(self, screen):
        # draw everything on this level
        # don't shift the background as much as the sprites are shifted
        # to give a feeling of depth
        screen.fill(constants.blue)
        screen.blit(self.background, (self.world_shift // 3,0))

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.coin_list.draw(screen)

    def shift_world(self, shift_x):
        # when the user moves left/right scroll everything

        # keep track of shift amount'
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for coin in self.coin_list:
            coin.rect.x += shift_x

# Create platforms for the Level
class Level_01(Level):
    # Definiton for Level 1

    def __init__(self, player):
        # create level 1

        # call the constructor
        Level.__init__(self, player)

        self.background = pygame.image.load('jetman.png').convert()
        self.background.set_colorkey(constants.white)
        self.level_limit = -5500

        # Array with type of platform, and x, y location of the platform
        level = [ [platforms.BLUE_PLATFORM_END, 535, 500],
                    [platforms.BLUE_PLATFORM_MIDDLE, 570, 500],
                    [platforms.BLUE_PLATFORM_END, 610, 500],
                    #
                    [platforms.BLUE_PLATFORM_END, 800, 400],
                    [platforms.BLUE_PLATFORM_END, 835, 400],
                    [platforms.BLUE_PLATFORM_MIDDLE, 870, 400],
                    [platforms.BLUE_PLATFORM_END, 910, 400],
                    [platforms.BLUE_PLATFORM_END, 945, 400],
                    #
                    [platforms.BLUE_PLATFORM_END, 1035, 500],
                    [platforms.BLUE_PLATFORM_MIDDLE, 1070, 500],
                    [platforms.BLUE_PLATFORM_END, 1105, 500],
                    #
                    [platforms.YELLOW_BRICK, 1120, 280],
                    [platforms.YELLOW_BRICK, 1152, 280],
                    [platforms.YELLOW_BRICK, 1184, 280],
                    #
                    [platforms.GRASS_LEFT, 1700, 240],
                    [platforms.GRASS_MIDDLE, 1730, 240],
                    [platforms.GRASS_MIDDLE, 1760, 240],
                    [platforms.GRASS_MIDDLE, 1790, 240],
                    [platforms.GRASS_RIGHT, 1820, 240],
                    #
                    [platforms.YELLOW_BRICK, 1718, 425],
                    [platforms.YELLOW_BRICK, 1750, 425],
                    [platforms.YELLOW_BRICK, 1782, 425],
                    #
                    [platforms.BLUE_PLATFORM_END, 1915, 185],
                    [platforms.BLUE_PLATFORM_END, 1950, 185],
                    [platforms.BLUE_PLATFORM_END, 1985, 185],
                    #
                    [platforms.STONE, 1891, 380],
                    [platforms.STONE, 1922, 380],
                    #
                    [platforms.BLUE_PLATFORM_END, 2100, 160],
                    [platforms.BLUE_PLATFORM_END, 2135, 160],
                    [platforms.BLUE_PLATFORM_END, 2170, 160],
                    #
                    [platforms.YELLOW_BRICK, 2150, 325],
                    [platforms.YELLOW_BRICK, 2182, 325],
                    [platforms.YELLOW_BRICK, 2214, 325],
                    #
                    [platforms.BLUE_PLATFORM_END, 2265, 245],
                    [platforms.BLUE_PLATFORM_END, 2300, 245],
                    [platforms.BLUE_PLATFORM_MIDDLE, 2335, 245],
                    [platforms.BLUE_PLATFORM_END, 2375, 245],
                    [platforms.BLUE_PLATFORM_END, 2410, 245],
                    #
                    [platforms.BLUE_PLATFORM_END, 2500, 190],
                    [platforms.BLUE_PLATFORM_END, 2535, 190],
                    [platforms.BLUE_PLATFORM_END, 2570, 190],
                    #
                    [platforms.BLUE_PLATFORM_END, 2725, 175],
                    [platforms.BLUE_PLATFORM_END, 2760, 175],
                    [platforms.BLUE_PLATFORM_END, 2795, 175],
                    #
                    [platforms.BLUE_PLATFORM_END, 2885, 165],
                    [platforms.BLUE_PLATFORM_MIDDLE, 2920, 165],
                    [platforms.BLUE_PLATFORM_END, 2960, 165],
                    # -- After Moving Platforms
                    [platforms.BLUE_PLATFORM_END, 3775, 160],
                    [platforms.BLUE_PLATFORM_MIDDLE, 3810, 160],
                    [platforms.BLUE_PLATFORM_END, 3850, 160],
                    ]

        # Go through array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # - Add second moving platform
        block = platforms.MovingPlatform(platforms.EXTEND_PLATFORM)
        block.rect.x = 3050
        block.rect.y = 215
        block.boundary_top = 215
        block.boundary_bottom = 425
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.EXTEND_PLATFORM)
        block.rect.x = 3325
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 415
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.EXTEND_PLATFORM)
        block.rect.x = 3570
        block.rect.y = 185
        block.boundary_top = 185
        block.boundary_bottom = 350
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        # ---

        # - Add Coin
        for coin in level:
            item = Coin(3810, 105)
            #item.rect.x = 3810
            #item.rect.y = 150
            item.player = self.player
            self.coin_list.add(item)


# add Level 2
class Level_02(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load('background_02.png').convert()
        self.background.set_colorkey(constants.white)
        self.level_limit = -1000

        level = [[platforms.BUBBLES, 500, 500],
                [platforms.BUBBLES, 570, 550],
                [platforms.BUBBLES, 640, 550],
                [platforms.BUBBLES, 800, 400],
                [platforms.BUBBLES, 870, 400],
                [platforms.BUBBLES, 940, 400],
                [platforms.BUBBLES, 1000, 500],
                [platforms.BUBBLES, 1070, 500],
                [platforms.BUBBLES, 1140, 500],
                [platforms.YELLOW_BRICK, 1120, 280],
                [platforms.YELLOW_BRICK, 1190, 280],
                [platforms.YELLOW_BRICK, 1260, 280],
                ]


        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # moving
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
