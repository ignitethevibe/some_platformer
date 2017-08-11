import pygame
import constants

from spritesheet_functions import SpriteSheet
from char_sprites import CharSprites

# -- Class to add images to levels and option to animate

class Extras(pygame.sprite.Sprite):
    def __init__(self, char_sprite):
        super(Extras, self).__init__()

        # Vector Speed
        self.change_x = 0
        self.change_y = 0

        # Animation holder
        self.walking_frames_l = []
        self.walking_frames_r = []

        # Start Direction
        self.direction = "R"



        self.boundary_top= 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.player = None

        self.level = None

    def update(self):

            # -- Move Left/Right
        self.rect.x += self.change_x

        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

            # -- Move Up/Down
        self.rect.y += self.change_y


            # Check the boundaries and see if we need to reverse
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1



        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
            self.image = pygame.transform.flip(self.image, True, False)
