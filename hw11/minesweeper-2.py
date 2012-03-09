#!/usr/bin/env python

from random import randrange
import pygame
from pygame import draw
from pygame.locals import *

#initialize pygame
pygame.init()

#Settings
WIDTH = 10
HEIGHT = 10
NUM_BOMBS = 10
TILE = 50
BORDER = 2

SCREEN_SIZE = WIDTH*TILE+BORDER, HEIGHT*TILE+BORDER
FPS = 30

#Colors
C_HIDDEN = (0,0,0)
WHITE = (255,255,255)
GREY = (80,80,80)
RED = (255,0,0)
C_ACTIVE = (220,220,220)
C_CLEARED = (160,160,160)
C_BOMB = (255, 0 , 0)
C_1 = (0,255,0)
C_2 = (255,255,0)
C_3 = (0,0,255)
C_4 = (255,0,255)
C_5 = (255,165,0)
C_6 = (255,155,180)
C_7 = (139,69,19)
C_8 = (0,255,255)

#font
numberfont = pygame.font.Font(None, 40)
winfont = pygame.font.Font(None, 80)

def empty_grid(width,height, value=0):
	grid = []
	for y in range(height):
		row = []
		for x in range(width):
			row.append(value)
		grid.append(row)
	return grid

def place_bombs(level, num_bombs, pos_bombs):
	width = len(level[0])
	height = len(level)

	bombs = 0
	while bombs < num_bombs:
		x = randrange(width)
		y = randrange(height)
		if level[y][x] == 0:
			level[y][x] = -1
			bombs += 1
			pos_bombs.append(level[y][x])

def bomb_at(level,x,y,width,height):
	if x < 0 or x >= width:
		return 0
	if y < 0 or y >= height:
		return 0
	if level[y][x] == -1:
		return 1
	else:
		return 0
	
def calc_counts(level):
	width = len(level[0])
	height = len(level[1])
	for x in range(width):
		for y in range(height):
			if level[y][x] != -1:
				level[y][x] += bomb_at(level, y+1, x+1, width, height)
				level[y][x] += bomb_at(level, y, x+1, width, height)
				level[y][x] += bomb_at(level, y-1, x+1, width, height)
				level[y][x] += bomb_at(level, y-1, x, width, height)
				level[y][x] += bomb_at(level, y-1, x-1, width, height)
				level[y][x] += bomb_at(level, y, x-1, width, height)
				level[y][x] += bomb_at(level, y+1, x-1, width, height)
				level[y][x] += bomb_at(level, y+1, x, width, height)
	return level[y][x]
			

def draw_numbers(screen, level, row, a, color):
	for y,row in enumerate(level):
		for x,a in enumerate(row):
			text_a = numberfont.render(str(a), True, color)
			screen.blit(text_a, (level[y][x]))
			
def draw_numbers2(screen, a, rects, row, color):
	for y,row in enumerate(rects):
		for x,a in enumerate(row):
			for rect in rects:
				text_a = numberfont.render(str(a), True, color)
				loc_a = text_a.get_rect()
				loc_a.center = rects[y][x].center
				screen.blit(text_a, loc_a)

def flagged_bomb(flag, bomb):
	x,y = pos
	for pos in pos_flag:
		if pos in pos_bombs:
			marked_bombs += 1


# Game
def game(screen, width, height, num_bombs):
        #initialize
	Flag = 0
	marked_bombs = 0
	pos_Flag = []
	pos_bombs = []
	level = empty_grid(width, height)
	place_bombs(level, num_bombs, pos_bombs)
	calc_counts(level)

	cleared = empty_grid(width, height, True)

	rects = empty_grid(width, height)
	for y, row in enumerate(rects):
		for x, v in enumerate(row):
			rects[y][x] = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
	 
	
        #game loop
	done = False
	mouseclick = False
	clear_square = False
	clock = pygame.time.Clock()
	
	while not done:
		for event in pygame.event.get():
			if event.type == QUIT:
				done = True
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				done = True
			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				mouseclick = True
				x,y = pygame.mouse.get_pos()
				x /= TILE
				y /= TILE
				if (x, y) in pos_bombs:
					cleared = True
					done = True
			elif event.type == MOUSEBUTTONUP and event.button == 1:
				mouseclick = False
				clear_square = True
			elif event.type == MOUSEBUTTONDOWN and event.button == 2:
				mouseclick = True
				x,y = pygame.mouse.get_pos()
				x /= TILE
				y /= TILE
				pygame.draw.rect(screen, WHITE, (x+25, y+5), 1, 40)
				pygame.draw.rect(screen, RED, (x+26, y+5), 10,10)
				pos_Flag.append([x,y])
				Flag += 1
			elif event.type == MOUSEBUTTONUP and event.button == 2:
				mouseclick = False

			
		#update
		if clear_square:
			x,y = pygame.mouse.get_pos()
			x /= TILE
			y /= TILE

			cleared[y][x] = True
			clear_square = False
		
		if marked_bombs == 10:
			win_text = winfont.render("You Win!", True, WHITE)
			loc = text.get_rect()
			loc.center = bounds.center
			done = True
			
		
		

		#draw
		#fill the entire screen with border
		#draw background
		screen.fill(GREY)
		#draw each square
		for y in range(height):
			for x in range(width):
				rect = rects[y][x]
				
				# find color of cell
				if cleared[y][x]:
					color = C_CLEARED
				elif mouseclick and rect.collidepoint(pygame.mouse.get_pos()):
					color = C_ACTIVE
				 
				else:
					color = C_HIDDEN


				# draw bg cell
				screen.fill(color, rect.inflate(-BORDER, -BORDER))

				# draw stuff
				if cleared[y][x]:
					if level[y][x] == -1:
						pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-BORDER, -BORDER))
					elif level[y][x] == 1:
						draw_numbers2(screen,"1", rects, row, C_1)
					elif level[y][x] == 2:
						draw_numbers2(screen, 2, rects, row, C_2)
					elif level[y][x] == 3:
						draw_numbers2(screen, 3, rects, row, C_3)
					elif level[y][x] == 4:
						draw_numbers2(screen, 4, rects, row, C_4)
					elif level[y][x] == 5:
						draw_numbers2(screen, 5, rects, row, C_5)
					elif level[y][x] == 6:
						draw_numbers2(screen, 6, rects, row, C_6)
					elif level[y][x] == 7:
						draw_numbers2(screen, 7, rects, row, C_7)
					elif level[y][x] == 8:
						draw_numbers2(screen, 8, rects, row, C_8)
					'''elif level[y][x] == 1:
						draw_numbers(screen, level, row, 1, C_1)
					elif level[y][x] == 2:
						draw_numbers(screen, level, row, 2, C_2)
					elif level[y][x] == 3:
						draw_numbers(screen, level, row, 3, C_3)
					elif level[y][x] == 4:
						draw_numbers(screen, level, row, 4, C_4)
					elif level[y][x] == 5:
						draw_numbers(screen, level, row, 5, C_5)
					elif level[y][x] == 6:
						draw_numbers(screen, level, row, 6, C_6)
					elif level[y][x] == 7:
						draw_numbers(screen, level, row, 7, C_7)
					elif level[y][x] == 8:
						draw_numbers(screen, level, row, 8, C_8)'''
						

				

		#refresh
		pygame.display.flip()
		clock.tick(FPS)
				

# Application (for restart)
def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	bounds = screen.get_rect()
	game(screen, WIDTH, HEIGHT, NUM_BOMBS)

main()
print "ByeBye"

"""
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
done = False

while not done:
	draw_squares(screen)

	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			done = True
			
	pygame.display.flip()
"""	




