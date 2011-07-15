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
from utils import *
from objects import *

class AlienInvasion():
    def __init__(self):
        pygame.display.init()
        pygame.mixer.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Alien Invasion: 2150 (Alpha)")
        
        self.spaceShip = Ship()
        self.draw()
        
        font = pygame.font.Font(None, 36)
        self.text = font.render("Alien Invasion: 2150 (Alpha)", 1, (10, 10, 10))
        textpos = self.text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        textpos.centery = self.screen.get_rect().centery
        self.screen.blit(self.text, textpos)

        self.sound = loadSound("drill_down.ogg")
        self.sound.play()
        
        pygame.display.flip()
        
    def draw(self):
        self.screen = pygame.display.get_surface()
        self.background = loadImage("background.bmp")
        self.background = self.background.convert()
        self.screen.blit(self.background, (0, 0))
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
