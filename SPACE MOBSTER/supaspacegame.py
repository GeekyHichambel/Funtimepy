from tkinter import *
import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer 

#- - - - - - - - - - - - - - - - - -  GAME FUNCTIONS    - - - - - - - - - - - - - - - - - - - - - - - - - 

class GameScene():
	def __init__(self):
		self.scene = 'game scene'

	def main_menu(self):
		global volume
		global currentstart
		global currentcontrol		

		for event in pygame.event.get():
			screen.blit(menu_bg,(0,0))
			screen.blit(currentstart,start_rect)
			screen.blit(currentcontrol,control_rect)
			
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()		

			if event.type == pygame.KEYDOWN:             

				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

				if event.key == pygame.K_UP:
						currentstart = start_but2
						currentcontrol = control_but					

				elif event.key == pygame.K_DOWN:
					    currentstart = start_but
					    currentcontrol = control_but2
				
				if event.key == pygame.K_m:
					if volume > 0.0:
						volume = 0.0
						print('muted')
						mixer.music.set_volume(volume)

					else:
						print('unmuted')
						volume = 1.0
						mixer.music.set_volume(volume)						
				
				if event.key == pygame.K_KP_PLUS:
					if volume == 1.0:
						print('max')

					else:
						volume+=(0.1)
						volume = round(volume,1)
						print(volume)
						mixer.music.set_volume(volume)

				if event.key == pygame.K_KP_MINUS:
					if volume == 0.0:
						print('min')			

					else:
						volume-=(0.1)
						volume = round(volume,1)
						print(volume)					
						mixer.music.set_volume(volume)
		
		pygame.display.flip()
		fps.tick(60)

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
fps = pygame.time.Clock()

#attributes
screen_w=1280

screen_h=720

font = pygame.font.SysFont('Bauhaus 93 Regular',40)

pygame.display.set_caption('SPACE MOBSTER')

screen = pygame.display.set_mode((screen_w,screen_h)) 
 
game_bg = pygame.image.load("BG.jpg")

menu_bg = pygame.image.load("main_menu.jpg")

start_but = pygame.image.load("Startbut.png")

start_rect = start_but.get_rect(center = [640,400])

start_but2 = pygame.image.load("Startbut(2).png")

control_but = pygame.image.load("Controlbut.png")

control_but2 = pygame.image.load("Controlbut(2).png")

control_rect = control_but.get_rect(center = [640,600])

currentstart = start_but

currentcontrol = control_but

#sprites
object_sprites = pygame.sprite.Group()

#music
mixer.music.load('CYBERPUNK.mp3')

mixer.music.play(-1)


volume = 1.0

#objects
#- - - - - - - - - - - - - - - ROCKET - - - - - - - - - - - - - - - - - - - - - - - -
color =  (102, 153, 153)
points = [600, 700],  [640, 620], [680, 700]

# - - - - - - - - - - - - - - -Game Loop - - - - - - - - - - - - - - - - - - - - -  - - - 

working = True 

while working:
	  GameScene.main_menu()
