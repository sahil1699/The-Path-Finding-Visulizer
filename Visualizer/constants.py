import pygame
import os

#dimensions
WIDTH , HEIGHT = 1340 , 660

GRID_WIDTH, GRID_HEIGHT = 1100, 500 

GAP = 20

GRID_COLS , GRID_ROWS = GRID_WIDTH//GAP, GRID_HEIGHT//GAP

#opens window in center of the screen
os.environ['SDL_VIDEO_CENTERED'] = "True"

#pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


#rgb
RED = (255,0 ,0)
WHITE = (255, 255, 255)
BLACK = (0,0 ,0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128 )
KHAKI = (202,255,112)
ORANGE = (255,97,3)
YELLOW = (255,255,0)
PINK = (234, 1, 132)
GREEN = (0, 255, 0)
BROWN = (138,54,15)

#state for mouse handle
WALL = "wall"
START = "start"
END = "end"

#Algonames 

BREATH_FIRST_SEARCH = "Breath First Search"
DEPTH_FIRST_SEARCH = "Depth First Search"
A_STAR = "A* Search"

#button size

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50


#square type

OTHER_SQUARE = "other"
START_SQUARE = "startsqaure"
END_SQUARE = "endsqure"

#speeds

FAST = 500
SLOW = 6
MEDIUM = 12