#!/usr/bin/env python

import random
import pygame
from pygame import draw
from pygame.locals import *

#initialize pygame
pygame.init()

#Settings

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (255,0,255)
BACKGROUND = (80,80,80)

#screen
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600,600
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BACKGROUND)
bounds = screen.get_rect()

#refresh settings
clock = pygame.time.Clock()
FPS = 30

#font
numberfont = pygame.font.Font(None, 4)

#Rectangles
RECT_SIZE = 30, 30
squares=[]
bombs = []


# Grid w/ bombs
# Function to make grid with Rect objects
def draw_squares(surf):
	grid = []
	for y in range(300):
		row = []
		for x in range(300):
			if x %30 == 0 and y %30 == 0:
				square = pygame.Rect((x,y), RECT_SIZE)
				squares.append(square)
				row.append(square)
		grid.append(row)
	for y,row in enumerate(grid):
		for x, square in enumerate(row):
			pygame.draw.rect(surf, BLACK, square, 1)
# bomb distribution function
	def draw_bombs():		
		while len(bombs) < 10:
			bomb_x = random.randrange(0,300,30)
			bomb_y = random.randrange(0,300,30)
			if (bomb_x,bomb_y) not in bombs:
				bombs.append((bomb_x,bomb_y))
		bomb = 0
		while bomb <= 9:
			for pos in bombs:
				pygame.draw.circle(surf, BACKGROUND, (pos[0]+15, pos[1]+15) , 10)
				bomb += 1
		return bombs
	draw_bombs()
	return grid, row, squares

# Function to calculate how many bombs a square is touching
def touch():
	touch = 0
	for pos in bombs:
		for square in row:
			if Rect.collidepoint((pos[0],pos[1]))
				touch += 1
				color = BACKGROUND
				text = numberfont.render(touch, True, color, BACKGROUND)
				loc = text.get_rect()
				loc.center = bounds.center 
				screen.blit(text, loc)
done = False

while not done:
	draw_squares(screen)

	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			done = True
			
	pygame.display.flip()
	




