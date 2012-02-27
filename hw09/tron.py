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

#Move and Player functions
def move_player_1(x1, y1, dx1, dy1, bounds):
    while not done:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_LEFT:
                dx1 = -1
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                dx1 = 1
            if event.type == KEYDOWN and event.key == K_DOWN:
                dy1 = -1
            elif event.type == KEYDOWN and event.key == K_UP:
                dy1 = 1
        x1 += dx1
        y1 += dy1
        if x1 == bounds.left or bounds.right or y1 == bounds.top or bounds.bottom:
            GAMEOVER = True
        return x1, y1, dx1, dy1

def Player1(pos1):
    x1, y1 = pos1
    pygame.draw.rect(screen, RED, (x1, y1, 4, 4))
    new_pos1 = x1, y1
    pos_player1 = [new_pos1]
    '''for pos in pos_player1:
        if x1 == pos_player1[x1] and y1 == pos_player1[y1]:
            GAMEOVER = True
        pos_player1.append(new_pos1)'''
        
def move_player_2(x2, y2, dx2, dy2, bounds):
    while not done:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_a:
                dx2 = -1
            elif event.type == KEYDOWN and event.key == K_d:
                dx2 = 1
            if event.type == KEYDOWN and event.key == K_s:
                dy2 = -1
            elif event.type == KEYDOWN and event.key == K_w:
                dy2 = 1
        x2 += dx2
        y2 += dy2
        if x2 == bounds.left or bounds.right or y2 == bounds.top or bounds.bottom:
                GAMEOVER = True
        return x2, y2, dx2, dy2

def Player2(pos2):
    x2, y2 = pos2
    pygame.draw.rect(screen, BLUE, (x2, y2, 4, 4))
    new_pos2 = x2, y2
    pos_player2 = [new_pos2]
    '''for pos in pos2:
        if x2 == pos_player2[x2] and y2 == pos_player2[y2]:
            GAMEOVER = True
        pos2.append(new_pos2)'''

tron1 = []
tron2 = []

#Game loop
done = False
GAMEOVER = False
PLAYING = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        if event.type == KEYDOWN and event.key == K_SPACE:
            PLAYING = True
        if PLAYING == True:
            x1, y1 = 250, 300
            dx1, dy1 = 0, 0
            x2, y2 = 350, 300
            dx2, dy2 = 0, 0
            #Move players
            x1, y1, dx1, dy1 = move_player_1(x1, y1, dx1, dy1, screen_bounds)
            x2, y2, dx2, dy2 = move_player_2(x2, y2, dx2, dy2, screen_bounds)
            #Player1(move_player_1())
            #Player2(move_player_2())
            #Drag lines?
            #tron1.append(Player1())
            #tron2.append(Player2())
            # resets display
            if GAMEOVER == True:
                pygame.dislpay.quit()
    
    pygame.display.flip()

