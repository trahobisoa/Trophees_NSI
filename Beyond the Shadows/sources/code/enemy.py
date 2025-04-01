import pygame
from settings import *
from entity import Entity
from import_tool import *

class Enemy(Entity):
	def __init__(self,name,pos,groups,obstacle_sprites,dmg_hero):
		super().__init__(groups)
		self.sprite_type = 'enemy'
		self.enemy = name

		#stats

		self.data = enemy_stats.get(self.enemy)
		self.hp = self.data.get('hp')
		self.atk = self.data.get('atk')
		self.atk_type = self.data.get('atk_type')
		self.speed = self.data.get('speed')
		self.resistance = self.data.get('resistance')
		self.range = self.data.get('atk_range')
		self.aggro = self.data.get('aggro')
		self.import_monstre_atout()
		self.orientation = 'avant_'
		self.status = 'idle'
		self.image = self.animations['avant_'+self.status][self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)
		self.dmg_hero = dmg_hero
		self.hitbox = self.rect.inflate(0,-10)
		self.obstacle_sprites = obstacle_sprites
		self.peut_atk = True
		self.atk_time = None
		self.atk_cooldown = self.data.get('cooldown')
		self.invincible = False
		self.hit_time = None
		self.hit_cooldown = 600


	def import_monstre_atout(self):
		enemy_path = '../media/monsters/' +self.enemy+'/' #complete with folder with animations
		self.animations = {'avant_mouvement': [], 'arriere_mouvement': [],'gauche_mouvement': [], 'droite_mouvement': [],'avant_idle': [], 'arriere_idle': [], 'gauche_idle': [],'droite_idle': []
		, 'avant_attaque': [''], 'arriere_attaque': [''],'gauche_attaque': [''], 'droite_attaque': ['']}
		for animation in self.animations.keys():
			full_path = enemy_path + animation
			self.animations[animation] = import_folder(full_path)


	def get_hero_direction(self,hero):
		enemy_vec = pygame.math.Vector2(self.rect.center)
		hero_vec = pygame.math.Vector2(hero.rect.center)
		distance = (hero_vec-enemy_vec).magnitude()
		if distance >0:
			direction = (hero_vec - enemy_vec).normalize()
		else:
			direction = pygame.math.Vector2()
		return (distance,direction)

	def get_status(self,hero):
		distance = self.get_hero_direction(hero)[0]
		if distance <= self.range and self.peut_atk:
			if self.status != 'attaque':
				self.frame_index = 0
			self.status = 'attaque'
		elif distance <= self.aggro:
			self.status = 'mouvement'
		else:
			self.status = 'idle'

	def behavior(self,hero):
		if self.status == 'attaque':
			self.atk_time = pygame.time.get_ticks()
			self.dmg_hero(-self.atk,self.atk_type)
		elif self.status == 'mouvement':
			self.direction = self.get_hero_direction(hero)[1]
		else:
			self.direction = pygame.math.Vector2()
		sx,sy = self.hitbox.centerx,self.hitbox.centery
		hx,hy = hero.hitbox.centerx,hero.hitbox.centery
		if abs(hx-sx) < 150 and abs(hy-sy) > 100 and sy > hy:
			self.orientation = 'arriere_'
		elif abs(hx-sx) < 150 and abs(hy-sy) > 100 and sy < hy:
			self.orientation = 'avant_'
		elif sx > hx:
			self.orientation = 'gauche_'
		elif sx < hx:
			self.orientation = 'droite_'

	def recharge(self):
		time = pygame.time.get_ticks()
		if not self.peut_atk:
			if time - self.atk_time >= self.atk_cooldown:
				self.peut_atk = True
		if self.invincible:
			if time - self.hit_time >= self.hit_cooldown:
				self.invincible = False


	def get_dmg(self,hero,atk_type):
		if self.invincible == False:
			self.direction = self.get_hero_direction(hero)[1]
			if atk_type == 'arme':
				self.hp -= hero.get_weapon_dmg()
			elif atk_type == 'magie':
				self.hp -= hero.get_magie_dmg()
		self.hit_time = pygame.time.get_ticks()
		self.invincible = True

	def check_death(self):
		if self.hp <= 0:
			self.kill()

	def on_hit(self):
		if self.invincible:
			self.direction *= -self.resistance


	def animer(self):
		animation = self.animations[self.orientation+self.status]
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			if self.status == 'attaque':
				self.peut_atk = False
			self.frame_index = 0 
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

		if self.invincible:
			alpha = self.flicker()
			self.image.set_alpha(alpha)
		else:
			self.image.set_alpha(255)

	def update(self):
		self.on_hit()
		self.move(self.speed)
		self.animer()
		self.recharge()
		self.check_death()

	def enemy_update(self,hero):
		self.get_status(hero)
		self.behavior(hero)