from tkinter import *
import pygame
import sys
import random
from pygame.locals import *
from pygame import mixer

#-------------  CLASSES ----------#
class buttons():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.pressed = False

    def place(self):
        click = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                click = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.pressed = False                

        screen.blit(self.image,(self.rect.x,self.rect.y))

        return click

class score():
    def show_pscore(self, x, y):
        global player_score
        self.player_score_txt = font.render("PLAYER : "+str(player_score),True,(255,255,255))
        screen.blit(self.player_score_txt,(x,y))

    def show_cscore(self, x, y):
        global computer_score
        self.computer_score_txt = font.render("COMPUTER : "+str(computer_score),True,(255,255,255))
        screen.blit(self.computer_score_txt,(x,y))

#------------- Initialization ----------#

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial',32)
fps = pygame.time.Clock()
Score = score()
T_K = Tk() 

#-------------  ATTRIBUTES ----------#

screen_width = 600
screen_height = 600
pygame.display.set_caption('S.P.S')
screen = pygame.display.set_mode((screen_width,screen_height))

#------------- RESOURCES ----------#

bg = pygame.image.load("bg.png")
stone = pygame.image.load("stone_butt.png")
scissor = pygame.image.load("scissor_butt.png")
paper = pygame.image.load("paper_butt.png")

#-------------  MUSIC ----------#
stone_sound = pygame.mixer.Sound('stone.mp3')
paper_sound = pygame.mixer.Sound('paper.mp3')
scissor_sound = pygame.mixer.Sound('scissor.mp3')
stone_sound.set_volume(0.1)
paper_sound.set_volume(0.1)
scissor_sound.set_volume(0.1)

#------------- DATA ----------#

choices = ["Stone", "Paper", "Scissor"]
player = ""
computer_score = 0
player_score = 0

#------------- BUTTONS ----------#

stone_button = buttons(100,280,stone)
scissor_button = buttons(240,280,scissor)
paper_button = buttons(380,280,paper)

#-------------  TEXT ----------#

choice_txt = font.render('YOUR CHOICE',True,(255,255,255))

#-------------  MAIN LOOP ----------#

working = True

while working:   

    screen.fill('black')
        
    for event in pygame.event.get():            
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            pygame.quit()
            sys.exit()  

    screen.blit(bg,(0,0))
    screen.blit(choice_txt,(200,200))
    
    if stone_button.place():
        computer = random.choice(choices)
        print('The computer choses: '+computer)
        player = "Stone"
        if computer == player:
            stone_sound.play()
            print('The rocks collide hence a tie')
        elif computer == "Scissor":
            stone_sound.play()
            print('Hard hit of stone makes the scissor break hence u win')
            player_score+=1
        elif computer == "Paper":
            paper_sound.play()
            print('Oops! The rock got caught by the paper hence u lose')
            computer_score+=1 

    if scissor_button.place():
        computer = random.choice(choices)
        print('The computer choses: '+computer)
        player = "Scissor"
        if computer == player:
            scissor_sound.play()
            print('Oops! The scissors got stuck hence a tie')
        elif computer == "Stone":
            stone_sound.play()
            print('Scissor got rammed by the stone hence u lose')
            computer_score+=1
        elif computer == "Paper":
            scissor_sound.play()
            print('You cut the paper into pieces hence u win')
            player_score+=1

    if paper_button.place():
        computer = random.choice(choices)
        print('The computer choses: '+computer)
        player = "Paper"
        if computer == player:
            paper_sound.play()
            print('Two lame papers cannot do much hence a tie')
        elif computer == "Scissor":
            scissor_sound.play()
            print('Paper got torn in halves hence u lose')
            computer_score+=1
        elif computer == "Stone":
            paper_sound.play()
            print('You trapped the stone like a bait hence u win')
            player_score+=1
    
    Score.show_pscore(50,530)
    Score.show_cscore(320,530)
    pygame.display.update()
    fps.tick(60)
