import pygame

from Visualizer.constants import DEPTH_FIRST_SEARCH , WIN , YELLOW, GRID_COLS , GRID_ROWS , GAP ,ORANGE , BLUE

from Visualizer.graph import graph

from Visualizer.square import start_square, end_square, Square

from Visualizer.constants import GRID_ROWS, GRID_COLS

from Visualizer.redrawwindow import Redrawwindow


redrawwindow = Redrawwindow(WIN)
clock = pygame.time.Clock()
class DepthFirstSearch:
    def __init__(self, surface):
        self.name = DEPTH_FIRST_SEARCH
        self.surface = surface
        self.done = []
        self.privious = {}
        self.answer = []
        self.pathFound = False
        self.stop = True
    
    def reset(self):
        self.__init__(self.surface)

    def run(self, mouseHandler):
        
        directions = [ [0, -1] , [1, 0 ], [0,1 ],  [-1, 0] ]
        self.privious[(start_square.x , start_square.y)] = None

        self.recursiveDFS(directions, start_square , mouseHandler ) 
    
    def recursiveDFS(self, directions, curr_square, mouseHandler ):

        clock.tick(mouseHandler.algoSpeed)
        mouseHandler.commanMouseHandler()
        if(self.stop) : return

        if (curr_square.x == end_square.x and curr_square.y == end_square.y):
            self.drawPath(mouseHandler)
            return

        if(self.pathFound) : return

        self.done.append(curr_square)
        
        for d in directions :
            mouseHandler.commanMouseHandler()
            if(self.stop or self.pathFound ) : return

            x, y = curr_square.row, curr_square.col
            x += d[0]
            y += d[1]
            if (x >=  0  and y >=0 and x  < GRID_COLS  and y <  GRID_ROWS and not graph.visited[y][x] ):
                graph.visited[y][x] = True

                newSquare = Square(self.surface,(x * GAP , y * GAP), BLUE )


                self.privious[(newSquare.x, newSquare.y )] = (curr_square.x , curr_square.y)

                redrawwindow.draw(self)

                self.recursiveDFS(directions, newSquare , mouseHandler)

        return


    def drawPath (self, mouseHandler):
        back = self.privious[(end_square.x , end_square. y )]
        curr_square_x , curr_square_y = back

        while(back != None and not self.pathFound):
            mouseHandler.commanMouseHandler()
            if (self.stop) : return

            self.answer.append(Square(self.surface, (curr_square_x,  curr_square_y) , ORANGE ))

            back = self.privious[(curr_square_x, curr_square_y )]

            if(back) :  
                curr_square_x , curr_square_y = back
            else:
                self.pathFound = True

            redrawwindow.draw(self)

        
        
        

depthFirstSearch = DepthFirstSearch(WIN)