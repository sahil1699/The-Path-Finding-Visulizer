import pygame

from .constants import GRID_ROWS , GRID_COLS


class Graph:
    def __init__(self):
        self.wall = [[None for _ in range(GRID_COLS) ] for _ in range(GRID_ROWS)]
        self.visited = [[False for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
    
    def reset(self):
        self.__init__()

graph  = Graph()