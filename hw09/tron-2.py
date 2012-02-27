#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *
from pygame import draw

#initialize pygame
pygame.init()

#Colors used in game

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

#draw screen
screen = pygame.display.set_mode((600,600))
screen.fill(BLACK)
screen_bounds = screen.get_rect()

#Initial Player Positions
p1x, p1y = 150, 300
p1dx, p1dy = 1, 0
p2x, p2y = 450, 300
p2dx, p2dy = -1, 0

#Player, Move, and Collsion functions
def draw_player(surf, color, pos):
    x, y = pos
    pygame.draw.rect(surf, color, (x, y, 4, 4))

def move(x, y, dx, dy):
    x += dx
    y += dy
    return x, y

def collision(new_pos, pos1, pos2):
    x,y = new_pos
    if new_pos in pos1:
        return True
    if new_pos in pos2:
        return True
    else:
        return False
#time
clock = pygame.time.Clock()
#Game loop
done = False
GAMEOVER = False
PLAYING = False
#Lists to make dragging trails
tron1 = []
tron2 = []

while not done:
    for event in pygame.event.get():
        # Quit
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        #Player1 controls
        elif event.type == KEYDOWN and event.key == K_UP:
            p1dx, p1dy = 0, -1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            p1dx, p1dy = 0, 1
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            p1dx, p1dy = 1, 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            p1dx, p1dy = -1, 0
        #Player 2 controls
        elif event.type == KEYDOWN and event.key == K_w:
            p2dx, p2dy = 0, -1
        elif event.type == KEYDOWN and event.key == K_s:
            p2dx, p2dy = 0, 1
        elif event.type == KEYDOWN and event.key == K_d:
            p2dx, p2dy = 1, 0
        elif event.type == KEYDOWN and event.key == K_a:
            p2dx, p2dy = -1, 0
        #start game with space bar
        if event.type == KEYDOWN and event.key == K_SPACE:
            PLAYING = True
    if PLAYING == True:
        # Move players
        new_pos1 = p1x, p1y = move(p1x, p1y, p1dx, p1dy)
        new_pos2 = p2x, p2y = move(p2x, p2y, p2dx, p2dy)
        # Draw players
        draw_player(screen, RED, (p1x, p1y))
        draw_player(screen, BLUE, (p2x, p2y))
        
        #collision
        collision1 = collision(new_pos1, tron1, tron2)
        collision2 = collision(new_pos2, tron1, tron2)
        
        if collision1:
            PLAYING = False
            print "Player2 wins"
        
        if collision2:
            PLAYING = False
            print "Player1 wins"
        
        if p1x == p2x and p1y == p2y:
            PLAYING = False
            print "You both lose, GAMEOVER"
        
        if p1x == screen_bounds.left:
            print "Player2 wins"
            PLAYING = False
        
        if p1x == screen_bounds.right:
            print "Player2 wins"
            PLAYING = False
        
        if p2x == screen_bounds.left:
            print "Player1 wins"
            PLAYING = False
            
        if p2x == screen_bounds.right:
            print "Player1 wins"
            PLAYING = False
            
        if p1y == screen_bounds.top:
            print "Player2 wins"
            PLAYING = False
            
        if p1y == screen_bounds.bottom:
            print "Player2 wins"
            PLAYING = False
            
        if p2y == screen_bounds.top:
            print "Player1 wins"
            PLAYING = False
            
        if p2y == screen_bounds.bottom:
            print "Player1 wins"
            PLAYING = False
            
        if PLAYING == False:
            PLAYING = False
            screen.fill(BLACK)
            pygame.display.flip()
        
        # Drag lines
        tron1.append(new_pos1)
        tron2.append(new_pos2)
        pygame.display.flip()

    clock.tick(30)
    
        

