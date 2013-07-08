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

pygame.display.set_mode((640, 480))
pygame.display.set_caption("Alien Invasion: 2150")

class GameDisplay():
    def __init__(self, screen):

        pygame.display.init()
        pygame.font.init()
        
        self.screen = screen

        self.font = pygame.font.Font("media/Lato-Regular.ttf", 36)

        fullname = os.path.join('./media/', "background.png")
        fullname = os.path.realpath(fullname)

        self.background = pygame.image.load(fullname)
        self.background.convert()

    def update(self, score, health):
        self.score_board = self.font.render("Score: " + str(score), 6, (0, 0, 0))
        self.health_indicator = self.font.render("Health: " + str(health), 6, (0, 0, 0))

        self.score_position = (10, 50)
        self.health_position = (10, 10)

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.score_board, self.score_position)
        self.screen.blit(self.health_indicator, self.health_position)


class Game():
    def __init__(self, game_map, screen):
        self.map = game_map
        self.screen = screen

        self.player = Ship()
        self.missles = pygame.sprite.Group()
        self.player_missles = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        self.num_ast = 0
        self.score = 0

    def update(self):
        self.event_input(pygame.event.get())
        self.player.update()
        while True:
            if self.num_ast < 5:
                self.asteroids.add(Asteroid())
                self.num_ast = self.num_ast + 1
            else:
                break
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        for asteroid in self.asteroids:
            if pygame.sprite.spritecollide(asteroid, self.missles, False):
                asteroid.kill()
                self.num_ast -= 1
                self.score += 1
            if pygame.sprite.spritecollide(asteroid, self.players, False):
                asteroid.kill()
                self.num_ast -= 1
                self.player.decrease_health()
                if self.player.health == 0:
                    print("DEAD!")
            if asteroid.position[1] > 480:
                asteroid.kill()
                self.num_ast -= 1
            elif asteroid.position[0] > 640 or asteroid.position[0] < 0:
                asteroid.x_speed = (asteroid.x_speed * -1)
            else:
                self.screen.blit(asteroid.image[0], asteroid.position)
            asteroid.update(self.missles, self.player)

        for missle in self.missles:
            missle.update()
            self.screen.blit(missle.image[0], missle.position)

    def event_input(self, events):
        for event in events: 
            if event.type == QUIT: 
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.player.move_right()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.player.move_left()
            elif event.type == KEYUP and (event.key == K_LEFT or event.key == K_RIGHT):
                self.player.stop()
            elif event.type == KEYUP and event.key == K_SPACE:
                self.player.shoot()
                
                missle = Missle()
                missle.position = (self.player.x, self.player.y)
                missle.rect = Rect(missle.position[0], missle.position[1], 24, 24)
                self.missles.add(missle)
            else: 
                print(event)


class Player():
    def __init__(self, playlist):
        self.playlist = playlist
        pygame.mixer.init()

        self.song = self.playlist[0]
        self.sound = load_sound(self.song)

        self.playing = False

    def play(self):
        self.sound.play()
        self.playing = True

    def update(self):
        if pygame.mixer.get_busy() and self.playing == True:
            pass
        else:
            self.sound.play()



audio = Player(["space-invaders-by-pornophonique.ogg"])
audio.play()

pygame.display.set_mode((640, 480))
screen = pygame.display.get_surface()
game_map = GameDisplay(screen)
game = Game(game_map, screen)

while True:
    clock = pygame.time.Clock()
    clock.tick(60)
    #if alienInvasion.player.health == 0:
    #    sys.exit()
    #else:
    game_map.update(game.score, game.player.health)
    game.update()
    audio.update()
    pygame.display.update()