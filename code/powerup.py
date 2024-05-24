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

playerimg = pygame.image.load(path.join(img_dir,"player.png")).convert()
bulletupimg = pygame.image.load(path.join(img_dir,"bulletup.png")).convert()
speedupimg = pygame.image.load(path.join(img_dir,"speedup.png")).convert()
healthupimg = pygame.image.load(path.join(img_dir,"healthup.png")).convert()
roundbulletimg = pygame.image.load(path.join(img_dir,"roundbullet.png")).convert()
shieldimg = pygame.image.load(path.join(img_dir,"shield.png")).convert()
shieldupimg = pygame.image.load(path.join(img_dir,"shieldup.png")).convert()
shield_symbolimg = pygame.image.load(path.join(img_dir,"shieldsymbol.png")).convert()
missileimg = pygame.image.load(path.join(img_dir,"missile.png")).convert()
missile_symbolimg = pygame.image.load(path.join(img_dir,"missilesymbol.png")).convert()
missileupimg = pygame.image.load(path.join(img_dir,"missileup.png")).convert()

class Bulletup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -800
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()

class Speedup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = speedupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = random.randrange(0,width-self.rect.width)
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()

class Healthup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = healthupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -800
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()

class Liveup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(playerimg,(35,25))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -800
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()

class Shieldup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = shieldupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = -500
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill()

class Missileup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = missileupimg
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,width-self.rect.width)
        self.rect.y = random.randrange(0,width-self.rect.width)
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.kill() 
            
class Missile(pygame.sprite.Sprite):
    def __init__(self,centerx,centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missileimg,(50,70))
        self.image.set_colorkey((black))
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedy = -7

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()