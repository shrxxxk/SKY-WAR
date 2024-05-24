import pygame
from pygame.locals import FULLSCREEN
import os
import math
from os import path


black = (0,0,0)
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
width, height = screen.get_size()

img_dir = path.join(path.dirname(__file__),"img")
snd_dir = path.join(path.dirname(__file__),"snd")

black = (0,0,0)
white = (255,255,255)
red  = (200,0,0)
brightred = (255,0,0)
green = (0,200,0)
brightgreen = (0,255,0)
blue = (0,0,200)
brightblue = (0,0,255)
yellow = (200,200,0)
brightyellow = (255,255,0)
purple = (200,0,200)
brightpurple = (255,0,255)
orange = (255,128,0)

img_dir = path.join(path.dirname(__file__),"img")
snd_dir = path.join(path.dirname(__file__),"snd")

explosion_anim = {}
explosion_anim['large'] = []
explosion_anim['small'] = []
explosion_anim['death'] = []
for i in range(9):
    fname = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir,fname)).convert()
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img,(100,100))
    explosion_anim['large'].append(img_lg)
    img_sm = pygame.transform.scale(img,(50,50))
    explosion_anim['small'].append(img_sm)
    fname = "sonicExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(img_dir,fname)).convert()
    img.set_colorkey(black)
    explosion_anim['death'].append(img)
    
#******Setup******
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
mybulletimg = pygame.image.load(path.join(img_dir,"mylaser.png")).convert()

class Mybullet(pygame.sprite.Sprite):
    def __init__(self,x,y,radian):
        pygame.sprite.Sprite.__init__(self)
        self.image = mybulletimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x
        self.speed = -15
        self.speedx = math.cos(radian)*self.speed
        self.speedy = math.sin(radian)*self.speed

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.bottom < 0) or (self.rect.right < 0) or (self.rect.left > width):
            self.kill()


