#!/usr/bin/env python

import math

from random import randrange

import pygame
from pygame.locals import *


## Settings
C_BLACK = 0,0,0
C_RED = 255,0,0


## from tiefighter.py
def draw_tie(surf, color, size):
    wall = size / 8

    surf.fill(C_BLACK)
    pygame.draw.rect(surf, color, (0, 0, wall, size))
    pygame.draw.rect(surf, color, (size-wall, 0, wall, size))
    pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
    pygame.draw.circle(surf, color, (size/2, size/2), size/4)

class TieFighter(object):
    def __init__(self, x, y, vx, vy, bounds, size=40, color=C_RED):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color
        self.bounds = bounds
        
        #set up image: size of tiefighter to be drawn
        self.image = pygame.Surface((size,size))
        draw_tie(self.image, color, size)
        
        self.rect = pygame.Rect(x,y,size,size)
   
#function to update tiefighter's position
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right: 
            self.vx *= -1
            self.rect.x += self.vx*2
        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy *= -1
            self.rect.y += self.vy*2

    #draws image to surface
    def draw(self, surf):
        surf.blit(self.image, self.rect)

def spawn(tiefighter):
    pass

#create object for game
class Game(object):
    # settings
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

#initialize
    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)
        self.ties = [ ]
        #appends TieFighter object
        self.ties.append(TieFighter(200,200,3,3, self.bounds))

# Game Loop
    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True

            # update
            for tie in self.ties:
                tie.update()
            spawn(TieFighter(randrange(0,800,1), randrange(0,600,1), 3, 3, self.bounds))

        

            # draw
            self.screen.fill(C_BLACK)
            for tie in self.ties:
                tie.draw(self.screen)
            pygame.display.flip()


#creates main function that is mother function to run all other functions in this file only if functions from other files are referenced it will only run those functions, not the file.
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
