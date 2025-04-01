import pygame
import time
from settings import *
from import_tool import import_folder
from entity import Entity
from inventaire import Inventaire

class Hero(Entity):
    def __init__(self,pos,grp,obs_sprite,creer_attaque,kill_attack,magie_attaque,lvl):
        super().__init__(grp)
        self.image = pygame.image.load("../media/Joueur_Animations/avant/front_walk_2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.stage = '1'
        self.import_joueur_atout()
        self.status = 'avant'
        self.inventaire = Inventaire()
        self.lvl = lvl
        
        self.attaquant = False
        self.attaquant_magie = False
        self.attaque_recharge = 400
        self.attaque_temps = None
        self.stats = {'vie' : 100, 'energie' : 60, 'attaque' : 10, 'mana': 4, 'vitesse' : 4.5}
        self.vie = self.stats['vie']
        self.vie_max = self.vie
        self.energie = self.stats['energie']   #mana
        self.energie_max = self.energie          #mana
        self.speed = self.stats['vitesse']
        self.obstacle_sprites = obs_sprite
        
        self.creer_attaque = creer_attaque
        self.detruire_arme = kill_attack
        self.armes_index = 0
        self.arme = None
        self.peut_change_armes = True
        self.change_armes_temps = None
        self.change_recharge = 200
        self.invincible = False
        self.hit_time = None
        self.hit_cooldown = 600
        #magie
        self.magie_attaque = magie_attaque
        self.magie_index = 0
        self.magie = list(magie_data.keys())[self.magie_index]
        self.peut_change_magie = True
        self.change_magie_temps = None
        
        
    
    def import_joueur_atout(self):
        
        caractere_path = '../media/Joueur_Animations/'  #complete with folder with animations
        
        self.animations = {'avant': [''], 'arriere': [''],'gauche': [''], 'droite': [],'avant_idle': [''], 'arriere_idle': [''], 'gauche_idle': [''],'droite_idle': [''],
                           'avant_attaque': [''], 'arriere_attaque': [''],'gauche_attaque': [''], 'droite_attaque': ['']}
        for animation in self.animations.keys():
            full_path = caractere_path + animation
            self.animations[animation] = import_folder(full_path)

        
    def key_input(self):
        
        #mouvement
        if self.attaquant != True:

            key = pygame.key.get_pressed()
            if key[pygame.K_UP] or key[pygame.K_w]:
                self.direction.y = -1
                self.status = 'arriere'
            elif key[pygame.K_DOWN] or key[pygame.K_s]:
                self.direction.y = 1
                self.status = 'avant'
            else:
                self.direction.y = 0
            
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.direction.x = -1
                self.status = 'gauche'
            elif key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.direction.x = 1
                self.status = 'droite'
            else:
                self.direction.x = 0
                
            
            #attaque
                
            if key[pygame.K_SPACE]:
                if self.arme != None:
                    self.attaquant = True
                    self.attaque_temps = pygame.time.get_ticks()
                    self.creer_attaque()
                
            
            
            #magie
                
            if key[pygame.K_LCTRL]:
                self.attaquant_magie = True
                self.attaque_temps = pygame.time.get_ticks()
                self.magie_attaque('tempest',self.stats["mana"],magie_data['tempest']['degats'],[self.lvl.graphics_sprites,self.lvl.attack_sprites])
                print('magie')
         
         
         
            if key[pygame.K_q] and self.peut_change_armes:
                self.peut_change_armes = False
                self.change_armes_temps = pygame.time.get_ticks()
                
                if self.armes_index < len(list(self.inventaire.objet.items())) - 1:
                    self.armes_index += 1
                    
                else:
                    self.armes_index = 0
                    
                if self.inventaire.objet != {}:
                    self.arme = list(self.inventaire.objet.items())[self.armes_index][0]
                else:
                    self.arme = None
         
       
    def get_status(self):
        
        
        #idle_status
        
        if self.direction.x == 0 and self.direction.y == 0:
            
            if not 'idle' in self.status and not 'attaque' in self.status:
                self.status = self.status + '_idle'
                
            
        if self.attaquant:
            
            self.direction.x = 0
            self.direction.y = 0
            
            if not 'attaque' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attaque')
                else:
                    self.status = self.status + '_attaque'
       
        else:
            if 'attaque' in self.status:
                self.status = self.status.replace('_attaque','')     

        if self.vie <= 0:
            son_mort = pygame.mixer.Sound('../media/son/mort.mp3')
            musique_mort = pygame.mixer.Sound('../media/son/mort_musique.mp3')
            son_mort.play()
            pygame.mixer.music.unload()
            musique_mort.play()
            self.kill()
            self.lvl.end_game('lose')
    
    
    def recharge(self):
        
        temps_instant = pygame.time.get_ticks()
        
        if self.attaquant:
            if temps_instant - self.attaque_temps >= self.attaque_recharge + self.inventaire.objet[self.arme]['cooldown']:
                self.attaquant = False
                
                self.detruire_arme()

        if self.attaquant_magie:
            if temps_instant - self.attaque_temps >= self.attaque_recharge + magie_data[self.magie]['cooldown']:
                self.attaquant_magie = False
                
                self.detruire_arme()
                
        if not self.peut_change_armes:
            if temps_instant - self.change_armes_temps >= self.change_recharge:
                self.peut_change_armes = True

        if self.invincible:
            if temps_instant - self.hit_time >= self.hit_cooldown:
                self.invincible = False

    def get_weapon_dmg(self):
        hero_dmg = self.stats['attaque']
        weapon_dmg = self.inventaire.objet[self.arme]['damage']
        return hero_dmg + weapon_dmg
    def get_magie_dmg(self):
        dmg_base = self.stats['attaque']
        dmg_magie = magie_data[self.magie]['degats']
        return dmg_base + dmg_magie
    
    def affect_health(self,amount):
        if self.vie+amount > self.vie_max:
            self.vie = self.vie_max
        else:
            self.vie += amount
        print(self.vie)

    def energie_recharge(self):
        '''Methode qui recharge les points de mana'''
        
        if self.energie < self.stats['energie']:
            self.energie += 0.01 * self.stats['mana']
        else:
            self.energie = self.stats['energie']
    
    def animer(self):
        
        animations = self.animations[self.status]
        
        
        #loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animations):
            self.frame_index = 0
                        
        self.image = animations[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if self.invincible:
            alpha = self.flicker()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
        
    
    def update(self):
        self.key_input()
        self.recharge()
        self.get_status()
        self.animer()
        self.move(self.speed)
        self.energie_recharge()
            