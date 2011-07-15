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

class Asteroid():
    def __init__(self):
        self.rect = pygame.Surface((24,24))
        self.rect = self.rect.convert()
        self.rect.fill((250, 250, 250))

class Alien():
    def __init__(self):
        self.rect = pygame.Surface((48,48))
        self.rect = self.rect.convert()
        self.rect.fill((250, 250, 250))

class Ship():
    def __init__(self):
        self.image = loadImage("spaceship.bmp")
        self.position = (320, 432)
        
    def moveLeft(self):
        self.position = (self.position[0] - 10, self.position[1])
       
    def moveRight(self):
        self.position = (self.position[0] + 10, self.position[1])

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.spaceShip = Ship()
        self.window = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Alien Invasion: 2150")
        
        self.draw()
        
        font = pygame.font.Font(None, 36)
        self.text = font.render("Alien Invasion: 2150", 1, (10, 10, 10))
        textpos = self.text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        textpos.centery = self.screen.get_rect().centery
        self.screen.blit(self.text, textpos)

        self.sound = loadSound("drill_down.ogg")
        self.sound.play()
        
        pygame.display.flip()
        
    def draw(self):
        self.screen = pygame.display.get_surface()
        self.screen.blit(loadImage("background.bmp"), (0, 0))
        self.screen.blit(self.spaceShip.image, self.spaceShip.position)
        
    def eventInput(self, events):
        for event in events: 
            if event.type == QUIT: 
                sys.exit(0)
            elif event.type == 2 and event.key == 275:
                self.spaceShip.moveRight()
                self.draw()
                pygame.display.update()
            elif event.type == 2 and event.key == 276:
                self.spaceShip.moveLeft()
                self.draw()
                pygame.display.update()
            else: 
                print(event)

if __name__ == '__main__':
    alienInvasion = AlienInvasion()
    while True:
        clock = pygame.time.Clock()
        clock.tick(60)
        alienInvasion.eventInput(pygame.event.get())
