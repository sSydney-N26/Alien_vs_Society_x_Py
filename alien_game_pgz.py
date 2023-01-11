
import pgzrun
import random
from pgzrun import *

WIDTH = 900    # width of the window
HEIGHT = 700   # height of the window

BACKGROUND_IMG = "final_mars_background"

player = Actor('spaceship_up', midbottom=(450,600))
alien = Actor('alien_beg_sprite')
alien.pos = (random.randint(60,WIDTH-60), random.randint(120,HEIGHT-60))   #randomize alien position.
score = 0

sounds.music_upbeat.play(-1)
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

    if(player.colliderect(alien) == 1):
        sounds.alien_device.play()
        score += 1
        alien.pos = (random.randint(40,WIDTH-40), random.randint(100,HEIGHT-40))


    if(keyboard.up == 1) and (player.top > 0): # detect pressing up, down, left, right buttons
        #player.y = player.y +(-5)
        player.y +=-5
        player.image="spaceship_up"   
    
    elif(keyboard.down==1) and (player.bottom < HEIGHT):
        player.y += 5
        player.image="spaceship_down"
    elif(keyboard.left==1) and (player.left > 0):
        player.x +=-5
        player.image="spaceship_left"
    elif(keyboard.right==1) and (player.right < WIDTH):
        player.x +=5
        player.image="spaceship_right"

    elif(keyboard.w == 1) and (player.top > 0):   #detect pressing W, A, D, S as up, down, left, right.
        player.y += -5
        player.image = "spaceship_up"
    elif(keyboard.s == 1) and (player.bottom < HEIGHT):
        player.y += 5
        player.image="spaceship_down"
    elif(keyboard.a == 1) and (player.left > 0):
        player.x +=-5
        player.image="spaceship_left"
    elif(keyboard.d == 1) and (player.right < WIDTH):
        player.x +=5
        player.image="spaceship_right"
    

pgzrun.go()