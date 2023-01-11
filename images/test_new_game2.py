# Alien Pygame

import pygame
import sys
from pygame import mixer
import random

WIDTH = 900    # width of the window
HEIGHT = 700   # height of the window

BACKGROUND_IMG = "final_mars_background.png"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = pygame.image.load("spaceship_up.png")
alien = pygame.image.load("alien_beg_sprite.png")
score = 0

# Setting Game Music:

mixer.init()
mixer.music.load("music_upbeat.wav")
mixer.music.set_volume(0.7)
mixer.music.play()

# sounds.music_upbeat.play(-1)
# DRAW SCREEN
def draw():

 screen.clear()
 screen.blit(BACKGROUND_IMG, (0,0))
 player.draw()
 alien.draw()

 show_score = str(score)
 screen.draw.text(show_score, fontsize=65, topright = (760,35), color="white")

def update():
    global score
    player_x = 450
    player_y = 600 
    alien_x = random.randint(60,WIDTH-60)
    alien_y = random.randint(120,HEIGHT-60)  
    screen.blit(alien, (alien_x, alien_y))

    if(player.colliderect(alien) == 1):
        music = mixer.music.load("alien_device.wav")
        mixer.music.play(music)
        score += 1
        screen.blit(alien, (random.randint(40,WIDTH-40), random.randint(100,HEIGHT-40)))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP) and (player.top > 0): # detect pressing up, down, left, right buttons
                #player.y = player.y +(-5)
                player_y +=-5
                player = pygame.image.load("spaceship_up.png")
                screen.blit(player, (player_x, player_y))
            
            elif(event.key == pygame.K_DOWN) and (player.bottom < HEIGHT):
                player_y += 5
                player = pygame.image.load("spaceship_down.png")
                screen.blit(player, (player_x, player_y))
            elif(event.key == pygame.K_LEFT) and (player.left > 0):
                player_x +=-5
                player = pygame.image.load("spaceship_left.png")
                screen.blit(player, (player_x, player_y))
            elif(event.key == pygame.K_RIGHT) and (player.right < WIDTH):
                player_x +=5
                player = pygame.image.load("spaceship_right.png")
                screen.blit(player, (player_x, player_y))

            elif(event.key == pygame.K_w) and (player.top > 0):   #detect pressing W, A, D, S as up, down, left, right.
                player.y += -5
                player = pygame.image.load("spaceship_up.png") 
            elif(event.key == pygame.K_s) and (player.bottom < HEIGHT):
                player_y += 5
                player = pygame.image.load("spaceship_down.png")
                screen.blit(player, (player_x, player_y))
            elif(event.key == pygame.K_a) and (player.left > 0):
                player_x +=-5
                player = pygame.image.load("spaceship_left.png")
                screen.blit(player, (player_x, player_y))
            elif(event.key == pygame.K_d) and (player.right < WIDTH):
                player_x +=5
                player = pygame.image.load("spaceship_right.png")
                screen.blit(player, (player_x, player_y))
        pygame.display.update()
            

update()
