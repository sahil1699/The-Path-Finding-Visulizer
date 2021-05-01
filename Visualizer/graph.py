import pygame
import random
from .constants import GRID_ROWS , GRID_COLS,YELLOW, WIN , GAP
from .square import start_square,end_square,Square


class Graph:
    def __init__(self):
        self.wall = [[None for _ in range(GRID_COLS) ] for _ in range(GRID_ROWS)]
        self.visited = [[False for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
    
    def reset(self):
        self.__init__()

    def drawRandomMaze(self):
        self.reset()

        for i in range(GRID_ROWS):
            noWallsInthisRow = random.randint(5 , GRID_COLS - 30 )
            wallonTheseCols =  random.sample(range(0,GRID_COLS), noWallsInthisRow )
            for j in wallonTheseCols:
                if not self.OnStart(i, j) and not self.OnEnd(i, j) :
                    newSquare = Square(WIN, (j * GAP, i * GAP) )
                    self.wall[i][j] = newSquare
                    self.visited[i][j] = True

            
    def drawVerticalMaze(self):
        self.reset()
        for a in range(0,GRID_COLS,2):
            skip1  = random.randint(0,GRID_ROWS//3)
            skip2 = random.randint(GRID_ROWS//3, 2 * GRID_ROWS//3 )
            skip3 = random.randint(2 * GRID_ROWS//3 , GRID_ROWS )
            for b in range(GRID_ROWS):
                if not self.OnStart(b, a) and not self.OnEnd(b, a) :
                    if skip1 != b and skip2 != b and skip3 != b:
                        self.wall[b][a] = Square(WIN, (a* GAP , b* GAP))
                        self.visited[b][a] = True


    def drawHorizentalMaze(self):
        self.reset()
        for a in range(0,GRID_ROWS,2):
            skip1  = random.randint(0,GRID_COLS//3)
            skip2 = random.randint(GRID_COLS//3, 2 * GRID_COLS//3 )
            skip3 = random.randint(2 * GRID_COLS//3 , GRID_COLS )
            for b in range(GRID_COLS):
                if not self.OnStart(a, b) and not self.OnEnd(a, b) :
                    if skip1 != b and skip2 != b and skip3 != b:
                        self.wall[a][b] = Square(WIN, (b* GAP , a* GAP))
                        self.visited[a][b] = True

    def OnStart(self, col ,row ):

        directions = [[0,0] , [1,1] , [-1, -1 ] , [1, -1] , [-1, 1 ] , [1,0] , [0,1] , [-1,0],  [0, -1]]

        for d in directions :
            x = start_square.row + d[0]
            y = start_square.col + d[1]

            if x >= 0 and  y >=0 and x < GRID_COLS and y < GRID_ROWS and row == x and col == y :
                return True

        return False


    def OnEnd(self, col ,row ):
        directions = [[0,0] , [1,1] , [-1, -1 ] , [1, -1] , [-1, 1 ] , [1,0] , [0,1] , [-1,0],  [0, -1]]

        for d in directions :
            x = end_square.row + d[0]
            y = end_square.col + d[1]

            if x >= 0 and  y >=0 and x < GRID_COLS and y < GRID_ROWS and row == x and col == y :
                return True

        return False


graph  = Graph()