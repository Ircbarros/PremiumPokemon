#!/usr/bin/env python3
#pylint: disable=missing-docstring, C0303

'''
Author: Italo Barros
Email: italorenan_@hotmail.com
License: MIT

The Pokemon: Pick them All Game!

You can run this program using the command line:

$ python3 main.py


Classes:

    Map   : Responsible to create the Infinite Map at the screen
    Camera: Responsible to follow the player when he moves

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


import pygame as pg
from world import settings

# LOAD THE DEFAULT VARIABLES
default = settings.GameDefaults()


class Map:
    '''
    This Class is responsible to create the world based in the txt file
    he will read the file and convert the text to a Tilemap

    Args:
     
        filename (str)

    Vars:

        filename : The path location to open the 'map.txt' file 

    '''
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            #* For every line in the map.txt append the map_data
            for line in f:
                self.data.append(line)
        #* The length of the map is the length of the line
        self.tile_width = len(self.data[0])
        #* The height of the map is the number of lines
        self.tile_height = len(self.data)
        #* The pixel width and heigth density
        self.width = self.tile_width * default.TILESIZE
        self.height = self.tile_height * default.TILESIZE


class Camera:
    '''
    This Class is responsible to follow the player while he runs 
    at the screen

    Methods:
     
        apply : Apply a camera rectangle in the screen
        
        update: Follow the Player movements in the screen

    '''
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        '''
        This method will return the camera entity 
        '''
        return entity.rect.move(self.camera.topleft)
    
    def apply_rect(self, rect):
        '''
        This method will apply the camera rectangle
        '''
        return rect.move(self.camera.topleft)
    
    def update(self, target):
        '''
        This method will update the camera at every frame
        '''
        x = -target.rect.x + int(default.SCREEN_WIDTH/2)
        y = -target.rect.y + int(default.SCREEN_HEIGHT/2)
        #self.camera = pg.Rect(x, y, self.width, self.height)
        self.camera = pg.Rect(x, y, self.width, self.height)
