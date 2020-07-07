#!/usr/bin/env python3

'''
Author: Italo Barros
Email: italorenan_@hotmail.com
License: MIT

The Pokemon: Pick them All Game!

You can run this program using the command line:

$ python3 main.py


Classes:

        Game: The Main Class Responsible to load the Game

Functions:

        run_game       : The Method Responsible to run the Game inside the
                         screen
        clear_raw_input: The Method Responsible to Clear the stdin input

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
import sys
from warnings import warn
from multiprocessing import Process
#pylint: disable=wrong-import-position
# DONT SHOW 'WELCOME TO PYGAME'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
#pylint: enable=wrong-import-position
import world.settings as settings
from world.sprites import Player, WorldLimit, Pokebola
from world.tilemap import Map, Camera

# LOAD THE COLORS
paint = settings.Colors()
# LOAD THE DEFAULT VARIABLES
default = settings.GameDefaults()
# LOAD THE IMG AND VECTORS
vectors = settings.Vectors()
# SAVES THE GAME FOLDER STR
game_folder = os.path.dirname(os.path.abspath(__file__))
# WORLD GAME FOLDER
world_folder = os.path.join(game_folder, 'world')
# IMAGES FOLDER
images_folder = os.path.join(game_folder, 'vectors')
# SOUNDS FOLDER
sounds_folder = os.path.join(game_folder, 'sounds')
# THE NUMBER OF POKEBOLAS COLLECTED
POKEBOLAS_QTD = 1
#pylint: disable=missing-docstring, E1101


class Game:
    '''

    Game Class:

    This Class is responsible to Run the Game using the Pygame Library,
    and also to Animate and Interact with the Stdin.

    Functions:

        load_data          : Responsible to Read the Grid Map
        New                : Responsible to create the Game Sprites
        Run                : Responsible to Run the Game in a Loop
        Quit               : Responsible to Quit the Game
        Update             : Responsible to Update the Frames
        collected_pokebolas: Responsible to save the Pokebolas
                                collected by the player
        draw_grid          : Responsible to Draw the Tilemap Grid
        draw               : Responsible to draw the Screen Background
        events             : Responsible to Deal with Game Events

    '''
    def __init__(self):
        # INIT THE PYGAME LIB
        pg.init()
        # SET THE SCREEN
        self.screen = pg.display.set_mode((default.SCREEN_WIDTH,
                                           default.SCREEN_HEIGHT))
        pg.display.set_caption(default.TITLE)
        # SET THE GAME CLOCK
        self.clock = pg.time.Clock()
        self.load_data()


    def load_data(self):
        '''
        This method will read some data to use in the game
        '''
        #* The World Map File
        self.map = Map(os.path.join(world_folder, 'big_map.txt'))
        #* The Player Image Folder
        player_img_folder = os.path.join(images_folder, 'player')
        #* The Player Image Movements
        #pylint: disable=missing-docstring, C0301
        self.player_walk_top = [pg.image.load(os.path.join(player_img_folder,
                                                           vectors.player_top_0)).convert_alpha()
                                ]
        self.player_walk_bottom = [pg.image.load(os.path.join(player_img_folder,
                                                              vectors.player_down_0)).convert_alpha()
                                   ]
        self.player_walk_right = [pg.image.load(os.path.join(player_img_folder,
                                                             vectors.player_right_0)).convert_alpha(),
                                  pg.image.load(os.path.join(player_img_folder,
                                                             vectors.player_right_1)).convert_alpha()
                                 ]
        self.player_walk_left = [pg.image.load(os.path.join(player_img_folder,
                                                            vectors.player_left_0)).convert_alpha(),
                                 pg.image.load(os.path.join(player_img_folder,
                                                            vectors.player_left_1)).convert_alpha()
                                 ]
        #pylint: enable=missing-docstring, C0301
        #* The Player Waiting Image
        self.player_waiting = pg.image.load(os.path.join(player_img_folder,
                                                         vectors.player_waiting)).convert_alpha()
        #* The Pokebola Image Folder
        pokebola_img_folder = os.path.join(images_folder, 'pokebola')
        #* The Player Image Movements
        self.pokebola_img = pg.image.load(os.path.join(pokebola_img_folder,
                                                       vectors.pokebola)).convert_alpha()
        self.pokebola_img = pg.transform.scale(self.pokebola_img, (32, 32))
        #* The Background Image
        self.background_img = pg.image.load(os.path.join(images_folder, vectors.background))
        #* The Desired Path
        self.desired_path = DESIRED_PATH


    def new(self):
        '''
        This method will initialize all the Game Sprites and Limits
        '''
        self.all_sprites = pg.sprite.Group()
        self.limits = pg.sprite.Group()
        self.items = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                #* If the line has a '1' is a Limit
                if tile == '1':
                    WorldLimit(self, col, row)
                #* If the Line has a 'P' is the Player position
                if tile == 'P':
                    self.player = Player(self, col, row)
                else:
                    Pokebola(self, col, row)
        # USES THE CAMERA
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        '''
        This method will keep the game running in the screen
        '''
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def quit(self):
        '''
        Method responsible to Quit the Application when Needed

        Returns:

            Quit the Game
        '''
        pg.quit()
        sys.exit()


    def collected_pokebolas(self, amount=1):
        '''
        Method responsible to calculate the amount of Pokebolas
        collected by the Player
        '''
        global POKEBOLAS_QTD
        POKEBOLAS_QTD += amount
        self.pokebolas_qtd = POKEBOLAS_QTD


    def update(self):
        '''
        Method responsible to Update the Sprites in the Screen

        Returns:

            The Sprites Updated in the Screen for every game loop
        '''
        self.all_sprites.update()
        self.camera.update(self.player)
        self.hits = pg.sprite.spritecollide(self.player, self.items, True)
        self.collected_pokebolas(len(self.hits))


    def draw_grid(self):
        '''
        Method responsible to draw the Grid (Tilemap) in the Screen

        Returns:

            The Tilemmap Grid Drawn in the Screen
        '''
        for x in range(0, default.SCREEN_WIDTH, default.TILESIZE):
            pg.draw.line(self.screen, paint.COLOR_GRAYISH, (x, 0), (x, default.SCREEN_HEIGHT))
        for y in range(0, default.SCREEN_HEIGHT, default.TILESIZE):
            pg.draw.line(self.screen, paint.COLOR_GRAYISH, (0, y), (default.SCREEN_WIDTH, y))


    def draw(self):
        '''
        Method responsible to paint the main screen

        Returns:

            The Screen Filled with the desired color or image and
            with the Sprites Drawn
        '''
        self.screen.fill(paint.COLOR_WHITE)
        self.screen.blit(self.background_img, (0, 0))
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()


    def events(self):
        '''
        Method responsible to deal with some events in the screen

        Returns:

            The action desired for the event
        '''
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_end_screen(self):
        '''
        Method responsible to shows the end screen when the player
        finish the movements
        '''
        pass

def run_game():
    '''
    The Main Method is responsible to run the Game

    Returns:

        The Pokemon Game in a 1024x768 screen.
    '''
    #* The Program Icon
    program_icon = pg.image.load(os.path.join(images_folder,
                                              vectors.logo))
    pg.display.set_icon(program_icon)
    game = Game()
    #* The Background Sound
    sound_path = os.path.join(sounds_folder, vectors.main_sound)
    main_music = pg.mixer.Sound(str(sound_path))
    main_music.set_volume(0.4)
    main_music.play()
    while True:
        game.new()
        game.run()
        game.show_end_screen()


def clear_raw_input():
    '''
    The main Function Responsible to read and clean the stdin input.

    The function reads the desired path inputed in the stdin, upper the str characters,
    encode the text in ASCII format and ignore special symbols, removes numbers
    letters and tricky characters, translate the ascii to a list, and finnaly uses
    the maketrans to delete all special characters.

    Attributes:

        remove_characters (str): Some characters that we don't want to add to the
                                 desired path

    Return:

        The desired Path with the coordinates N, S, E or O in the sequence inputed by
        the user

    Raises:

        UserWarning: If the stdin inputed doesn't have the path coordinates (N,S,E,O)

    '''
    #* Join is more efficient than concatenate with "+"
    remove_characters = "".join(['012345671890', 'ABCDFGHIJKLMPQRTUVWXYZbnx', "'", '"'])

    #* Single Jump Operation for a more efficient Infinite Loop
    while 1:
        try:
            raw_stdin = sys.stdin.readline().upper()
            # Encode the stdin to ASCII to remove symbols and special letters
            raw_to_ascii = str(raw_stdin.encode(encoding='ascii', errors='ignore'))
            raw_del_int = str.maketrans(dict.fromkeys(remove_characters))
            #* Remove all lines and blank spaces
            raw_str = raw_to_ascii.translate(raw_del_int).split(None, 0)
            #* Apply a filter on each character that isn't a string an join all
            path = ["".join(list(filter(str.isalnum, line))) for line in raw_str]
            #* If the path is empty (no commands found)
            if path == ['']:
                warn('The Desired Path is Empty, '+
                     'please run again and provide a valid Path', stacklevel=3)
                break
            #* If the path is not empty
            global DESIRED_PATH
            DESIRED_PATH = list(path[0])
            #* Using Multiprocessing to reduce heavy
            Process(target=run_game).start()
            sys.exit(0)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    #* Run the stdin input and Game threaded
    clear_raw_input()
