import pygame

from .constants import KHAKI, GRID_WIDTH, GRID_HEIGHT,GRID_COLS,GRID_ROWS,GAP , ORANGE , WIN, PINK ,BREATH_FIRST_SEARCH, DEPTH_FIRST_SEARCH,YELLOW,BLUE,A_STAR
from .square import start_square, end_square
from .graph import graph

from .createButton import BfsButton, ResetButton, DfsButton, FastButton, SlowButton, MediumButton, AStarButton

class Redrawwindow :

    def __init__(self , surface ):
        self.surface = surface
        
    
    def draw(self,curr_algorithem):

        self.surface.fill(KHAKI)

        self.drawGrid()

        start_square.draw()
        end_square.draw()

        for i in range(GRID_ROWS):
            for j in range (GRID_COLS):
                if (graph.wall[i][j]) : graph.wall[i][j].draw()

        if curr_algorithem == None:
            pass
        elif curr_algorithem.name == BREATH_FIRST_SEARCH : 
            self.drawBFS(curr_algorithem)
        elif curr_algorithem.name == DEPTH_FIRST_SEARCH :
            self.drawDFS(curr_algorithem)
        elif curr_algorithem.name == A_STAR:
            self.drawAStar(curr_algorithem)
            
        #algoButton
        BfsButton.draw(self.surface,True)
        DfsButton.draw(self.surface,True)
        AStarButton.draw(self.surface,True)

        #speedButtons
        FastButton.draw(self.surface, True)
        MediumButton.draw(self.surface, True)
        SlowButton.draw(self.surface, True)

        #resetButton
        ResetButton.draw(self.surface, True)

        pygame.display.update()


    def drawGrid(self):
        x = 0
        y = 0

        for _ in range(GRID_ROWS):
            y += GAP
            pygame.draw.line(self.surface,(138,54,15), (0,y),(GRID_WIDTH,y))

        for _ in range(GRID_COLS):
            x += GAP
            pygame.draw.line(self.surface,(138,54,15), (x,0),(x,GRID_HEIGHT))



    def drawBFS(self,curr_algorithem):
        for i in range(len(curr_algorithem.queue)):
            curr_algorithem.queue[0].color = PINK
            curr_algorithem.queue[i].draw()
        
        for i in range(len(curr_algorithem.done)):
            curr_algorithem.done[i].draw()

        for i in range(len(curr_algorithem.answer)):
            curr_algorithem.answer[i].draw()

    def drawDFS(self,curr_algorithem):
        lenOfdone = len(curr_algorithem.done)

        curr_square = curr_algorithem.done[lenOfdone - 1]
        if (not ( start_square.x == curr_square.x and start_square.y == curr_square.y) ) :
            curr_algorithem.done[lenOfdone - 1].color = YELLOW

        for i in range(lenOfdone):
            curr_algorithem.done[i].draw()

        if (not ( start_square.x == curr_square.x and start_square.y == curr_square.y) ) :
            curr_algorithem.done[lenOfdone - 1].color = BLUE

        for i in range(len(curr_algorithem.answer)):
            curr_algorithem.answer[i].draw()

    def drawAStar(self, curr_algorithem):

        for i in range(len(curr_algorithem.open)):
            curr_algorithem.open[i].draw()
        
        for i in range(len(curr_algorithem.closed)):
            curr_algorithem.closed[i].draw()

        for i in range(len(curr_algorithem.answer)):
            curr_algorithem.answer[i].draw()


    