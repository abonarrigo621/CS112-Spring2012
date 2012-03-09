#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

# pieces of code Alec already wrote that we want to access w/ this code
from app import Application
from graphics import draw_tie, draw_ywing
from ships import Ship, ShipSpawner
from utils import *

## EXPLOSIONS
class Explosion(Sprite):
    dradius = 60
    duration = 1500
    
    def __init__(self, pos, radius):
        Sprite.__init__(self)
        self.pos = pos
        self.radius = radius

    def update(self, dt):
        if self.duration > 0:
            self.duration -= dt
        elif self.radius > 0:
            self.radius -= self.dradius * (dt / 1000.0)
        else: 
            self.kill()

    def rand_color(self):
        return randrange(120,256), 255, randrange(120,256)

    def draw(self, surf):
        pygame.draw.circle(surf, self.rand_color(), self.pos, int(self.radius))

class ExplosionGroup(Group):
    def draw(self, surf):
        for xplo in self:
            if xplo.radius > 0 :
                xplo.draw(surf)

## Ship Group... Only add a ship if there's room in the list
class ShipGroup(Group):
    def __init__(self, count):
        Group.__init__(self)
        self.count = count

    def add(self, *sprites):
        for sprite in sprites: 
            if len(self) < self.count:
                Group.add(self, sprite)

## TIE FIGHTER
class TieFighter(Ship):
    width = 40
    height = 40 

    def draw_image(self):
        draw_tie(self.image, self. color)

    def update(self, dt):
        vx = self.vx
        vy = self.vy

        Ship.update(self, dt)

        # create a new ship if bounced (when they bounce, vx, vy no longer = self.vx or self.vy
        if vx != self.vx or vy != self.vy:
            if vx != self.vx:
                vx = self.vx
                vy = -vy
            else: 
                vx = -vx
                vy = self.vy

            tie = TieFighter(self.rect.x, self.rect.y, vx, vy, self.bounds, self.color)
            for group in self.groups():
                group.add(tie)
    
class TieSpawner(ShipSpawner):
    ship_type = TieFighter

    def rand_vel(self):
        vx = randint_neg(100,250)
        vy = randint_neg(100,250)
        return vx, vy

    def rand_color(self):
        r = randrange(128,256)
        return r, 0, 0
## YWING
class YWing(Ship):
    width = 128
    height = 64

    def draw_image(self):
        draw_ywing(self.image, self.color)
        self.orig_image = self.image
        #Flip x image, don't flip y
        self.flipped_image = pygame.transform.flip(self.image, True, False)

    def update(self, dt):
        #one in 60 chance it will flip directions
        if randrange(60) == 0:
            self.vx = -self.vx
        
        Ship.update(self, dt)

        if self.vx > 0:
            self.image = self.orig_image
        else:
            self.image = self.flipped_image

class YWingSpawner(ShipSpawner):
    ship_type = YWing

    def rand_vel(self):
        vx = randint_neg(200, 400)
        return vx, 0

    def rand_color(self):
        r = randrange(128,256)
        return r, r, r


#Application is an object defined in the app code that was imported
class Game(Application):
    title = "Spaceships"
    screen_size = 800, 600
    min_dt = 200
    max_ships = 600
    
    def __init__(self):
        #initialize Application
        Application.__init__(self)

        self.bounds = self.screen.get_rect()
        #won't produce more than max_ships
        self.ships = ShipGroup(self.max_ships) #Sprite Group, makes sprite fxn (collision) easier
        self. spawners = [ TieSpawner(1000, self.ships, self.bounds),
                           YWingSpawner(2000, self.ships, self.bounds)]
        self.xplos = ExplosionGroup()

    def handle_event(event):
        if event.type ==  MOUSEBUTTONDOWN and event.button == 1:
            self.xplos.add( Explosion(pygame.mouse.get_pos())

    def update(self):
        #makes it so the min fram rate it can run at is min dt
        dt = min(self.min_dt, self.clock.get_time())
        self.ships.update(dt)
        self.xplos.update(dt)

        for spawner in self.spawners:
            spawner.update(dt)
       
                         

    def draw(self, screen):
        screen.fill((0,0,0))
        self.ships.draw(screen)


if __name__ == "__main__":
    Game().run()
    print "ByeBye"
