import pygame

from Visualizer.constants import A_STAR,BLACK, OTHER_SQUARE, WIN,GRID_COLS, GRID_ROWS,GAP,YELLOW, BLUE,ORANGE,PINK

from heapq import heapify, heappush, heappop 

from Visualizer.graph import graph 

from Visualizer.square import start_square, end_square , Square

from Visualizer.redrawwindow import Redrawwindow

redrawwindow = Redrawwindow(WIN)
clock = pygame.time.Clock()


class AStarSquare(Square) : 
    count = 0
    def __init__(self,surface,pos,color = BLACK , square_type = OTHER_SQUARE ):
        super().__init__(surface,pos,color , square_type )
        self.f = float("inf")
        self.g = float("inf")
        self.h = float("inf")
        
    
    def __lt__(self, other):
        if (self.f != other.f):
            return self.f < other.f
        elif (self.count != other.count):
            return self.count < other.count
        elif self.h != self.h:
            return self.h < other.h
        else :
            return self.g < self.g

    def __repr__(self) :
        return f'Node value: f{self.f} g{self.g} h{self.h} x{self.row} y{self.col} '
 

class AStar:
    def __init__(self,surface):
        self.surface = surface
        self.name = A_STAR
        self.open = []
        heapify(self.open)
        self.closed = []
        self.privious = {}
        self.pathFound = False
        self.stop = True
        self.answer = []

    def reset(self):
        self.__init__(self.surface)

    def run(self, mouseHandler):
        #curr_count = 0

        astart_start = AStarSquare(self.surface, (start_square.x, start_square.y) )
        astart_start.g = 0


        g_set = {(astart_start.row, astart_start.col ) : astart_start }

        self.privious[(start_square.x, start_square.y)] =  None

        heappush(self.open, astart_start )

        heapSet = {astart_start}

        directions = [[1,0] ,[0, 1] , [-1, 0] , [0, -1]]

        while len(self.open) != 0 and not self.pathFound :
            
            clock.tick(mouseHandler.algoSpeed)
            mouseHandler.commanMouseHandler()
            if (self.stop) : return

            curr_square = heappop(self.open)
            curr_square.color = PINK
            heapSet.remove(curr_square)
            redrawwindow.draw(self)

            if (curr_square.x == end_square.x and curr_square.y == end_square.y ):
                self.drawPath(mouseHandler)
                return
                

            for d in directions :
                x = d[0] +  curr_square.row
                y = d[1] + curr_square.col
                
                if (x >= 0 and  y >=0 and x < GRID_COLS and y < GRID_ROWS and not graph.visited[y][x] ):

                    if (x,y)  in  g_set :
                        newSquare = g_set[(x,y)]
                    else:
                        newSquare = AStarSquare(self.surface, (GAP * x, GAP * y), YELLOW)                    
                        g_set[(x,y)] =  newSquare


                    temp_g = curr_square.g + 1

                    if (temp_g < newSquare.g  ): 

                        self.privious[(newSquare.x, newSquare.y)] =  (curr_square.x , curr_square.y)
                        newSquare.g = temp_g
                        newSquare.h = self.getHuristic((newSquare.row, newSquare.col), (end_square.row, end_square.col) )
                        newSquare.f = newSquare.g + newSquare.h
                        if newSquare not in heapSet:
                            # curr_count += 1
                            # curr_square.count = curr_count
                            heappush(self.open, newSquare)
                            heapSet.add(newSquare )

            curr_square.color = BLUE
            self.closed.append(curr_square)
            redrawwindow.draw(self)

            
    def getHuristic(self, curr, goal):
        curr_x , curr_y = curr
        goal_x , goal_y = goal

        h = abs (curr_x - goal_x) + abs (curr_y - goal_y)

        return h

    def drawPath (self, mouseHandler):
        back = self.privious[(end_square.x , end_square. y )]
        curr_square_x , curr_square_y = back

        while(back != None and not self.pathFound):
            mouseHandler.commanMouseHandler()
            if (self.stop) : return

            self.answer.append(Square(self.surface, (curr_square_x,  curr_square_y) , ORANGE ))

            if(back) : back = self.privious[(curr_square_x, curr_square_y )]

            if (back) : curr_square_x , curr_square_y = back

            redrawwindow.draw(self)

        
        self.pathFound = True


aStar = AStar(WIN)