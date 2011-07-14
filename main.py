#!/usr/bin/env python
import pygame, sys, os
from pygame.locals import *

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.sound = self.loadSound("drill_down.ogg")
        self.shipSurface = self.loadImage("spaceship.bmp")
        self.window = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Alien Invasion: 2150")
        self.screen = pygame.display.get_surface()
        self.shipPosition = (320, 432)
        self.screen.blit(self.shipSurface, self.shipPosition)
        print self.shipPosition[1]
        pygame.display.flip()
        self.sound.play()

    def loadImage(self, name):
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print("Cannot load image: %s" % name)
            raise SystemExit, message
        return image

    def loadSound(self, name):
        fullname = os.path.join('data', name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error, message:
            print("Cannot load sound: %s" % name)
            raise SystemExit, message
        return sound

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

alienInvasion = AlienInvasion()
while True:
   alienInvasion.eventInput(pygame.event.get())
