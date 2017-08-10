import pygame
import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

    # --- BirdPerson Player Sprite
class Player(pygame.sprite.Sprite):
    # this class represents the bar at the bottom that the player controls

    # -- methods
    def __init__(self):
        #constructor function
        super(Player, self).__init__()

        # attributes
        # set vector speed
        self.change_x = 0
        self.change_y = 0

        # this holds all the animated images for walking left/right
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # list of sprites we can bump up against
        self.level = None

        sprite_sheet = SpriteSheet('birdpersonFlip.png')
        # Load all the right facing images into a list
        #image = sprite_sheet.get_image(18,750,104,148)
        #self.walking_frames_r.append(image)
        #image = sprite_sheet.get_image(276,750,102,148)
        #self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(10,926,110,138)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(142,928,110,134)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(268,926,112,136)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(400,926,104,136)
        self.walking_frames_r.append(image)


        # Load all the right facing images, then flip to face left

        #image = sprite_sheet.get_image(18,750,104,148)
        #image = pygame.transform.flip(image, True, False)
        #self.walking_frames_l.append(image)
        #image = sprite_sheet.get_image(276,750,102,148)
        #image = pygame.transform.flip(image, True, False)
        #self.walking_frames_l.append(image)
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
        # move the player
        # Gravity
        self.calc_grav()

        # move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # see if hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # move up/down
        self.rect.y += self.change_y

        # check if hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # stop vertival movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        # calc effects of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # see if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # if it's ok to jump, set speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player Controlled Movement
    def go_left(self):
        # called when user hits the Left Arrow
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        self.change_x =6
        self.direction = "R"

    def stop(self):
        # called when nothing is being pressed
        self.change_x = 0
