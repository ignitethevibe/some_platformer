# -- Collection of Background Animations
import pygame
from constants import *
from spritesheet_functions import SpriteSheet
import chars





class CharSprites(pygame.sprite.Sprite):
    def __init__(self, file_name, char_sprite):
        #super(CharSprites, self).__init__()

        self.change_x = 0
        self.change_y = 0

        # animation frames
        self.moving_frames_r = []
        self.moving_frames_l = []

        clock = pygame.time.Clock()
        ###
        self.animation_time = 0.1
        self.current_time = 0
        dt = clock.tick(frame_rate) / 1000
        self.animation_frames = 6
        self.current_frame = 0



        self.direction = "L"

        self.sprite_sheet = SpriteSheet(file_name)
        char_sprite = []

    def char_sprite(self):
        for i in char_sprite:
            image = sprite_sheet.get_image(char_sprite[0],
                                        char_sprite[1],
                                        char_sprite[2],
                                        char_sprite[3])
            self.moving_frames_l.append(image)

        # Flip
            image = sprite_sheet.get_image(char_sprite[0],
                                        char_sprite[1],
                                        char_sprite[2],
                                        char_sprite[3])
            image = pygame.transform.flip(image, True, False)
            self.moving_frames_r.append(image)
        return image

        self.image = self.moving_frames_l[0]

        self.rect = self.image.get_rect()

        self.index = 0
        self.image = moving_frames_l[self.index]

        self.rect.x = 0
        self.rect.y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self, dt):

        self.rect.x += self.change_x

        ####
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.moving_frames_l)
            self.image = self.moving_frames_l[self.index]


        pos = self.rect.x + self.level.world_shift
        #if self.direction == "L":
            #frame = (pos // 30) % len(self.moving_frames_l)
            #self.image = self.moving_frames_l[frame]
        #else:
            #frame = (pos // 30) % len(self.moving_frames_r)
            #self.image = self.moving_frames_r[frame]

        self.rect.y += self.change_y

        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
