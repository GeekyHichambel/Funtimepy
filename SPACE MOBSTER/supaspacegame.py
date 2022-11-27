from tkinter import *
import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer 

#- - - - - - - - - - - - - - - - - -  GAME SCENES   - - - - - - - - - - - - - - - - - - - - - - - - - 
class GameScene():
	def __init__(self):
		self.scene = 'game scene'

	def main_menu(self):
		global volume

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.KEYDOWN:             

				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

				if event.key == pygame.K_m:
					if volume:
						mixer.music.set_volume(0.0)
						volume = False

					else:
						mixer.music.set_volume(1.0)
						volume = True

		
		screen.blit(menu_bg,(0,0))
		screen.blit(start_but,(screen_w/2-210,screen_h/2-150))
		screen.blit(control_but,(screen_w/2-210,screen_h/2+80))

		pygame.display.flip()

	def main_game(self):	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.KEYDOWN:             

				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()     	
		
		screen.blit(bg,(0,0))
		pygame.display.flip()


#initializtion
pygame.init()
pygame.font.init()
GameScene = GameScene()

#attributes
screen_w=1280

screen_h=720

font = pygame.font.SysFont('Bauhaus 93 Regular',40)

pygame.display.set_caption('SPACE MOBSTER')

screen = pygame.display.set_mode((screen_w,screen_h)) 
 
game_bg = pygame.image.load("BG.jpg")

menu_bg = pygame.image.load("main_menu.jpg")

start_but = pygame.image.load("Startbut.png")

control_but = pygame.image.load("Controlbut.png")

#music
mixer.music.load('CYBERPUNK.mp3')

mixer.music.play(-1)

volume = True

#objects
#- - - - - - - - - - - - - - - ROCKET - - - - - - - - - - - - - - - - - - - - - - - -
color =  (102, 153, 153)
points = [600, 700],  [640, 620], [680, 700]

# - - - - - - - - - - - - - - -Game Loop - - - - - - - - - - - - - - - - - - - - -  - - - 

working = True 

while working:
	  GameScene.main_menu()