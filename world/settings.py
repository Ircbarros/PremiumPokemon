#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Italo Barros
Email: ircbarros@pm.me
License: MIT

This module is responsible to save the variables used to create the
Grid World. Here you can change the variables to run the world you want!

Classes:

    GameDefaults: The Default Game Variables to Run the World
    Vectors     : The images and vectors used in the game
    Colors      : The Colors used in the game

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

import os
#pylint: disable=wrong-import-position
# DONT SHOW 'WELCOME TO PYGAME'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
#pylint: enable=wrong-import-position
#pylint: disable=missing-docstring, C0103


class GameDefaults:
    '''
    Class responsible to save some Pygame Variables
    '''
    def __init__(self):
        #* SET the DEFAULT Grid Width
        self.SCREEN_WIDTH = 1024
        #* SET the DEFAULT Grid Height
        self.SCREEN_HEIGHT = 768
        #* SET the DEFAULT Width and Height of the Grid Cells
        self.TILESIZE = 32
        #* SET the DEFAUL GRID WIDTH AND HEIGHT
        self.GRIDWIDTH = self.SCREEN_WIDTH / self.TILESIZE
        self.GRIDHEIGHT = self.SCREEN_HEIGHT / self.TILESIZE
        #* SET the DEFAULT SPEED
        self.MAX_SPEED = 32
        # DEFINE THE FPS
        self.FPS = 60
        # DEFINE THE FONT NAME
        self.FONT_NAME = pygame.font.match_font('dejavusans')
        self.TITLE = str("Pokémon - Gotta Catch'em all!")



class Vectors:
    '''
    Class responsible to save dir for images and vectors used
    '''
    def __init__(self):
        # THE PLAYER IMAGES
        self.player_top_0 = 'move_top_0.png'
        self.player_down_0 = 'move_down_0.png'
        self.player_left_0 = 'move_left_0.png'
        self.player_left_1 = 'move_left_1.png'
        self.player_right_0 = 'move_right_0.png'
        self.player_right_1 = 'move_right_1.png'
        self.player_waiting = 'player_waiting.png'
        # THE ITEM IMAGE
        self.pokebola = 'pokebola_closed.png'
        # THE BACKGROUND IMAGE
        self.background = 'background.png'
        # THE GAME LOGO
        self.logo = 'ircbarros_logo.png'
        # THE GAME SOUNDS
        self.main_sound = 'world_sound.wav'

class Colors:
    '''
    Class responsible to save the colors used to paint the Screen
    '''
    def __init__(self):
        #? For more RGB Colors go to:
        # https://graf1x.com/shades-of-red-color-palette-hex-rgb-code/
        #? To translate Corors to the Decimal RGB Format go to:
        # https://www.colorhexa.com/

        self.COLOR_BLACK = (0, 0, 0)
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_GREEN = (0, 255, 0)
        self.COLOR_RED = (255, 0, 0)
        self.COLOR_CYAN = (0, 255, 255)
        self.COLOR_MAGENTA = (255, 0, 255)
        self.COLOR_YELLOW = (255, 255, 0)
        self.COLOR_YELLOW_ROYAL = (250, 218, 94)
        #* The Recharge Zone Color
        self.COLOR_SOFT_YELLOW = (239, 217, 127)
        self.COLOR_DARKGRAY = (40, 40, 40)
        self.COLOR_MEDGRAY = (75, 75, 75)
        self.COLOR_STATEGRAY = (211, 211, 211)
        #* The Obstacles Color
        self.COLOR_LIGHTGRAY = (170, 170, 169)
        #* The Workers Zone Color
        self.COLOR_PRUSSIAN = (9, 71, 99)
        #* The Delivery Zone Color
        self.COLOR_CAROLINA = (118, 180, 214)
        #* The Treadmill Zone Color
        self.COLOR_INDEPENDENCE = (64, 90, 155)
        #* The Pickup Zone Color
        self.COLOR_VERMILION = (163, 44, 50)
        #* The Don't Move Zone Color
        self.COLOR_GRAYISH = (226, 230, 230)
