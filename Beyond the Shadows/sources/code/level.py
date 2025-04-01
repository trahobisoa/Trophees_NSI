import pygame
from settings import *
from tile import Tile
from hero import Hero
from import_tool import *
from enemy import Enemy
from armes import Armes
from NPC import *
from UI import Ui
from magie import Magie
from particules import AnimationJoueur
from Boss import *

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.lvl = Map(0)
        self.graphics_sprites = Camera_sprite(self.lvl)
        self.graphics_sprites.get_floor()
        self.obstacle_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.border = []
        self.enemies = []
        self.entities = []
        self.hero = Hero((1344,3712),[self.graphics_sprites],self.obstacle_sprites,self.creer_attaque,self.detruire_arme,self.magie_attaque,self)
        #chests
        self.chest = {'chest_labyrinth':'closed','chest_map_4':'closed','chest_jungle':'closed','chest_town':'closed'}
        self.create_map()
        self.pause = False
        self.attaque_actuel = None
        self.ui = Ui()
        self.last_input_time = 0
        self.inventory_cooldown = 400

         #Magie
        self.animation_joueur = AnimationJoueur()
        self.magie_joueur = Magie(self.animation_joueur)
        
    
    def create_map(self): #ajouter les collisions et entitées de chaque map
        for j in self.border:
            j.kill()
        for n in self.enemies:
            n.kill()
        for k in self.entities:
            k.kill()

        layouts = {
        'border' : self.lvl.border,
        'entities' : self.lvl.entities
        }

        for type,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if type == 'border':
                            self.border.append(Tile((x,y),self.obstacle_sprites,'border'))
                        if type == 'entities':
                            if col == '3442': enemy_type = 'rope'
                            elif col == '3443': enemy_type = 'goblin'
                            elif col == '3444': enemy_type = 'rose'
                            elif col == '3445': enemy_type = 'slime'
                            elif col == '3446': enemy_type = 'mini_golem'
                            elif col == '3447': enemy_type = 'squelette'
                            self.enemies.append(Enemy(enemy_type,(x,y),[self.graphics_sprites,self.attackable_sprites],self.obstacle_sprites,self.dmg_hero))
        if self.lvl.lvl_number == 0:
            self.entities.append(Jean((27*64,54*64),[self.graphics_sprites],self.obstacle_sprites,False,self,self.hero))
            self.entities.append(Hugo((15*64,100*64),[self.graphics_sprites],self.obstacle_sprites,False,self,self.hero))
            self.entities.append(Rahobisoa((32*64,87*64),[self.graphics_sprites],self.obstacle_sprites,False,self,self.hero))
            self.entities.append(Liam((60*64,39*64),[self.graphics_sprites],self.obstacle_sprites,False,self,self.hero))
            self.entities.append(Chest((69*64,103*64),[self.graphics_sprites,self.obstacle_sprites],self,self.hero,'grey',('quete',{'materiaux': 'materiaux_stage_1'}),self.chest['chest_labyrinth'],'chest_labyrinth'))
            if 'materiaux_stage_2' not in self.hero.inventaire.quete.values():
                self.entities.append(Boss_Wolf('loup',(70*64,27*64),[self.graphics_sprites,self.attackable_sprites],self.obstacle_sprites,self.dmg_hero,self.hero))
        if self.lvl.lvl_number == 1:
            self.entities.append(Chest((46*64,75*64),[self.graphics_sprites,self.obstacle_sprites],self,self.hero,'green',('objet',{'katana':{'cooldown': 80, 'damage': 10, 'graphic':'../media/Armes/Armes/katana'}}),self.chest['chest_jungle'],'chest_jungle'))
        if self.lvl.lvl_number == 2:
            self.entities.append(Alex((26*64,70*64),[self.graphics_sprites],self.obstacle_sprites,False,self,self.hero))
        if self.lvl.lvl_number == 4:
            self.entities.append(Chest((15*64,39*64),[self.graphics_sprites,self.obstacle_sprites],self,self.hero,'grey',('objet',{'epee': {'cooldown': 100, 'damage': 15,'graphic':'../media/Armes/Armes/epee'}}),self.chest['chest_map_4'],'chest_map_4'))
        if self.lvl.lvl_number == 5:
            if len(self.hero.inventaire.trophee) == 0:
                self.entities.append(Boss_Golem('golem',(128*64,15*64),[self.graphics_sprites,self.attackable_sprites],self.obstacle_sprites,self.dmg_hero,self.hero))
        if self.lvl.lvl_number == 6:
            self.entities.append(Shangyu((61*64,12*64),[self.graphics_sprites],self.obstacle_sprites,False,self,self.hero))
        if self.lvl.lvl_number == 8:
            self.entities.append(Chest((22*64,76*64),[self.graphics_sprites,self.obstacle_sprites],self,self.hero,'grey',('objet',{'lance': {'cooldown': 400, 'damage': 30,'graphic':'../media/Armes/Armes/lance'}}),self.chest['chest_town'],'chest_town'))
    
    def map_change_rect(self,rect,lvl_number,x_offset = 0,y_offset = 0, hero_x = None, hero_y = None): #bloc qui permet de passer d'une map à l'autre
        if self.hero.hitbox.colliderect(rect):
            self.lvl.path_update(lvl_number)
            self.graphics_sprites.lvl = self.lvl
            self.graphics_sprites.get_floor()
            self.create_map()
            self.hero.hitbox.y += y_offset
            self.hero.hitbox.x += x_offset
            if hero_y != None:
                self.hero.hitbox.y = hero_y
            if hero_x != None:
                self.hero.hitbox.x = hero_x


    def check_map(self): #ensemble des blocs de changements de map
        if self.lvl.lvl_number == 0:
            self.map_change_rect(pygame.Rect(55 * TILESIZE+12, 28 * TILESIZE+19, 40, 25),1,y_offset = 80)
            self.map_change_rect(pygame.Rect(26 * TILESIZE+12, 75 * TILESIZE+19, 40, 25),2)
            self.map_change_rect(pygame.Rect(81 * TILESIZE+12, 25 * TILESIZE+19, 40, 25),3,x_offset = 200,hero_y = 25*TILESIZE+20)
            self.map_change_rect(pygame.Rect(91 * TILESIZE+12, 17 * TILESIZE+19, 40, 25),3,y_offset = -80)
            self.map_change_rect(pygame.Rect(116 * TILESIZE+12, 12 * TILESIZE+19, 40, 25),3,y_offset = -80)
            self.map_change_rect(pygame.Rect(26 * TILESIZE+12, 53 * TILESIZE+19, 40, 25),4,y_offset = -128)
            self.map_change_rect(pygame.Rect(134 * TILESIZE+12, 11 * TILESIZE+19, 40, 25),5,hero_x = 128*TILESIZE,hero_y = 24*TILESIZE)
            self.map_change_rect(pygame.Rect(61 * TILESIZE+12, 15 * TILESIZE, 40, 25),6,hero_x = 61*TILESIZE,hero_y = 14*TILESIZE)
            self.map_change_rect(pygame.Rect(77 * TILESIZE+12, 55 * TILESIZE, 40, 25),7,hero_x = 77*TILESIZE,hero_y = 54*TILESIZE)
            self.map_change_rect(pygame.Rect(15 * TILESIZE+12, 83 * TILESIZE, 40, 25),8,hero_x = 15*TILESIZE,hero_y = 81*TILESIZE)
            self.map_change_rect(pygame.Rect(18 * TILESIZE+12, 76 * TILESIZE, 40, 25),8,hero_x = 22*TILESIZE,hero_y = 79*TILESIZE)
        elif self.lvl.lvl_number == 1:
            self.map_change_rect(pygame.Rect(55 * TILESIZE+12, 27 * TILESIZE+19, 40, 25),0,y_offset = 80)
        elif self.lvl.lvl_number == 2:
            self.map_change_rect(pygame.Rect(26 * TILESIZE+12, 76 * TILESIZE+19, 40, 25),0,y_offset = 30)
        elif self.lvl.lvl_number == 3:
            self.map_change_rect(pygame.Rect(82 * TILESIZE+12, 25 * TILESIZE+19, 40, 25),0,x_offset = -200,hero_y = 25*TILESIZE+20)
            self.map_change_rect(pygame.Rect(91 * TILESIZE+12, 17 * TILESIZE+19, 40, 25),0,y_offset = 80)
            self.map_change_rect(pygame.Rect( 116* TILESIZE+12, 12 * TILESIZE+19, 40, 25),0,y_offset = 80)
        elif self.lvl.lvl_number == 4:
            self.map_change_rect(pygame.Rect(26 * TILESIZE+12, 52 * TILESIZE+19, 40, 25),0,y_offset = 128,hero_x = 26*TILESIZE)
        elif self.lvl.lvl_number == 5:
            self.map_change_rect(pygame.Rect(128 * TILESIZE+12, 25 * TILESIZE+19, 40, 25),0,hero_x = 134*TILESIZE,hero_y = 12*TILESIZE)
        elif self.lvl.lvl_number == 6:
             self.map_change_rect(pygame.Rect(61 * TILESIZE+12, 16 * TILESIZE, 40, 25),0,hero_x = 61*TILESIZE,hero_y = 16*TILESIZE)
        elif self.lvl.lvl_number == 7:
            self.map_change_rect(pygame.Rect(77 * TILESIZE+12, 55 * TILESIZE, 40, 25),0,hero_x = 77*TILESIZE,hero_y = 56*TILESIZE)
        elif self.lvl.lvl_number == 8:
            self.map_change_rect(pygame.Rect(15 * TILESIZE+12, 82 * TILESIZE, 40, 25),0,hero_x = 15*TILESIZE,hero_y = 84*TILESIZE)
            self.map_change_rect(pygame.Rect(22 * TILESIZE+12, 80 * TILESIZE, 40, 25),0,hero_x = 18*TILESIZE,hero_y = 77*TILESIZE)
    
    def creer_attaque(self):
        
        self.attaque_actuel = Armes(self.hero,[self.graphics_sprites,self.attack_sprites],self.hero.arme)
        
    
    def magie_attaque(self,style,mana,degats,grps):
        
        if style == 'tempest':
            self.magie_joueur.tempest(self.hero,mana,grps)
        
        if style == 'death_purple':
            self.magie_joueur.death_purple(self.hero,mana,grps)
            
            
    def detruire_arme(self):
        
        if self.attaque_actuel:
            self.attaque_actuel.kill()
            
        self.attaque_actuel = None

    def detect_attack(self):
         if self.attack_sprites:
            for atk_sprite in self.attack_sprites:
                colliding_sprites = pygame.sprite.spritecollide(atk_sprite,self.attackable_sprites,False)
                if colliding_sprites:
                    for sprite in colliding_sprites:
                        if sprite.sprite_type == 'enemy':
                            sprite.get_dmg(self.hero,atk_sprite.sprite_type)

    def dmg_hero(self,amount,atk_type):
        if not self.hero.invincible:
            self.hero.affect_health(amount)
            self.hero.invincible = True
            self.hero.hit_time = pygame.time.get_ticks()
            perte_de_vie = pygame.mixer.Sound('../media/son/pertedevie.mp3')
            perte_de_vie.play()

    def get_inventory_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_TAB]:
            time = pygame.time.get_ticks()
            if time - self.last_input_time >= self.inventory_cooldown:
                self.last_input_time = time
                self.ui.display_inventory()

    def end_game(self,event):
        self.pause = True
        if event == 'win':
            self.screen.fill('white')
            hero_surf = pygame.image.load("../media/menu/hero_saved.png").convert_alpha()
            hero_rect = hero_surf.get_rect(center = (SCREEN_HEIGHT/2,SCREEN_WIDTH/2))
            font = pygame.font.Font("../media/menu/font.ttf",100)
            win_txt = font.render("MERCI D'AVOIR JOUE", True, "black")
            win_rect = win_txt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(win_txt,win_rect)
            self.screen.blit(hero_surf,hero_rect)
        elif event == 'lose':
            self.screen.fill('black')
            font = pygame.font.Font("../media/menu/font.ttf",100)
            game_over_txt = font.render("GAME OVER", True, "red")
            game_over_rect = game_over_txt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(game_over_txt,game_over_rect)
        
        
    
    
    def run(self):
        #update+draw game
        self.check_map()
        self.graphics_sprites.get_water_frame()
        self.graphics_sprites.ft_draw(self.hero)
        self.get_inventory_input()
        self.ui.update(self.hero)
        self.graphics_sprites.update()
        self.graphics_sprites.enemy_update(self.hero)
        self.detect_attack()

class Camera_sprite(pygame.sprite.Group): #groupe qui fait en sorte que le hero soit toujours au milieu, avec les elements autour de lui
    def __init__(self,lvl):
        
        super().__init__()
        self.lvl = lvl
        self.screen = pygame.display.get_surface()
        self.half_width = self.screen.get_size()[0]//2
        self.half_height = self.screen.get_size()[1]//2
        self.offset = pygame.math.Vector2(100,200)
        self.animations = []
        self.import_water_animations()
        self.frame_index = 0
        self.animation_speed = 0.1

    def import_water_animations(self):
        self.animations = import_folder("../media/map/map_0/water")
        
    def get_floor(self):
        self.floor = pygame.image.load(self.lvl.path+'/map.png').convert_alpha()
        self.floor_rect = self.floor.get_rect(topleft = (0,0))

    def get_water_frame(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.water_frame = self.animations[int(self.frame_index)]
        self.water_rect = self.water_frame.get_rect(topleft = (0,0))

        
    def ft_draw(self,hero):
        self.offset.x = hero.rect.centerx - self.half_width
        self.offset.y = hero.rect.centery - self.half_height
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.screen.blit(self.water_frame,floor_offset_pos)
        self.screen.blit(self.floor,floor_offset_pos)
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image,offset_pos)

    def enemy_update(self,hero):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(hero)

class Map:
    def __init__(self,lvl_number):
        
        self.lvl_number = lvl_number
        self.path_update(self.lvl_number)
        self.map_entities = []

    def path_update(self,lvl):
        self.lvl_number = lvl
        self.path = '../media/map/map_'+str(self.lvl_number)
        self.entities = import_csv_layout(self.path+'/data/map_'+str(self.lvl_number)+'_entity.csv')
        self.border = import_csv_layout(self.path+'/data/map_'+str(self.lvl_number)+'_border.csv')

            
            
            
            
            