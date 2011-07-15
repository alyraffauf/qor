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

class Player():
    def __init__(self, playlist):
        self.playlist = playlist
        pygame.mixer.init()

    def play(self):
        self.song = self.playlist[0]
        self.sound = loadSound(self.song)
        self.sound.play()
        self.update()     
          
    def update(self):
        if pygame.mixer.get_busy():
            pass
        else:
            self.playlist.remove(self.song)
            self.playlist.append(self.song)
            self.start()
                
       
