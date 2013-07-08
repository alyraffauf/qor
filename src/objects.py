# Alien Invasion: 2150 - a game inspired by Space Invaders
# Copyright (C) 2011 Thomas Chace <ithomashc@gmail.com>

# Alien Invasion: 2150 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Alien Invasion: 2150 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
import random
from pygame.locals import *
from utils import *

import os, sys

random.seed()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = load_image("asteroid.png")
        self.position = [random.randrange(0, 640 - 24), -24]
        self.rect = Rect(self.position[0], self.position[1], 24, 24)
        self.x_speed = random.randrange(-1,1)
        self.y_speed = 3

    def update(self, missles, player):
        self.rect.left += self.x_speed
        self.rect.top += self.y_speed
        self.position = (self.position[0] + self.x_speed, self.position[1] + self.y_speed)
              
class Missle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = load_image("asteroid.png")
        self.position = [random.randrange(0, 640 - 24), -24]
        self.rect = Rect(self.position[0], self.position[1], 24, 24)
        self.x_speed = 0
        self.y_speed = -8

    def update(self):
        self.rect.left += self.x_speed
        self.rect.top += self.y_speed
        self.position = (self.position[0] + self.x_speed, self.position[1] + self.y_speed)

class Ship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image("spaceship.png", -1)
        #self.image = self.image.convert()
        self.x = 320
        self.y = 432
        self.rect = Rect(self.x, self.y, 24, 24)
        self.x_speed = 0
        self.health = 10

    def decrease_health(self):
        self.health -= 1
        
    def move_left(self):
        self.x_speed = 10
       
    def move_right(self):
        self.x_speed = -10

    def stop(self):
        self.x_speed = 0

    def update(self):
        self.rect.left += self.x_speed
        self.x += self.x_speed

    def shoot(self):
        print("shoot!")
