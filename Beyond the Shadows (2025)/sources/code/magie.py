##Creer par a.pham 21/02/2025

import pygame
from settings import *
from random import randint



class Magie:
    
    def __init__(self,animation_joueur):
        
        self.animation_joueur = animation_joueur
        
    
    def tempest(self,hero,mana,groups):
        
        if hero.energie >= mana:
            hero.energie -= mana
            
            
            if hero.status.split('_')[0] == 'droite':
                direction = pygame.math.Vector2(1,0)
                
            elif hero.status.split('_')[0] == 'gauche':
                direction = pygame.math.Vector2(-1,0)
            
            elif hero.status.split('_')[0] == 'avant':
                direction = pygame.math.Vector2(0,1)
                
            else:
                direction = pygame.math.Vector2(0,-1)
                
                
            for i in range(1,6):
                
                if direction.x:
                    offset_x = (direction.x * i) * TILESIZE
                    x = hero.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = hero.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_joueur.creer_particules('tempest',(x,y),groups)
                else:
                    offset_y = (direction.y * i) * TILESIZE
                    x = hero.rect.centerx  + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = hero.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_joueur.creer_particules('tempest',(x,y),groups)
    
    
    def death_purple(self,hero,mana,groups):
        if hero.energie >= mana:
            hero.energie -= mana
            
            
            if hero.status.split('_')[0] == 'droite':
                direction = pygame.math.Vector2(1,0)
                
            elif hero.status.split('_')[0] == 'gauche':
                direction = pygame.math.Vector2(-1,0)
            
            elif hero.status.split('_')[0] == 'avant':
                direction = pygame.math.Vector2(0,1)
                
            else:
                direction = pygame.math.Vector2(0,-1)
                
                
            for i in range(1,6):
                
                if direction.x:
                    offset_x = (direction.x * i) * TILESIZE
                    x = hero.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = hero.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_joueur.creer_particules('death_purple',(x,y),groups)
                else:
                    offset_y = (direction.y * i) * TILESIZE
                    x = hero.rect.centerx  + randint(-TILESIZE // 3, TILESIZE // 3)
                    y = hero.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_joueur.creer_particules('death_purple',(x,y),groups)