import pygame
import time
from settings import *
from import_tool import import_folder
from entity import Entity

class NPC(Entity):
    def __init__(self,grp):
        super().__init__(grp)
        self.last_input_time = 0
        self.cooldown = 400


    def import_npc_atout(self,name):
        
        caractere_path = '../media/npc/'+name+'/'  #complete with folder with animations
        
        self.animations = {'avant_mouvement': [''], 'arriere_mouvement': [''],'gauche_mouvement': [''], 'droite_mouvement': [],'avant_idle': [''], 'arriere_idle': [''], 'gauche_idle': [''],'droite_idle': ['']}
        for animation in self.animations.keys():
            full_path = caractere_path + animation
            self.animations[animation] = import_folder(full_path)

    def animer(self):
        
        animations = self.animations[self.orientation+self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animations):
            self.frame_index = 0
                        
        self.image = animations[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def get_hero_distance(self):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        hero_vec = pygame.math.Vector2(self.hero.rect.center)
        distance = (hero_vec-enemy_vec).magnitude()
        return distance

    def get_status(self):
        distance = self.get_hero_distance()
        sx,sy = self.hitbox.centerx,self.hitbox.centery
        hx,hy = self.hero.hitbox.centerx,self.hero.hitbox.centery
        if hy < sy and abs(hx-sx)<80:
            self.orientation = 'arriere_'
        if hy > sy and abs(hx-sx)<70:
            self.orientation = 'avant_'
        elif abs(hy-sy) < 60 and abs(hx-sx) < 200:
            if hx > sx:
                self.orientation = 'droite_'
            else:
                self.orientation = 'gauche_'
        else:
            self.orientation = 'avant_'
        if self.move == True:
            self.wander()
        else:
            if distance <= 100:
                self.status = 'idle'
                self.get_input()
    
    def wander(self):
        if distance <= 100:
            self.status = 'idle'
            self.get_input()
        self.status = 'mouvement'

        
    def get_input(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_e]:
                time = pygame.time.get_ticks()
                if time - self.last_input_time >= self.cooldown:
                    self.last_input_time = time
                    son_texte = pygame.mixer.Sound('../media/son/texte_dialogue.mp3')
                    son_texte.play()
                    if self.talking == True:
                        self.talking = False
                    else:
                        self.behavior()



    def update(self):
        self.get_status()
        self.text.update()
        self.animer()


class Text:
    def __init__(self,text,npc,display_name = True):
        self.screen = pygame.display.get_surface()
        self.txt = text
        self.font = pygame.font.Font('../media/font/pixel_font.ttf', 20)
        self.name_font = pygame.font.Font('../media/font/pixel_font.ttf', 30)
        self.x = 1/20*SCREEN_WIDTH
        self.y= 19/20*SCREEN_HEIGHT -150
        self.show_text = False
        self.npc = npc
        self.name = self.name_font.render(self.npc.__class__.__name__, True, (255,255,255))
        self.display_name = display_name
        

    def text_box(self):
        main_rect = pygame.Rect(self.x,self.y,18/20*SCREEN_WIDTH,125)
        self.rect = main_rect.copy()
        pygame.draw.rect(self.screen, (0,0,0), main_rect, 0)
        for i in range(4):
            border = pygame.Rect(self.x-i,self.y-i,18/20*SCREEN_WIDTH,125)
            pygame.draw.rect(self.screen, (255,255,255),border, 3)
            self.rect = self.rect.union(border)

    def text(self):
        text = self.font.render(self.txt, True, (255,255,255))
        return text

    def display_text(self):
        if self.show_text == True:
            self.text_box()
            text = self.text()
            self.screen.blit(text,(self.x+30,self.y+20))
            if self.display_name == True:
                self.screen.blit(self.name,(self.x+10,self.y-50))

    def get_show_text(self):
        self.show_text = self.npc.talking
        if self.npc.get_hero_distance() > 100:
            self.show_text = False
            self.npc.talking = False

    def update(self):
        self.get_show_text()
        self.display_text()


        
#all NPC classes:

class Jean(NPC):
    def __init__(self,pos,groups,obs_sprite,mov,lvl,hero):
        super().__init__(groups)
        self.image = pygame.image.load("../media/npc/Jean/avant_idle/2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.import_npc_atout('Jean')
        self.speed = 5
        self.obstacle_sprites = obs_sprite
        self.move = mov
        self.status = 'idle'
        self.inventory = []
        self.lvl = lvl
        self.hero = hero
        self.orientation = 'avant_'
        self.talking = False
        self.dialogue = ["Pauvre phantome ou est donc ton corps?","Une certaine personne pourrait peut-être t'aider...","Rend visite au mage Liam quand tu auras le temps"]
        self.dialogue2 = ["A l'est d'ici tu trouveras un labyrinthe.","Il contient un trésor, mais est infesté de monstres..."]
        self.dialogue_index1 = 0
        self.dialogue_index2 = 0
        self.text = Text('None',self)


    def behavior(self):
        self.talking = True
        if self.dialogue_index1 < len(self.dialogue):
            self.text = Text(self.dialogue[self.dialogue_index1],self)
            self.dialogue_index1+=1
            self.text.update()
        else:
            self.text = Text(self.dialogue2[self.dialogue_index2],self)
            self.text.update()
            self.dialogue_index2+=1
            if self.dialogue_index2>len(self.dialogue2)-1:
                self.dialogue_index2 = 0

class Hugo(NPC):
    def __init__(self,pos,groups,obs_sprite,mov,lvl,hero):
        super().__init__(groups)
        self.image = pygame.image.load("../media/npc/Hugo/avant_idle/2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.import_npc_atout('Hugo')
        self.speed = 5
        self.obstacle_sprites = obs_sprite
        self.move = mov
        self.status = 'idle'
        self.inventory = []
        self.lvl = lvl
        self.hero = hero
        self.orientation = 'avant_'
        self.talking = False
        self.dialogue = ["J'ai renforce toutes tes armes.","Reviens me voir quand tu auras plus d'armes","j'ai renforce tes armes au maximum."]
        self.dialogue2 = "Si tu tue le Loup qui vit dans les bois au nord, j'ameliorerais ton equipement une deuxieme fois"
        self.dialogue3 = "Si tu m'apporte le tresor du labyrinthe, j'ameliorerais ton equipement"
        self.dialogue4 = ["N'attire pas de monstres dans le village!","...","J'ai entendu des bruits etranges qui viennent des montagnes","...","Ne me derange pas pendant que je travaille"]
        self.dialogue_index = 0
        self.text = Text('None',self)

    def behavior(self):
        self.talking = True
        if self.hero.stage == '1':
            if 'materiaux_stage_1' in self.hero.inventaire.quete.values():
                if len(self.hero.inventaire.objet) != 3:
                    self.text = Text(self.dialogue[1],self)
                else:
                    self.hero.stage = '2'
                    self.text = Text(self.dialogue[0],self)
                    self.hero.inventaire.quete.pop('materiaux')
                self.text.update()
            else:
                self.text = Text(self.dialogue3,self)
        elif self.hero.stage == '2':
            if 'materiaux_stage_2' in self.hero.inventaire.quete.values():
                self.text = Text(self.dialogue[2],self)
                self.hero.stage = '3'
                self.hero.inventaire.quete.pop('materiaux')
            else:
                self.text = Text(self.dialogue2,self)
            self.text.update()
        else:
            self.text = Text(self.dialogue4[self.dialogue_index],self)
            self.text.update()
            self.dialogue_index+=1
            if self.dialogue_index>len(self.dialogue2)-1:
                self.dialogue_index = 0

            
class Alex(NPC):
    def __init__(self,pos,groups,obs_sprite,mov,lvl,hero):
        super().__init__(groups)
        self.image = pygame.image.load("../media/npc/Alex/avant_idle/2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.import_npc_atout('Alex')
        self.speed = 5
        self.obstacle_sprites = obs_sprite
        self.move = mov
        self.status = 'idle'
        self.inventory = []
        self.lvl = lvl
        self.hero = hero
        self.orientation = 'avant_'
        self.talking = False
        self.dialogue = ["splish, splash, splish, splash","plip, plop, plip, plop"]
        self.dialogue_index = 0
        self.text = Text('None',self)

    def behavior(self):
        self.talking = True
        self.text = Text(self.dialogue[self.dialogue_index],self)
        self.text.update()
        self.dialogue_index+=1
        if self.dialogue_index>len(self.dialogue)-1:
            self.dialogue_index = 0
        if self.hero.vie < self.hero.vie_max:
            self.hero.vie = self.hero.vie_max

class Rahobisoa(NPC):
    def __init__(self,pos,groups,obs_sprite,mov,lvl,hero):
        super().__init__(groups)
        self.image = pygame.image.load("../media/npc/Mr.Rahobisoa/avant_idle/1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.import_npc_atout('Mr.Rahobisoa')
        self.speed = 5
        self.obstacle_sprites = obs_sprite
        self.move = mov
        self.status = 'idle'
        self.inventory = []
        self.lvl = lvl
        self.hero = hero
        self.orientation = 'avant_'
        self.talking = False
        self.dialogue = ["Viens me voir quand tu commence à manquer d'énergie","C'est toujours un plaisir d'aider une âme en peine"]
        self.dialogue_index = 0
        self.text = Text('None',self)

    def behavior(self):
        self.talking = True
        self.text = Text(self.dialogue[self.dialogue_index],self)
        self.text.update()
        self.dialogue_index+=1
        if self.dialogue_index>len(self.dialogue)-1:
            self.dialogue_index = 0
        if self.hero.vie < self.hero.vie_max:
            self.hero.vie = self.hero.vie_max


class Liam(NPC):
    def __init__(self,pos,groups,obs_sprite,mov,lvl,hero):
        super().__init__(groups)
        self.image = pygame.image.load("../media/npc/Liam/avant_idle/2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.import_npc_atout('Liam')
        self.speed = 5
        self.obstacle_sprites = obs_sprite
        self.move = mov
        self.status = 'idle'
        self.inventory = []
        self.lvl = lvl
        self.hero = hero
        self.orientation = 'avant_'
        self.talking = False
        self.dialogue = ["Malheureusement, je ne peux pas te rendre ton corps.",
                         "Je peux cependant te rendre plus puissant.",
                         "..."]
        self.dialogue2 = "Pas besoin de me remercier."
        self.dialogue3 = ["J'ai entendu parler d'un mage qui pourrait peut etre t'aider","Il vit dans l'un des grands arbres de cette forêt.","Il pourra surement t'aider"]
        self.dialogue_index = 0
        self.dialogue_index3 = 0
        self.text = Text('None',self)

    def behavior(self):
        self.talking = True
        if self.hero.vie_max == 100 and self.dialogue_index < len(self.dialogue):
            self.text = Text(self.dialogue[self.dialogue_index],self)
            self.dialogue_index+=1
        elif self.hero.vie_max == 100:
            self.text = Text(self.dialogue2,self)
            self.hero.vie_max += 20
            self.hero.affect_health(20)
            self.hero.energie_max += 20
        else:
            self.text = Text(self.dialogue3[self.dialogue_index3],self)
            self.dialogue_index3+=1
            if self.dialogue_index3>len(self.dialogue)-1:
                self.dialogue_index3 = 0
        self.text.update()
        

class Shangyu(NPC):
    def __init__(self,pos,groups,obs_sprite,mov,lvl,hero):
        super().__init__(groups)
        self.image = pygame.image.load("../media/npc/Shangyu/avant_idle/2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.import_npc_atout('Shangyu')
        self.speed = 5
        self.obstacle_sprites = obs_sprite
        self.move = mov
        self.status = 'idle'
        self.inventory = []
        self.lvl = lvl
        self.hero = hero
        self.orientation = 'avant_'
        self.talking = False
        self.dialogue = "Tu est faible. Reviens me voir quand tu seras plus fort."
        self.dialogue0 = ["Je vois que tu est suffisament puissant pour m'etre utile."]
        self.dialogue1 = ["Va au plus profond des montagnes","ramene moi le crystal du Golem.","Si tu tiens a retrouver ton corps, bien sur.","Si tu remplis ta mission, je ramenerais ton corps a la vie."]
        self.dialogue2 = ["Tu as donc reussi a obtenir le crystal","...","Comme promis, je vais maintenant ramener ton corps d'entre les morts.","...","3","...","2","...","1","..."]
        self.dialogue_index0 = 0
        self.dialogue_index1 = 0
        self.dialogue_index2 = 0
        self.text = Text('None',self)

    def behavior(self):
        self.talking = True
        if self.hero.stage == '1':
            self.text = Text(self.dialogue,self)
            self.text.update()
        elif 'golem_crystal.png' not in self.hero.inventaire.trophee.values():
            if self.dialogue_index0 < len(self.dialogue0):
                self.text = Text(self.dialogue0[0],self)
                self.dialogue_index0 += 1
            else:
                self.text = Text(self.dialogue1[self.dialogue_index1],self)
                self.dialogue_index1+=1
                if self.dialogue_index1>len(self.dialogue1)-1:
                    self.dialogue_index1 = 0
            self.text.update()
        else:
            if self.dialogue_index2>=len(self.dialogue2):
                self.talking = False
                self.lvl.end_game('win')
            else:
                self.text = Text(self.dialogue2[self.dialogue_index2],self)
                self.text.update()
                self.dialogue_index2+=1
        
        
class Chest(NPC):
    def __init__(self,pos,groups,lvl,hero,type,item,status,name):
        super().__init__(groups)
        self.image = pygame.image.load("../media/objects/chests/"+type+"/1.png")
        self.image_index = 0
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-30)
        self.import_animation(type)
        self.status = status
        self.item = item #tuple (item_type,item)
        self.hero = hero
        self.animation_speed = 0.25
        self.lvl = lvl
        self.info = "Vous obtenez "
        self.talking = False
        self.name = name

    def import_animation(self,type):
        full_path = '../media/objects/chests/'+type+'/'
        self.animations = import_folder(full_path)

    def get_hero_distance(self):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        hero_vec = pygame.math.Vector2(self.hero.rect.center)
        distance = (hero_vec-enemy_vec).magnitude()
        return distance

    def get_status(self):
        distance = self.get_hero_distance()
        if distance <= 100:
            self.get_input()

    def get_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_e]:
            if self.status == 'closed':
                self.behavior()

    def animate(self):
        if self.status == 'open':
            if self.image_index != 3:
                self.image_index += self.animation_speed
                self.image = self.animations[int(self.image_index)]
                self.talking = True
            self.text = Text(self.info+list(self.item[1].keys())[0],self,False)
            self.text.update()

    def behavior(self):
        self.lvl.chest[self.name] = 'open'
        item_type = self.item[0]
        if item_type == 'objet':
            self.hero.inventaire.objet.update(self.item[1])
        if item_type == 'quete':
            self.hero.inventaire.quete.update(self.item[1])
        self.status = 'open'

    def update(self):
        self.get_status()
        self.animate()

