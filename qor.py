#!/usr/bin/env python
# Qor - a game inspired by Space Invaders
# Copyright (C) 2011 Thomas Chace <ithomashc@gmail.com>

# Qor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Qoris distributed in the hope that it will be useful,
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

pygame.init()

class GameDisplay():
    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.Font(pygame.font.match_font("FreeMono"), 36)

        #fullname = os.path.join('./media/', "background.png")
        #fullname = os.path.realpath(fullname)

        #self.background = pygame.image.load(fullname)
        #self.background.convert()

    def update(self, score, health):
        self.score_board = self.font.render("SCORE: " + str(score), 6, (26, 174, 0))
        self.health_indicator = self.font.render("HEALTH: " + str(health), 6, (26, 174, 0))

        self.score_position = (10, 50)
        self.health_position = (10, 10)

        self.screen.fill((0, 0, 0))

        #self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.score_board, self.score_position)
        self.screen.blit(self.health_indicator, self.health_position)

class GameOver():
    def __init__(self, screen, game_map):
        self.screen = screen
        self.map = game_map

        self.font = pygame.font.Font(pygame.font.match_font("FreeMono"), 50)

    def update(self, score, health):
        game_over = self.map.font.render("GAME OVER", 6, (26, 174, 0))
        game_over_position = (350, 300)

        self.screen.blit(game_over, game_over_position)

    def event_input(self, events):
        for event in events:
            if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == JOYBUTTONDOWN and event.button == 6): 
                sys.exit(0)

class Game():
    def __init__(self, game_map, screen):
        self.running = True
        self.map = game_map
        self.screen = screen
        self.game_over = GameOver(screen, game_map)

        self.player = Ship()
        self.missles = pygame.sprite.Group()
        self.player_missles = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.healthbars = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        self.num_ast = 0
        self.score = 0
        self.joysticks = []
        for i in range(0, pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
            self.joysticks[-1].init()

        self.healthbars.add(Healthbar(100))
        self.healthbars.add(Healthbar(300))
        self.healthbars.add(Healthbar(500))
        self.healthbars.add(Healthbar(700))

    def update(self):
        self.map.update(self.score, self.player.health)
        
        if self.running:
            self.event_input(pygame.event.get())
            self.player.update()

            while self.num_ast <= 5:
                self.asteroids.add(Asteroid())
                self.num_ast = self.num_ast + 1

            self.screen.blit(self.player.image, (self.player.x, self.player.y))
            for healthbar in self.healthbars:
                self.screen.blit(healthbar.image[0], healthbar.position)
                if pygame.sprite.spritecollide(healthbar, self.asteroids, False):
                    healthbar.kill()
                    self.player.decrease_health()
            for asteroid in self.asteroids:
                if pygame.sprite.spritecollide(asteroid, self.missles, False):
                    asteroid.kill()
                    self.num_ast -= 1
                    self.score += 1
                elif pygame.sprite.spritecollide(asteroid, self.players, False):
                    asteroid.kill()
                    self.num_ast -= 1
                    self.player.decrease_health()

                if asteroid.position[1] > 600:
                    asteroid.kill()
                    self.num_ast -= 1
                elif asteroid.position[0] > 800 or asteroid.position[0] < 0:
                    asteroid.x_speed *= -1
                else:
                    self.screen.blit(asteroid.image[0], asteroid.position)
                asteroid.update(self.missles, self.player)

            for missle in self.missles:
                missle.update()
                self.screen.blit(missle.image[0], (missle.x, missle.y))

        else:
            self.game_over.event_input(pygame.event.get())
            self.game_over.update(self.score + (len(self.healthbars) * 10), self.player.health)

    def event_input(self, events):
        for event in events: 
            # Keyboard Input
            if event.type == QUIT:
                sys.exit(0)
            elif (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == JOYBUTTONDOWN and event.button == 6): 
                self.running = False
            elif (event.type == KEYUP and event.key == K_SPACE) or (event.type == JOYBUTTONDOWN and event.button == 0):                
                missle = Missle(self.player.x, self.player.y)
                self.missles.add(missle)
            elif (event.type == KEYDOWN and event.key == K_LEFT):# or (event.type == JOYAXISMOTION and self.joysticks[event.joy].get_axis(0) < -0.7):
                self.player.move_right()
            elif (event.type == KEYDOWN and event.key == K_RIGHT):# or (event.type == JOYAXISMOTION and self.joysticks[event.joy].get_axis(0) > 0.7):
                self.player.move_left()
            #elif event.type == JOYAXISMOTION:
            #    if (self.joysticks[event.joy].get_axis(0) < -0.4) or (self.joysticks[event.joy].get_axis(0) > 0.4):
            #        self.player.x_speed = round(5 * self.joysticks[event.joy].get_axis(0), 1)
            #    else:
            #        self.player.x_speed = 0
            elif (event.type == KEYUP):# and (event.key == K_LEFT or event.key == K_RIGHT)):
                self.player.stop()

class Player():
    def __init__(self, playlist):
        self.playlist = playlist

        self.song = self.playlist[0]
        self.sound = load_sound(self.song)

        self.playing = False

    def play(self):
        self.sound.play()
        self.playing = True

    def stop(self):
        self.sound.stop()

    def update(self):
        if not pygame.mixer.get_busy() and not self.playing == True:
            self.sound.play()


pygame.display.set_mode((800, 600))
pygame.display.set_caption("Qor")

audio = Player(["space-invaders-by-pornophonique.ogg"])
audio.play()

screen = pygame.display.get_surface()
game_map = GameDisplay(screen)
game = Game(game_map, screen)

while True:
    clock = pygame.time.Clock()
    clock.tick(60)
    game.update()
    audio.update()
    if game.player.health == 0:
        game.running = False
        audio.stop()

    pygame.display.update()