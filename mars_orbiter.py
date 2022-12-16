'''
Began: 12/16/2022
Completed: / /

This is my first project made in Github. In order to
get some practice with project management, github, and
python, I decided to work on a few problems from the book 
Impractical Python Projects.



'''

import os
import math
import random
import pygame as pg

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
LT_BLUE = (173, 216, 230)

class Satellite(pg.sprite.Sprite):

    def __init__(self, background):
        super().__init__()
        self.background = background
        self.image_sat = pg.image.load(" ").convert()
        self.image_crash = pg.image.load(" ").convert()
        self.image = self.image_sat
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK) 

        

