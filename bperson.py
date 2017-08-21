import pygame
import constants
import sys
from spritesheet_functions import SpriteSheet





class BirdPerson(pygame.sprite.Sprite):
    def __init__(self):
        #constructor function
        super(BirdPerson, self).__init__()

        # attributes
        # set vector speed
        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        # this holds all the animated images for walking left/right
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # list of sprites we can bump up against
        self.level = None
        self.player = None

        sprite_sheet = SpriteSheet('birdpersonFlip.png')
        # Load all the right facing images into a list

        image = sprite_sheet.get_image(10,926,110,138)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(142,928,110,134)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(268,926,112,136)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(400,926,104,136)
        self.walking_frames_r.append(image)


        # Load all the right facing images, then flip to face left


        image = sprite_sheet.get_image(10,926,110,138)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(142,928,110,134)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(268,926,112,136)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(400,926,104,136)
        image = pygame.transform.flip(image, True, False)


        # Set the image player starts with
        self.image = self.walking_frames_r[0]

        # set a reference to the image rect
        self.rect = self.image.get_rect()

    def update(self):


        # move left/right
        self.rect.x += self.change_x


        pos = self.rect.x #+ self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        if self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


        # move up/down
        self.rect.y += self.change_y


        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x #- self.level.world_shift
        #if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            #self.change_x *= -1
            #self.image = pygame.transform.flip(self.image, True, False)

        if cur_pos < self.boundary_left:
            self.change_x *= -1
            self.direction = "R"

        if cur_pos > self.boundary_right:
            self.change_x *= -1
            self.direction = "L"

    # Player Controlled Movement
    def go_left(self):
        # called when user hits the Left Arrow
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        self.change_x =6
        self.direction = "R"
