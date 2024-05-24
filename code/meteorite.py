import pygame
import random
from pygame.locals import FULLSCREEN
import os
from os import path

black = (0,0,0)
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
width, height = screen.get_size()
img_dir = path.join(path.dirname(__file__),"img")
snd_dir = path.join(path.dirname(__file__),"snd")
meteo_list = ["m1.png","m2.png","m3.png","m4.png","m5.png","m6.png","m7.png"]

class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.meteochoice = random.choice(meteo_list)
        self.meteoriteimg_orig = pygame.image.load(path.join(img_dir, self.meteochoice)).convert()
        self.meteoriteimg_orig.set_colorkey(black)
        self.meteoriteimg = self.meteoriteimg_orig.copy()
        self.image = self.meteoriteimg
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width)
        self.rect.y = -800
        self.radius = int(self.rect.width * 0.85 / 2)
        self.speedx = random.randrange(-10,10)
        self.speedy = random.randrange(3,13)
        self.rot = 0
        self.rotspeed = random.randrange(-15,15)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot+self.rotspeed)%360
            newimage = pygame.transform.rotate(self.meteoriteimg_orig,self.rot)
            old_center = self.rect.center
            self.image = newimage
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.right < 0) or (self.rect.left > width) or (self.rect.top > height):
            self.rect.x = random.randrange(0, width)
            self.rect.y = -500
            self.speedx = random.randrange(-10, 10)
            self.speedy = random.randrange(3, 13)
