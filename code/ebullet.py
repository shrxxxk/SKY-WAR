import pygame
import math
from pygame.locals import FULLSCREEN
import os
from os import path

screen = pygame.display.set_mode((0, 0), FULLSCREEN)
width, height = screen.get_size()
fps = 60

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

#******Setup******
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Sky War")
clock = pygame.time.Clock()

#******load_graphic********
background = pygame.image.load(path.join(img_dir,"background.jpg")).convert()
backgound = pygame.transform.scale(background,(width,height))
introbackground = pygame.image.load(path.join(img_dir,"introbackground.png")).convert()
introbackground = pygame.transform.scale(introbackground,(width,height))
infobackground = pygame.image.load(path.join(img_dir,"infobackground.jpg")).convert()
infobackground = pygame.transform.scale(infobackground,(width,height))
gameoverbackground = pygame.image.load(path.join(img_dir,"gameover.jpg")).convert()
gameoverbackground = pygame.transform.scale(gameoverbackground,(width,height))
playerimg = pygame.image.load(path.join(img_dir,"player.png")).convert()
liveupimg = pygame.transform.scale(playerimg,(50,40))
meteo_list = ["m1.png","m2.png","m3.png","m4.png","m5.png","m6.png","m7.png"]
mybulletimg = pygame.image.load(path.join(img_dir,"mylaser.png")).convert()
bulletupimg = pygame.image.load(path.join(img_dir,"bulletup.png")).convert()
speedupimg = pygame.image.load(path.join(img_dir,"speedup.png")).convert()
healthupimg = pygame.image.load(path.join(img_dir,"healthup.png")).convert()
enemy1img = pygame.image.load(path.join(img_dir,"enemy1img.png")).convert()
enemy2img = pygame.image.load(path.join(img_dir,"enemy2img.png")).convert()
roundbulletimg = pygame.image.load(path.join(img_dir,"roundbullet.png")).convert()
boss1img = pygame.image.load(path.join(img_dir,"boss1.png")).convert()
laser1img = pygame.image.load(path.join(img_dir,"laser1.png")).convert()
enemy3img = pygame.image.load(path.join(img_dir,"enemy3.png")).convert()
dartimg = pygame.image.load(path.join(img_dir,"dart.png")).convert()
boss2img = pygame.image.load(path.join(img_dir,"boss2.png")).convert()
boss3img = pygame.image.load(path.join(img_dir,"boss3.png")).convert()
ximg = pygame.image.load(path.join(img_dir,"x.png")).convert()
shieldimg = pygame.image.load(path.join(img_dir,"shield.png")).convert()
shieldupimg = pygame.image.load(path.join(img_dir,"shieldup.png")).convert()
shield_symbolimg = pygame.image.load(path.join(img_dir,"shieldsymbol.png")).convert()
missileimg = pygame.image.load(path.join(img_dir,"missile.png")).convert()
missile_symbolimg = pygame.image.load(path.join(img_dir,"missilesymbol.png")).convert()
missileupimg = pygame.image.load(path.join(img_dir,"missileup.png")).convert()
upimg = pygame.image.load(path.join(img_dir,"up.png")).convert()
upimg = pygame.transform.scale(upimg,(40,40))
downimg = pygame.image.load(path.join(img_dir,"down.png")).convert()
downimg = pygame.transform.scale(downimg,(40,40))
leftimg = pygame.image.load(path.join(img_dir,"left.png")).convert()
leftimg = pygame.transform.scale(leftimg,(40,40))
rightimg = pygame.image.load(path.join(img_dir,"right.png")).convert()
rightimg = pygame.transform.scale(rightimg,(40,40))
spaceimg = pygame.image.load(path.join(img_dir,"space.png")).convert()
spaceimg = pygame.transform.scale(spaceimg,(80,40))
on_music = pygame.image.load(path.join(img_dir,"musik_hidup.png")).convert()
on_music = pygame.transform.scale(on_music,(80,40))
off_music = pygame.image.load(path.join(img_dir,"musik_mati.png")).convert()
off_music = pygame.transform.scale(off_music,(80,40))
lose = pygame.image.load(path.join(img_dir,"gameoverimg.png")).convert_alpha()

class Roundbullet(pygame.sprite.Sprite):
    def __init__(self,x,y,degree):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(roundbulletimg,(30,30))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 7
        self.speedx = self.speed*math.sin(math.radians(degree))
        self.speedy = self.speed * math.cos(math.radians(degree))

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.top > height) or (self.rect.right < 0) or (self.rect.left > width):
            self.kill()
class Laser1(Roundbullet):
    def __init__(self,x,y,degree):
        super().__init__()
        self.image = pygame.transform.scale(laser1img, (30,30))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

class Dart(Roundbullet):
    def __init__(self,x,y,degree):
        super().__init__(x,y,degree)
        self.img_orig = dartimg
        self.img_orig.set_colorkey(black)
        self.image = self.img_orig.copy()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.rot = 0
        self.rotspeed = 15
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rotspeed) % 360
            newimage = pygame.transform.rotate(self.img_orig, self.rot)
            old_center = self.rect.center
            self.image = newimage
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rotate()
        if (self.rect.top > height) or (self.rect.right < 0) or (self.rect.left > width):
            self.kill()

class X(Dart):
    def __init__(self,x,y,degree):
        super().__init__()
        self.img_orig = dartimg
        self.img_orig.set_colorkey(black)
        self.image = self.img_orig.copy()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.rot = 0
        self.rotspeed = 30
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = -(self.rot + self.rotspeed) % 360
            newimage = pygame.transform.rotate(self.img_orig, self.rot)
            old_center = self.rect.center
            self.image = newimage
            self.rect = self.image.get_rect()
            self.rect.center = old_center