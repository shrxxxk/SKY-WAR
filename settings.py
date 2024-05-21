import pygame
from pygame.locals import FULLSCREEN
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
icon =  pygame.image.load(path.join(img_dir,"icon1.png")).convert()
icon.set_colorkey(black)
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#******load_graphic********
background = pygame.image.load(path.join(img_dir,"background.jpg")).convert()
backgound = pygame.transform.scale(background,(width,height))
introbackground = pygame.image.load(path.join(img_dir,"introbackground.jpg")).convert()
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
on_music = pygame.transform.scale(on_music,(40,40))
off_music = pygame.image.load(path.join(img_dir,"musik_mati.png")).convert()
off_music = pygame.transform.scale(off_music,(40,40))

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

#******load_sound********
bulletup_sound = pygame.mixer.Sound(path.join(snd_dir,'bulletup.wav'))
shieldup_sound = pygame.mixer.Sound(path.join(snd_dir,'shieldup.wav'))
healthup_sound = pygame.mixer.Sound(path.join(snd_dir,'healthup.wav'))
liveup_sound = pygame.mixer.Sound(path.join(snd_dir,'liveup.wav'))
missileup_sound = pygame.mixer.Sound(path.join(snd_dir,'missileup.wav'))
speedup_sound = pygame.mixer.Sound(path.join(snd_dir,'speedup.wav'))

explodesm_sound = pygame.mixer.Sound(path.join(snd_dir,'explodesm.wav'))
explodebg_sound = pygame.mixer.Sound(path.join(snd_dir,'explodebg.wav'))
explodedeath_sound = pygame.mixer.Sound(path.join(snd_dir,'explodedeath.wav'))

shoot_sound = pygame.mixer.Sound(path.join(snd_dir,'shoot.wav'))
missile_sound = pygame.mixer.Sound(path.join(snd_dir,'missile.wav'))
shield_sound = pygame.mixer.Sound(path.join(snd_dir,'shield.wav'))
