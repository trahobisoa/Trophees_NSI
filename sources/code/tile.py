import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,grp,sprite_type,surf = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(grp)
        self.sprite_type = sprite_type
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        