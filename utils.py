# Qor - a game inspired by Space Invaders
# Copyright (C) 2014 Alexandra Chace <marilyn@marilync.co>

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
import os
from pygame.locals import *
    
def load_image(name, colorkey=None):
    fullname = os.path.join('./media/', name)
    fullname = os.path.realpath(fullname)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    fullname = os.path.join('./media/', name)
    fullname = os.path.realpath(fullname)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print("Cannot load sound: %s" % name)
        raise SystemExit
    return sound
