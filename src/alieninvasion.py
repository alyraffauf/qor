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
import time
from pygame.locals import *
from utils import *
from objects import *
from player import *


class AlienInvasion():
    def __init__(self):
        self.playlist = ['spaceInvadersByPornophonique.ogg',
            'audio/drillDownBySeveredFifth.ogg']
        self.audio = Player(self.playlist)
        pygame.display.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((640, 480))
        self.screen = pygame.display.get_surface()

        pygame.display.set_caption("Alien Invasion: 2150 (Alpha)")
        
        fullname = os.path.join('./media/', "background.png")
        fullname = os.path.realpath(fullname)

        self.background = pygame.image.load(fullname)
        self.background.convert()

        self.player = Ship()
        self.font = pygame.font.Font("media/Lato-Regular.ttf", 36)

        self.audio.play()
        self.missles = pygame.sprite.Group()
        self.player_missles = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        self.num_ast = 0
        self.score = 0
        
    def draw(self):
        self.score_text = self.font.render("Score: " + str(self.score), 6, (0, 0, 0))
        self.scorepos = (10, 50)
        self.health_text = self.font.render("Health: " + str(self.player.health), 6, (0, 0, 0))
        self.health_position = (10, 10)
        self.screen = pygame.display.get_surface()
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.score_text, self.scorepos)
        self.screen.blit(self.health_text, self.health_position)
        self.screen.blit(self.player.image, self.player.position)
        for asteroid in self.asteroids:
            #asteroid.kill()
            if asteroid.position[1] > 480:
                asteroid.kill()
                self.num_ast -= 1
            else:
                self.screen.blit(asteroid.image[0], asteroid.position)
        for missle in self.missles:
            self.screen.blit(missle.image[0], missle.position)
        pygame.display.update()


    def update(self):
        self.eventInput(pygame.event.get())
        self.player.update()
        while True:
            if self.num_ast < 5:
                self.asteroids.add(Asteroid())
                self.num_ast = self.num_ast + 1
            else:
                break
        for asteroid in self.asteroids:
            if pygame.sprite.spritecollide(asteroid, self.missles, False):
                asteroid.kill()
                #self.asteroids.add(Asteroid())
                self.num_ast -= 1
                self.score += 1
            if pygame.sprite.spritecollide(asteroid, self.players, False):
                asteroid.kill()
                self.num_ast -= 1
                self.player.decreaseHealth()
            asteroid.update(self.missles, self.player)
            
        for missle in self.missles:
            missle.update()
        self.draw()
        self.player.update()

    def eventInput(self, events):
        for event in events: 
            if event.type == QUIT: 
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.player.moveRight()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.player.moveLeft()
            elif event.type == KEYUP and (event.key == K_LEFT or event.key == K_RIGHT):
                self.player.stop()
            elif event.type == KEYUP and event.key == K_SPACE:
                self.player.shoot()
                
                missle = Missle()
                missle.position = self.player.position
                missle.rect = Rect(missle.position[0], missle.position[1], 24, 24)
                self.missles.add(missle)
            else: 
                print(event)

alienInvasion = AlienInvasion()
while True:
    clock = pygame.time.Clock()
    clock.tick(60)
    alienInvasion.update()
