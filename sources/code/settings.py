import pygame
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60
TILESIZE = 64

enemy_stats = { 'rope': {'hp' : 60, 'atk' : 7, 'speed' : 5, 'resistance' : 3, 'atk_range' : 20, 'aggro' : 400, 'atk_type': None,'cooldown':300}, 
				'goblin': {'hp' : 100, 'atk' : 12, 'speed' : 3, 'resistance' : 1, 'atk_range' : 40, 'aggro' : 450, 'atk_type': None,'cooldown':500},
				'rose': {'hp' : 70, 'atk' : 1, 'speed' : 0, 'resistance' : 0, 'atk_range' : 100, 'aggro' : 500, 'atk_type': None,'cooldown':700},
				'slime': {'hp' : 70, 'atk' : 5, 'speed' : 1, 'resistance' : 5, 'atk_range' : 30, 'aggro' : 300, 'atk_type': None,'cooldown':500},
				'mini_golem': {'hp' : 200, 'atk' : 20, 'speed' : 1, 'resistance' : 5, 'atk_range' : 30, 'aggro' : 250, 'atk_type': None,'cooldown':700},
				'squelette': {'hp' : 120, 'atk' : 15, 'speed' : 2, 'resistance' : 5, 'atk_range' : 40, 'aggro' : 400, 'atk_type': None,'cooldown':400},
				'golem': {'hp' : 1200, 'atk' : 30, 'speed' : 1, 'resistance' : 5, 'atk_range' : 64, 'aggro' : 600, 'atk_type': None,'cooldown':1000},
				'loup': {'hp' : 700, 'atk' : 25, 'speed' : 3.5, 'resistance' : 5, 'atk_range' : 75, 'aggro' : 300, 'atk_type': None,'cooldown':600}}


magie_data = {
    'death_purple': {'degats': 30, 'mana': 30, 'cooldown': 200, 'graphic': '../media/Particules/magie/magie_stage_2'},
    'tempest': {'degats': 20, 'mana': 20, 'cooldown': 100, 'graphic': '../media/Particules/magie/magie_stage_1'}}

