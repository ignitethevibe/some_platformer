# - module for managing platforms

import pygame
from spritesheet_functions import SpriteSheet

# These constants define our platform types:
# -- Name of file
# -- X Location of sprite
# -- Y location of sprite
# -- Width of sprite
# -- Height of Sprite

GRASS_LEFT              = (412,871,30,30)
GRASS_RIGHT             = (580,871,30,30)
GRASS_MIDDLE            = (479,871,30,30)
GRASS_PLAIN             = (433,871,30,30)
#STONE_PLATFORM_LEFT     = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE   = (648, 648, 70, 40)
#STONE_PLATFORM_RIGHT    = (792, 648, 70, 40)
STONE_BRICK             = (512,976,30,28)
STONE                   = (275,1007,31,32)

# -- Create more Level Objects
BLUE_PLATFORM_END       = (675, 228, 35, 38)
BLUE_PLATFORM_MIDDLE    = (709, 267, 40, 31)
YELLOW_BRICK            = (105, 574, 32, 31)
BUBBLES                 = (77, 725, 35, 39)
WHITE_BLOCK             = (975, 179, 40, 40)
EXTEND_PLATFORM         = (651, 572, 110, 35)





class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        super(Platform, self).__init__()

        sprite_sheet = SpriteSheet("tilesheet_comp.png")
        # grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    # fancy platform that can move
    def __init__(self, sprite_sheet_data):
        super(MovingPlatform, self).__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        # if player is in the way it will shove player out of the way

        # move left/right
        self.rect.x += self.change_x

        # See if hit player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        # move up/down
        self.rect.y += self.change_y

        # check for collision
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # check boundaries if need to reverse movement
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
