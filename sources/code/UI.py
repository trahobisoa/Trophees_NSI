import pygame
from settings import *
from tile import Tile

from import_tool import *





class Ui:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        #init des coeurs     
        path = '../media/UI/Barre de vie/'      
        self.coeur_complet = pygame.image.load(path+'coeur_1.png').convert_alpha()
        self.coeur_troisquarts = pygame.image.load(path+'coeur_2.png').convert_alpha()
        self.coeur_moitie = pygame.image.load(path+'coeur_3.png').convert_alpha()
        self.coeur_unquart = pygame.image.load(path+'coeur_4.png').convert_alpha()
        self.coeur_vide = pygame.image.load(path+'coeur_5.png').convert_alpha()
        self.display_inv = False
        self.inventaire_img = pygame.image.load("../media/UI/inventaire/inventaire.png")

        #convertir dictionnaire armes
        self.magie_graphiques = []
        for magies in magie_data:
            magie = pygame.image.load(magie_data[magies]['graphic']+'_h.png').convert_alpha()
            self.magie_graphiques.append(magie)

        path_ = '../media/UI/Mana/'
        self.mana_complet = pygame.image.load(path_+'mana_1.png').convert_alpha()
        self.mana_troisquarts = pygame.image.load(path_+'mana_2.png').convert_alpha()
        self.mana_moitie = pygame.image.load(path_+'mana_3.png').convert_alpha()
        self.mana_unquart = pygame.image.load(path_+'mana_4.png').convert_alpha()
        self.mana_vide = pygame.image.load(path_+'mana_5.png').convert_alpha()
        
        
        
    def vie(self,hero):
        x = 10
        if hero.vie<=0:
            for i in range(hero.vie_max//20):
                self.display_surface.blit(self.coeur_vide,(x,10))
                x+=70
        else:
            for i in range(hero.vie//20):
                self.display_surface.blit(self.coeur_complet,(x,10))
                x+=70
            vie_restante = hero.vie%20
            if vie_restante == 0:
                pass
            elif vie_restante >= 3/4*20:
                self.display_surface.blit(self.coeur_troisquarts,(x,10))
                x+=70
            elif vie_restante >= 2/4*20:
                self.display_surface.blit(self.coeur_moitie,(x,10))
                x+=70
            elif vie_restante >= 0:
                self.display_surface.blit(self.coeur_unquart,(x,10))
                x+=70
            for i in range((hero.vie_max-hero.vie)//20): 
                self.display_surface.blit(self.coeur_vide,(x,10))
                x+=70

    def mana(self,hero):
        
        '''Methode qui affiche les points de mana en fonction de hero.stats['mana']'''
        
        x = 10
        if hero.energie<=0:
            for i in range(hero.energie_max//20):
                self.display_surface.blit(self.mana_vide,(x,75))
                x+=70
        else:
            for i in range(int(hero.energie)//20):
                self.display_surface.blit(self.mana_complet,(x,75))
                x+=70
            energie_restante = hero.energie%20
            if energie_restante == 0:
                pass
            elif energie_restante >= 3/4*20:
                self.display_surface.blit(self.mana_troisquarts,(x,75))
                x+=70
            elif energie_restante >= 2/4*20:
                self.display_surface.blit(self.mana_moitie,(x,75))
                x+=70
            elif energie_restante >= 0:
                self.display_surface.blit(self.mana_unquart,(x,75))
                x+=70
            for i in range(int(hero.energie_max-hero.energie)//20): 
                self.display_surface.blit(self.mana_vide,(x,75))
                x+=70
            
    
    
    def boite(self,left,top,changer):
        
        boite_rect = pygame.Rect(left,top,64,64)
        pygame.draw.rect(self.display_surface,(128,128,128),boite_rect)
        
        if changer:
            pygame.draw.rect(self.display_surface,(128,128,128),boite_rect,10)
        else:
            pygame.draw.rect(self.display_surface,(128,128,128),boite_rect,10)
            
        return boite_rect
        
        
        
    def armes_montrer(self,hero,changer):
        
        boite_rect = self.boite(10,SCREEN_HEIGHT-100,changer)   #armes
        if hero.arme != None:
            stage_arme = hero.arme+'_stage_'+ hero.stage
            armes_surf = pygame.image.load('../media/Armes/Armes/'+hero.arme+'/'+stage_arme+'/'+stage_arme+'_d.png')
            armes_rect = armes_surf.get_rect(center = boite_rect.center)
        
        
            self.display_surface.blit(armes_surf,armes_rect)
        
        
    def magie_montrer(self,magie_index,changer):
        
        boite_rect = self.boite(90,SCREEN_HEIGHT-100,changer)    #magie
        magie_surf = self.magie_graphiques[magie_index]
        magie_rect = magie_surf.get_rect(center = boite_rect.center)
        
        self.display_surface.blit(magie_surf,magie_rect)

    def display_inventory(self):
        if self.display_inv == False:
            self.display_inv = True
        else:
            self.display_inv = False

    def hero_inventory(self,hero):
        inventaire_rect = self.inventaire_img.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        self.display_surface.blit(self.inventaire_img,inventaire_rect)
        i = 0
        for arme in hero.inventaire.objet.keys():
            stage_arme = arme+'_stage_'+ hero.stage
            arme_surf = pygame.image.load('../media/Armes/Armes/'+arme+'/'+stage_arme+'/'+stage_arme+'_h.png')
            arme_rect = arme_surf.get_rect(center = (inventaire_rect.left + 105+i*207, inventaire_rect.centery-45) )
            i+=1
            self.display_surface.blit(arme_surf,arme_rect)
        if len(hero.inventaire.trophee) != 0:
            trophee_surf = pygame.image.load("../media/items/"+hero.inventaire.trophee['golem'])
            trophee_rect = trophee_surf.get_rect(center = (inventaire_rect.left + 162,inventaire_rect.bottom - 70))
            self.display_surface.blit(trophee_surf,trophee_rect)

    
    
    def display(self,hero):
        
        self.armes_montrer(hero,not hero.peut_change_armes )
        self.magie_montrer(hero.magie_index, not hero.peut_change_magie)
        if self.display_inv == True:
            self.hero_inventory(hero)
        
        
    
    def update(self,hero):
        self.vie(hero)
        self.mana(hero)
        self.display(hero)
        
        
        
            