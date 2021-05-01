import pygame

from Visualizer.graph import graph

from Visualizer.square import start_square, end_square, Square

from Visualizer.constants import GRID_HEIGHT, GRID_WIDTH ,BLUE , YELLOW ,GAP,GRID_ROWS,GRID_COLS,PINK, ORANGE, WIN, BREATH_FIRST_SEARCH

from Visualizer.redrawwindow import Redrawwindow


redrawwindow = Redrawwindow(WIN)
clock = pygame.time.Clock()

class BreathFirstSearch :
    def __init__(self,surface):
        self.name = BREATH_FIRST_SEARCH
        self.surface = surface
        self.queue = [] 
        self.privious = {}
        self.done = []
        self.answer = []
        self.pathFound = False
        self.stop = True
    
    def reset(self):
        self.__init__(self.surface)
    
    def run(self, mouseHandler):
        
        self.queue.append(start_square)
        

        self.privious[(start_square.x , start_square.y)] = None

        directions = [[1, 0 ] , [0,1 ] , [-1, 0] , [0, -1]]

        while (len(self.queue) != 0 and not self.pathFound):
            
            clock.tick(mouseHandler.algoSpeed)
            mouseHandler.commanMouseHandler()
            if (self.stop) : return

            curr_square = self.queue.pop(0)


            if (curr_square.x == end_square.x and curr_square.y == end_square.y ):
                self.drawPath(mouseHandler)
                return            

            for d in directions:

                mouseHandler.commanMouseHandler()
                if (self.stop) : return

                x = d[0] +  curr_square.row
                y = d[1] + curr_square.col

                if (x >= 0 and  y >=0 and x < GRID_COLS and y < GRID_ROWS and not graph.visited[y][x]):

                    graph.visited[y][x] = True
                    newSquare = Square(self.surface,(x * GAP , y * GAP), YELLOW )
                    self.queue.append(newSquare)

                    
                    self.privious[(newSquare.x, newSquare.y )] = (curr_square.x , curr_square.y)

                    redrawwindow.draw(self)
            if (not ( start_square.x == curr_square.x and start_square.y == curr_square.y) ) :
                curr_square.color = BLUE
            self.done.append(curr_square)


    def drawPath (self, mouseHandler):
        back = self.privious[(end_square.x , end_square. y )]
        curr_square_x , curr_square_y = back

        while(back != None and not self.pathFound):
            mouseHandler.commanMouseHandler()
            if (self.stop) : return

            self.answer.append(Square(self.surface, (curr_square_x,  curr_square_y) , ORANGE ))

            if(back) : back = self.privious[(curr_square_x, curr_square_y )]

            curr_square_x , curr_square_y = back

            redrawwindow.draw(self)

        mouseHandler.currAlgo = None
        self.pathFound = True
        

        


breathFirstSearch = BreathFirstSearch(WIN)
        



    
