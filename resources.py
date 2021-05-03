import pygame
from pygame.transform import scale
import os, inspect

pygame.mixer.init()
screen_width = 800
screen_height = 600
background_width = 9086
background_height = 600


scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0))
scriptDIR  = os.path.dirname(scriptPATH)

assets = os.path.join(scriptDIR,"images")
assets_son = os.path.join(scriptDIR,"sons")
background = pygame.image.load(os.path.join(assets, "level_1.png"))
accueil = pygame.image.load(os.path.join(assets, "menumario.png"))
character_front_img = pygame.image.load(os.path.join(assets, "still_mario.png"))
character_jump_img = pygame.image.load(os.path.join(assets, "mario_jump.png"))
brique = pygame.image.load(os.path.join(assets, "brique.png"))



sprite = []
for i in range(3):
    spr = pygame.image.load(os.path.join(assets, "mario_running.png")).subsurface((16*i,0,16,16))
    spr = scale(spr, (43, 43))
    sprite.append(spr)

sprite2 = []
for j in range(2):
    spr2 = pygame.image.load(os.path.join(assets, "goomba.png")).subsurface((16*j,0,16,16))
    spr2 = scale(spr2, (43, 43))
    sprite2.append(spr2)

sprite3 = []
for j in range(2):
    spr3 = pygame.image.load(os.path.join(assets, "goomba_trans.png")).subsurface((16*j,0,16,16))
    spr3 = scale(spr2, (43, 43))
    sprite3.append(spr2)

sprite4 = []
for j in range(2):
    spr4 = pygame.image.load(os.path.join(assets, "boite.png")).subsurface((16*j,0,16,16))
    spr4 = scale(spr4, (43, 43))
    sprite4.append(spr4)

background = scale(background, (background_width, background_height))
accueil = scale (accueil, (screen_width, screen_height))
character_front_img = scale(character_front_img, (43, 43))
character_jump_img = scale(character_jump_img, (43, 43))
brique = scale(brique, (43, 43))

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)