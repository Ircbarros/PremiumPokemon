#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Italo Barros
Email: ircbarros@pm.me
License: MIT

This module is responsible to save the Sprites Variables and Methods


Classes:

    Player    : Create a new Player on the Grid and Update his position
                when needed
    WorldLimit: Create the Limits to travel
    Pokebola  : Create the Pokebola "Item" who can be collected by the
                player

Comments:

If you are using VS Code, please install the Better Comments Extension:
    # Indicates the Method
    #* Indicates some Important Information
    #! Indicates a deprecated or Warning Information
    #? Indicates possible future changes and questions
    #TODO: Indicates the future changes and optimizations
Need to change the code? Refactor? Help the next developer! Use a 
Style Guide to help others understand of your code. For more informations
about the Google Style Guide used here go to:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
'''

import sys
import os
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import world.settings as settings
import pyautogui
import pygame as pg

# LOAD THE COLORS
paint = settings.Colors()
# LOAD THE DEFAULT VARIABLES
default = settings.GameDefaults()
# LOAD THE IMG AND VECTORS
vectors = settings.Vectors()
# LOAD THE PYGAME MATH LIB
vec = pg.math.Vector2
# SAVES THE GAME FOLDER STR
game_folder = os.path.dirname(os.path.abspath(__file__))
# RESPONSIBLE TO BREAK THE ANIMATION LOOP
LOOPS = 0
#pylint: disable=missing-docstring, W1401
#pylint: disable=missing-docstring, C0303
#pylint: disable=missing-docstring, I1101
#pylint: disable=missing-docstring, E1101


class Player(pg.sprite.Sprite):
    '''
    This Class is responsible to deal with the player movements and
    animations.

    Methods:
     
        move       : Responsible to move the player in the screen
        update     : Responsible to update the player in the screen
        world_limit: Responsible to draw the Map Obstacles Limits

    '''
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #* The Game Images

        self.images_top = game.player_walk_top
        self.images_bottom = game.player_walk_bottom
        self.images_left = game.player_walk_left
        self.images_right = game.player_walk_right

        #* Define Player Locations
        self.pos = vec(x, y) * default.TILESIZE
        #* Define Speed
        self.vel = vec(0, 0)
        #* Define Rotation
        self.rotation = 0
        #* Define the Animation Counter
        self.animation_counter = -1
        #* Define the max Counter
        self.max_animation_counter = 60
        #* Define the Walk Count
        self.walk_count = 0
    
    def animate_horizontal(self):
        '''
        This method will run the horizontal animations
        '''
        if self.vel.x == 0:
            self.image = self.game.player_waiting
            self.rect = self.image.get_rect()
        else:
            self.vel.y = 0
            self.walk_count += 1
        if self.vel.x > 0:
            self.vel.y = 0
            if self.walk_count < 60:
                self.image = self.images_right[0]
                self.image.get_rect()
            else:
                self.walk_count = 0
                self.image = self.images_right[1]
                self.image.get_rect()
        if self.vel.x < 0:
            self.vel.y = 0
            if self.walk_count < 60:
                self.image = self.images_left[0]
                self.image.get_rect()
            else:
                self.walk_count = 0
                self.image = self.images_left[1]
                self.image.get_rect()


    def animate_vertical(self):
        '''
        This method will run the vertical animations
        '''
        if self.vel.y > 0:
            self.walk_count += 1
            self.vel.x = 0
            if self.walk_count < 60:
                self.image = self.images_bottom[0]
                self.image.get_rect()
            else:
                self.walk_count = 0
        if self.vel.y < 0:
            self.walk_count += 1
            if self.walk_count < 60:
                self.image = self.images_top[0]
                self.image.get_rect()
            else:
                self.walk_count = 0


    def simulate_keyboard(self, mov_direction):
        '''
        This method is responsible to simulate the keyboard movements

        Args:

            mov_direction (str)
        
        Vars:

            mov_direction: The desired direction that we want to move the
                           player
        '''
        self.values = mov_direction
        if self.values == 'O':
            pyautogui.press('a')
            pyautogui.keyUp('a')
            return
        elif self.values == 'E':
            pyautogui.press('d')
            pyautogui.keyUp('d')
            return
        elif self.values == 'N':
            pyautogui.press('w')
            pyautogui.keyUp('w')
            return
        elif self.values == 'S':
            pyautogui.press('s')
            pyautogui.keyUp('s')
            return


    
    def send_path(self):
        '''
        This method is responsible to send the paths threaded to the
        simulate keyboard function
        '''
        run_path = self.game.desired_path
        global LOOPS
        #* If the Path is Concluded then do Nothing
        if LOOPS == len(run_path):
            return
        #* Send the values and simulate the keyboard movement
        for values in run_path:
            LOOPS += 1
            self.simulate_keyboard(values)


    def get_movement(self):
        '''
        This method will uptade the player movement for every frame loop
        '''
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -default.MAX_SPEED
        elif keys[pg.K_d]:
            self.vel.x = default.MAX_SPEED
        elif keys[pg.K_w]:
            self.vel.y = -default.MAX_SPEED
        elif keys[pg.K_s]:
            self.vel.y = default.MAX_SPEED


    def update(self):
        '''
        This method will uptade the player in the Grid for every frame loop
        '''
        self.get_movement()
        self.animate_horizontal()
        self.animate_vertical()
        self.pos += self.vel
        self.rect.x = self.pos.x
        self.world_limit('x')
        self.rect.y = self.pos.y
        self.world_limit('y')
        with ThreadPoolExecutor(8) as executor:
            executor.submit(self.send_path())



    def world_limit(self, dir):
        '''
        This method is responsible to define the Grid Limits

        Args:

            dir (str)

        Vars:

            dir: The X or Y direction were the player colides 
        '''
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.limits, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                    self.print_end()
                    pg.quit()
                    sys.stdin.close()
                    sys.exit(1)
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                    self.print_end()
                    pg.quit()
                    sys.stdin.close()
                    sys.exit(1)
                self.vel.x = 0
                self.rect.x = self.pos.x
                
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.limits, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                    self.print_end()
                    pg.quit()
                    sys.stdin.close()
                    sys.exit(1)
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                    self.print_end()
                    pg.quit()
                    sys.stdin.close()
                    sys.exit(1)
                self.vel.y = 0
                self.rect.y = self.pos.y
                self.print_end()


    def print_end(self):
        print(
        '''
                    ______________                               
                ,===:'.,            `-._                           
                    `:.`---.__         `-._                       
                    `:.     `--.         `.                     
                        \.        `.         `.                   
                (,,(,    \.         `.   ____,-`.,                
            (,'     `/   \.   ,--.___`.'                         
        ,  ,'  ,--.  `,   \.;'         `                         
        `{D, {    \  :    \;                                    
            V,,'    /  /    //                                    
            j;;    /  ,' ,-//.    ,---.      ,                    
            \;'   /  ,' /  _  \  /  _  \   ,'/                    
                \   `'  / \  `'  / \  `.' /                     
                    `.___,'   `.__,'   `.__,' 

            OH NO! YOU ENTERED IN THE WORLD LIMIT!
            The world is infinte but you will face
            some bad dragons after here, please go
            back and keep catching some Pokemons!
            ''')


class WorldLimit(pg.sprite.Sprite):
    '''
    This Class is responsible to create the world limit obstacles
    that will be used to block the Player movement when he tryes
    to pass trought it.

    Args:
     
        game: The Game Class
        x   : The Position in the X axis desired
        y   : The Position in the Y axis desired

    '''
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.limits
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((default.TILESIZE, default.TILESIZE))
        self.image.fill(paint.COLOR_VERMILION)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * default.TILESIZE
        self.rect.y = y * default.TILESIZE



class Pokebola(pg.sprite.Sprite):
    '''
    This Class is responsible to create the Pokebolas in
    the world

    Args:
     
        game: The Game Class
        x   : The Position in the X axis desired
        y   : The Position in the Y axis desired
    '''
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.pokebola_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * default.TILESIZE
        self.rect.y = y * default.TILESIZE
