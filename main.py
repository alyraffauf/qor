#!/usr/bin/env python
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

import pygame, sys, os
from pygame.locals import *

def loadImage(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print("Cannot load image: %s" % name)
        raise SystemExit, message
    return image

def loadSound(name):
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print("Cannot load sound: %s" % name)
        raise SystemExit, message
    return sound


class EnemyShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadImage("enemyship.bmp")
        self.punching = 0

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.sound = loadSound("drill_down.ogg")
        self.shipSurface = loadImage("spaceship.bmp")
        self.window = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Alien Invasion: 2150")
        self.screen = pygame.display.get_surface()
        
        self.screen.blit(loadImage("background.bmp"), (0, 0))

        pygame.display.flip()
        self.shipPosition = (320, 432)
        self.screen.blit(self.shipSurface, self.shipPosition)

        pygame.display.flip()
        self.sound.play()

    def moveRight(self):
       self.shipPosition = (self.shipPosition[0] + 10, self.shipPosition[1])
       self.screen.blit(self.shipSurface, self.shipPosition)
       pygame.display.flip()

    def moveLeft(self):
       self.shipPosition = (self.shipPosition[0] - 10, self.shipPosition[1])
       self.screen.blit(self.shipSurface, self.shipPosition)
       pygame.display.flip()

    def eventInput(self, events):
        for event in events: 
            if event.type == QUIT: 
                sys.exit(0)
            elif event.type == 2 and event.key == 275:
                self.moveRight()
            elif event.type == 2 and event.key == 276:
                self.moveLeft()
            else: 
                print(event)

if __name__ == '__main__':
    alienInvasion = AlienInvasion()
    while True:
        alienInvasion.eventInput(pygame.event.get())
