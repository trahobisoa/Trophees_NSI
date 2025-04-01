#Creer par a.pham 07/01/2025

import pygame
from import_tool import *


class Armes(pygame.sprite.Sprite):
    
    
    def __init__(self,hero,groups,name):
        
        super().__init__(groups)
        self.sprite_type = 'arme'
        self.hero = hero
        self.name = name
        direction = self.hero.status.split('_')[0]
        self.import_weapon_atout()
        

        
        
        #graphique
        self.weapon = self.graphique[self.name][self.name+'_stage_'+self.hero.stage]
        
        
        
        #placement des armes
        if direction == 'droite':
            
            if self.name == 'lance':
                self.image = self.weapon[1]
                self.rect = self.image.get_rect(midleft = self.hero.rect.midright + pygame.math.Vector2(-35,16))
                
            else:     
                self.image = self.weapon[1]
                self.rect = self.image.get_rect(midleft = self.hero.rect.midright + pygame.math.Vector2(-10,16))
        
        elif direction == 'gauche':
            
            if self.name == 'lance':
                self.image = self.weapon[2]
                self.rect = self.image.get_rect(midright = self.hero.rect.midleft + pygame.math.Vector2(35,16))
                
            else:
                self.image = self.weapon[2]
                self.rect = self.image.get_rect(midright = self.hero.rect.midleft + pygame.math.Vector2(10,16))
        
        elif direction == 'avant':
            
            if self.name == 'lance':
                self.image = self.weapon[0]
                self.rect = self.image.get_rect(midtop = self.hero.rect.midbottom + pygame.math.Vector2(-20,-40))
            
            else:
                self.image = self.weapon[0]
                self.rect = self.image.get_rect(midtop = self.hero.rect.midbottom + pygame.math.Vector2(-20,-20))
            
        else:
            
            if self.name == 'lance':
                self.image = self.weapon[3]
                self.rect = self.image.get_rect(midbottom = self.hero.rect.midtop + pygame.math.Vector2(25,60))
            
            else:
                self.image = self.weapon[3]
                self.rect = self.image.get_rect(midbottom = self.hero.rect.midtop + pygame.math.Vector2(23,40))
            
        
        
        
    def import_weapon_atout(self):
        
        weapon_path = '../media/Armes/Armes/'  
        
        self.graphique = {'epee': {'epee_stage_1': [], 'epee_stage_2': [], 'epee_stage_3': []},
                          'lance': {'lance_stage_1': [], 'lance_stage_2': [], 'lance_stage_3': []},
                          'katana': {'katana_stage_1': [], 'katana_stage_2': [], 'katana_stage_3': []},
                          'magie': {'magie_stage_1': [], 'magie_stage_2': [], 'magie_stage_3': []}}
        
        for AUAUAU in self.graphique.keys():
            for UAUAUA in self.graphique[AUAUAU].keys():
                full_path = weapon_path+ AUAUAU +'/' + AUAUAU+'_stage_' + self.hero.stage
                self.graphique[AUAUAU][UAUAUA] = import_folder(full_path)
            
            
            
            
    