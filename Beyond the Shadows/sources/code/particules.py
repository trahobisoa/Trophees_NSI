#Creer par a.pham 21/02/2025

import pygame
from import_tool import import_folder
from random import choice




class AnimationJoueur:
    
    
    def __init__(self):
        
        self.cadre = {
            
        #magie
        'tempest': import_folder('../media/Particules/magie/magie_stage_1'),
        'death_purple': import_folder('../media/Particules/magie/magie_stage_2'),
        
        #adversaires_attaques
        'fleur_physique': import_folder('../media/Particules/Attaque_test/fleur/physique'),
        'fleur_projectile': import_folder('../media/Particules/Attaque_test/fleur/projectile'),
        'golem_physique': import_folder('../media/Particules/Attaque_test/golem/physique'),
        'golem_gamme': import_folder('../media/Particules/Attaque_test/golem/gamme'),
        'mini_golem': import_folder('../media/Particules/Attaque_test/mini_golem'),
        'goblin': import_folder('../media/Particules/Attaque_test/goblin'),
        'loup': import_folder('../media/Particules/Attaque_test/loup'),
        'rose': import_folder('../media/Particules/Attaque_test/rose'),
        'serpent': import_folder('../media/Particules/Attaque_test/serpent'),
        'squelette': import_folder('../media/Particules/Attaque_test/squelette'),
        
        #adversaires_morts
        'fleur': import_folder('../media/Particules/Mort/fleur'),
        'golem': import_folder('../media/Particules/Mort/golem'),
        'mini_golem': import_folder('../media/Particules/Mort/mini_golem'),
        'goblin': import_folder('../media/Particules/Mort/goblin'),
        'loup': import_folder('../media/Particules/Mort/loup'),
        'rose': import_folder('../media/Particules/Mort/rose'),
        'serpent': import_folder('../media/Particules/Mort/serpent'),
        'squelette': import_folder('../media/Particules/Mort/squelette'),
        
#         #feuilles_scenes
#         'feuille': (
#                     import_folder('../media/Particules/Feuille/feuille_1'),
#                     import_folder('../media/Particules/Feuille/feuille_2'),
#                     import_folder('../media/Particules/Feuille/feuille_3'),
#                     import_folder('../media/Particules/Feuille/feuille_4'),
#                     import_folder('../media/Particules/Feuille/feuille_5'),
#                     import_folder('../media/Particules/Feuille/feuille_6'),
#                     self.reflet_image(import_folder('../media/Particules/Feuille/feuille_1')),
#                     self.reflet_image(import_folder('../media/Particules/Feuille/feuille_2')),
#                     self.reflet_image(import_folder('../media/Particules/Feuille/feuille_3')),
#                     self.reflet_image(import_folder('../media/Particules/Feuille/feuille_4')),
#                     self.reflet_image(import_folder('../media/Particules/Feuille/feuille_5')),
#                     self.reflet_image(import_folder('../media/Particules/Feuille/feuille_6')),
#                    )
        
        #effet arriere plan
        'feuilles': (
                    import_folder('../media/Particules/Scene/Feuille/feuille_1'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_2'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_3'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_4'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_5'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_6'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_7'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_8'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_9'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_10'),
                    import_folder('../media/Particules/Scene/Feuille/feuille_11')
                    ),
        
        'herbe_roulant': import_folder('../media/Particules/Scene/Herbe_roulant'),
        
                      }
        
        
    
    def reflet_image(self,cadre):
        
        nouveau_cadre = []
        for cadres in cadre:
            cadre_inverse = pygame.transform.flip(cadres,True,False)
            nouveau_cadre.append(cadre_inverse)
        return nouveau_cadre
            

    def creer_particules_feuille(self,pos,groups):
        
        animation_cadre = choice(self.cadre['feuille'])
        Particules(pos,animation_cadre,groups)
        
    
    def creer_particules(self,animation_type,pos,groups):
        
        animation_cadre = self.cadre[animation_type]
        Particules(pos,animation_cadre,groups)
        
    

    
    
    def scene_feuilles(self,pos,groups):
        
        animation_cadre = choice(self.cadre['feuilles'])
        Particules(pos,animation_cadre,groups)
    
    
    
    def scene_herbe_roulant(self,pos,groups):
        
        animation_cadre = self.cadre['herbe_roulant']
        Particules(pos,animation_cadre,groups)
    
    
        
        
        


class Particules(pygame.sprite.Sprite):
    
    def __init__(self,pos,animation_cadre,groups):
        
        super().__init__(groups)
        self.screen = pygame.display.get_surface()
        self.sprite_type = 'magie'
        self.cadre_index = 0
        self.vitesse_anime = 0.15
        self.cadre = animation_cadre
        self.image = self.cadre[self.cadre_index]
        self.rect = self.image.get_rect(center = pos)
        
        
        
        
    def anime(self):
        
        self.cadre_index += self.vitesse_anime
        if self.cadre_index >= len(self.cadre):
            self.kill()
        else:
            self.image = self.cadre[int(self.cadre_index)]
            self.screen.blit(self.image,self.rect)
            
            
    def update(self):
        
        self.anime()