import pygame, sys
from button import Button
from Game import Game
from settings import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Beyond The Shadows")

BG = pygame.image.load("../media/menu/background.FAIT.png")
game = Game()
#musique/sons
musique = pygame.mixer.music.load('../media/son/jeu_musique.mp3')
pygame.mixer.music.play(-1)

def get_font(size,font): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(font, size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        if __name__ == '__main__':
            game.run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def instructions():
    while True:
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        INSTRUCTIONS_IMG = pygame.image.load("../media/menu/How to play.png")
        INSTRUCTIONS_RECT = INSTRUCTIONS_IMG.get_rect(center=(SCREEN_WIDTH/2, 320))
        SCREEN.blit(INSTRUCTIONS_IMG, INSTRUCTIONS_RECT)

        INSTRUCTIONS_BACK = Button(image=None, pos=(SCREEN_WIDTH/2, 600), 
                            text_input="RETOUR", font=get_font(75,"../media/menu/font.ttf"), base_color="Black", hovering_color="Green")

        INSTRUCTIONS_BACK.changeColor(INSTRUCTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40,"../media/font/ravie.ttf").render("Beyond the Shadows", True, "#52A736")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH/2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../media/menu/Play Rect.png"), pos=(SCREEN_WIDTH/2, 250), 
                            text_input="JOUER", font=get_font(75,"../media/menu/font.ttf"), base_color="#d7fcd4", hovering_color="White")
        INSTRUCTIONS_BUTTON = Button(image=pygame.image.load("../media/menu/Options Rect.png"), pos=(SCREEN_WIDTH/2, 400), 
                            text_input="TOUCHES", font=get_font(75,"../media/menu/font.ttf"), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../media/menu/Quit Rect.png"), pos=(SCREEN_WIDTH/2, 550), 
                            text_input="QUITTER", font=get_font(50,"../media/menu/font.ttf"), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()