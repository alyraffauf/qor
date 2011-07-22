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

import pygame
import sys
import os
from pygame.locals import *
from utils import *
from objects import *
from player import *


class AlienInvasion():
    def __init__(self):
        self.playlist = ['audio/spaceInvadersByPornophonique.ogg',
            'audio/drillDownBySeveredFifth.ogg']
        self.player = Player(self.playlist)
        pygame.display.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((640, 480))
        self.screen = pygame.display.get_surface()

        pygame.display.set_caption("Alien Invasion: 2150 (Alpha)")

        self.background = loadImage("images/background.png")
        self.background.convert()

        self.spaceShip = Ship()
        self.font = pygame.font.Font(None, 36)
        
        self.text = self.font.render("Alien Invasion: 2150 (Alpha)", 
            1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.screen.get_rect().centerx
        self.textpos.centery = self.screen.get_rect().centery

        self.asteroid = Asteroid()
        self.player.play()
        
    def draw(self):
        self.screen = pygame.display.get_surface()
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.textpos)
        self.screen.blit(self.spaceShip.image, self.spaceShip.position)
        self.screen.blit(self.asteroid.image, self.asteroid.position)

        pygame.display.update()


    def show(self):
        self.eventInput(pygame.event.get())
        self.spaceShip.update()
        self.asteroid.update()
        self.draw()
        self.player.update()

    def eventInput(self, events):
        for event in events: 
            if event.type == QUIT: 
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.spaceShip.moveRight()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.spaceShip.moveLeft()
            elif event.type == KEYUP and (event.key == K_LEFT or event.key == K_RIGHT):
                self.spaceShip.stop()
            else: 
                print(event)

if __name__ == '__main__':
    alienInvasion = AlienInvasion()
    while True:
        clock = pygame.time.Clock()
        clock.tick(60)
        alienInvasion.show()
