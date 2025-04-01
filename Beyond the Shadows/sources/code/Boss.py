import pygame
from import_tool import import_folder
from settings import *
from entity import Entity
from enemy import Enemy

class Boss_Golem(Enemy):
	def __init__(self,name,pos,groups,obstacle_sprites,dmg_hero,hero):
		super().__init__(name,pos,groups,obstacle_sprites,dmg_hero)
		self.animation_speed = 0.05
		self.hero = hero

	def get_dmg(self,hero,atk_type): #methode specifique pour les resistances et faiblesses du golem
		if self.invincible == False:
			self.direction = self.get_hero_direction(hero)[1]
			if atk_type == 'arme':
				self.hp -= 1/2*hero.get_weapon_dmg()
			elif atk_type == 'magie':
				self.hp -= 3/2*hero.get_magie_dmg()
		self.hit_time = pygame.time.get_ticks()
		self.invincible = True

	def on_hit(self): #boss trop lourd pour subir du knockback
		pass

	def check_death(self):
		if self.hp <= 0:
			self.kill()
			self.hero.inventaire.trophee['golem'] = 'golem_crystal.png'
			print(self.hero.inventaire.trophee)

class Boss_Wolf(Enemy):
	def __init__(self,name,pos,groups,obstacle_sprites,dmg_hero,hero):
		super().__init__(name,pos,groups,obstacle_sprites,dmg_hero)
		self.hero = hero

	def get_dmg(self,hero,atk_type): #methode specifique pour les resistances et faiblesses du loup
		if self.invincible == False:
			self.direction = self.get_hero_direction(hero)[1]
			if atk_type == 'arme':
				self.hp -= hero.get_weapon_dmg()
			elif atk_type == 'magie':
				self.hp -= 1/2*hero.get_magie_dmg()
		self.hit_time = pygame.time.get_ticks()
		self.invincible = True

	def check_death(self):
		if self.hp <= 0:
			self.kill()
			self.hero.inventaire.quete['materiaux'] = 'materiaux_stage_2'
