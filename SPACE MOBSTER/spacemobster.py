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
		global window
		global switch

		screen.blit(menu_bg,(0,0))
		screen.blit(currentstart,start_rect) 
		screen.blit(currentcontrol,control_rect)	

		for event in pygame.event.get():			
			
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()		

			if event.type == pygame.KEYDOWN:             

				if event.key == pygame.K_ESCAPE:
					switch_sfx.play()
					pygame.time.delay(400)
					pygame.quit()
					sys.exit()

				if event.key == pygame.K_RETURN:
					if window == 2:
						switch_sfx.play()
						switch = window
						break


					elif window == 3:
						switch_sfx.play()
						switch = window
						break

				if event.key == pygame.K_UP:
					    select_sfx.play()
					    currentstart = start_but2
					    currentcontrol = control_but
					    window = 2
					    							

				elif event.key == pygame.K_DOWN:
						select_sfx.play()
						currentstart = start_but
						currentcontrol = control_but2
						window = 3
						

				if event.key == pygame.K_m:
					if volume > 0.0:
						volume = 0.0
						print('muted')
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)

					else:
						print('unmuted')
						volume = 1.0
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)						
				
				if event.key == pygame.K_KP_PLUS:
					if volume == 1.0:
						print('max')

					else:
						volume+=(0.1)
						volume = round(volume,1)
						print(volume)
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)

				if event.key == pygame.K_KP_MINUS:
					if volume == 0.0:
						print('min')			

					else:
						volume-=(0.1)
						volume = round(volume,1)
						print(volume)					
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)
		
		pygame.display.flip()
		fps.tick(60)

	def main_game(self):
		global switch
		global volume
		global moving_left
		global moving_right
		global x_axis
		global y_axis

		screen.fill('black')

		for event in pygame.event.get():
		   		
		   	if event.type == pygame.QUIT:
		   		pygame.quit()
		   		sys.exit()

		   	if event.type == pygame.KEYDOWN:

		   		if event.key == pygame.K_ESCAPE:
		   			switch_sfx.play()
		   			switch = 1
		   			break

		   		if event.key == pygame.K_a:
		   			moving_left = True 
		   				
		   		if event.key == pygame.K_d:
		   			moving_right = True	   					

		   		if event.key == pygame.K_m:
		   			if volume > 0.0:
		   				volume = 0.0
		   				print('muted')
		   				mixer.music.set_volume(volume)
		   				select_sfx.set_volume(volume)
		   				switch_sfx.set_volume(volume)

		   			else:
		   				print('unmuted')
		   				volume = 1.0
		   				mixer.music.set_volume(volume)
		   				select_sfx.set_volume(volume)
		   				switch_sfx.set_volume(volume)						

		   		if event.key == pygame.K_KP_PLUS:
		   			if volume == 1.0:
		   				print('max')

		   			else:
		   				volume+=(0.1)
		   				volume = round(volume,1)
		   				print(volume)
		   				mixer.music.set_volume(volume)
		   				select_sfx.set_volume(volume)
		   				switch_sfx.set_volume(volume)

		   		if event.key == pygame.K_KP_MINUS:
		   			if volume == 0.0:
		   				print('min')

		   			else:
		   				volume-=(0.1)
		   				volume = round(volume,1)
		   				print(volume)					
		   				mixer.music.set_volume(volume)
		   				select_sfx.set_volume(volume)
		   				switch_sfx.set_volume(volume)

		   	elif event.type == pygame.KEYUP:

		   		if event.key == pygame.K_a:
		   			moving_left = False

		   		if event.key == pygame.K_d:
		   			moving_right = False

		if(moving_left) and x_axis>0:
	   		x_axis-=12

		elif(moving_right) and x_axis<1130:
	   		x_axis+=12	
		
		screen.blit(game_bg,(0,0))
		screen.blit(rocket,(x_axis,y_axis))
		pygame.display.update()
		fps.tick(60)

	def control_window(self):
		global switch
		global volume

		screen.fill('black')	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.KEYDOWN:             

				if event.key == pygame.K_ESCAPE:
					switch_sfx.play()
					switch = 1
					break

				if event.key == pygame.K_m:
					if volume > 0.0:
						volume = 0.0
						print('muted')
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)

					else:
						print('unmuted')
						volume = 1.0
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)						
				
				if event.key == pygame.K_KP_PLUS:
					if volume == 1.0:
						print('max')

					else:
						volume+=(0.1)
						volume = round(volume,1)
						print(volume)
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)

				if event.key == pygame.K_KP_MINUS:
					if volume == 0.0:
						print('min')			

					else:
						volume-=(0.1)
						volume = round(volume,1)
						print(volume)					
						mixer.music.set_volume(volume)
						select_sfx.set_volume(volume)
						switch_sfx.set_volume(volume)

		screen.blit(control_menu,(0,0))
		pygame.display.update()
		pygame.display.flip()
		fps.tick(60)     					


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

control_menu = pygame.image.load("controlpage.jpg")

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

select_sfx = pygame.mixer.Sound('selector.mp3')

switch_sfx = pygame.mixer.Sound('switch__.wav')

volume = 1.0

window = 1

#objects
#- - - - - - - - - - - - - - - ROCKET - - - - - - - - - - - - - - - - - - - - - - - -
rocket = pygame.image.load("rocket.png")

x_axis = 590

y_axis = 570

# - - - - - - - - - - - - - - -Game Loop - - - - - - - - - - - - - - - - - - - - -  - - - 

switch = 1

working = True

moving_left = False 

moving_right = False

while working:

	if switch == 1:
		GameScene.main_menu()

	elif switch == 2:	
		GameScene.main_game()

	elif switch == 3:
		GameScene.control_window()	
