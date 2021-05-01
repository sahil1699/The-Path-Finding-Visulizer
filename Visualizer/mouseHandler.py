import pygame

from .square import start_square, end_square ,Square , reset_square

from .constants import START, END ,WALL , GAP , GRID_ROWS, GRID_COLS , GRID_HEIGHT ,GRID_WIDTH,FAST,MEDIUM,SLOW,RED,GREEN

from .graph import graph

from .createButton import BfsButton, ResetButton, DfsButton ,FastButton, SlowButton , MediumButton,AStarButton, RandomMazeButton, VerticalMazeButton, HorizentalMazeButton

from Visualizer.Algorithmes.breathFirstSearch import breathFirstSearch
from Visualizer.Algorithmes.depthFirstSearch import depthFirstSearch
from Visualizer.Algorithmes.aStar import aStar

class MouseHandler:
    def __init__(self,surface):
        self.surface = surface
        self.isDraging = False
        self.offset_x = 0
        self.offset_y =0 
        #state wall start end
        self.currAlgo = None
        self.state = WALL
        self.algoSpeed = FAST

    def mouseDrag(self,event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                self.isDraging = True
                if start_square.collidepoint(event.pos) :
                    self.state = START
                    
                    self.dragStartingNode(event.pos, False ) 

                elif end_square.collidepoint(event.pos):
                    self.state = END
                    self.dragEndingNode(event.pos, False )
                else:
                    
                    self.drawWall(event.pos)
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                start_square.backToSquare()
                end_square.backToSquare()
                
                self.__init__(self.surface)

        elif event.type == pygame.MOUSEMOTION:
        
            if self.isDraging:
                if self.state == START:
                    self.dragStartingNode(event.pos, True)
                elif self.state == END:
                    self.dragEndingNode(event.pos, True)
                else:
                    self.drawWall(event.pos)


    def dragStartingNode(self, pos, inMotion ):
        if (self.isDraging) :
            
            mouse_x , mouse_y = pos
            
            if not inMotion :
                self.offset_x = start_square.x - mouse_x
                self.offset_y = start_square.y - mouse_y 
            
            start_square.x =  mouse_x + self.offset_x
            start_square.y = mouse_y + self.offset_y
    
    def dragEndingNode(self, pos, inMotion ):
        
        if (self.isDraging) :
            mouse_x , mouse_y = pos
           
            if not inMotion :
                self.offset_x = end_square.x - mouse_x
                self.offset_y = end_square.y - mouse_y
            
            end_square.x =  mouse_x + self.offset_x
            end_square.y = mouse_y + self.offset_y
    
    def drawWall(self, pos):
        newSquare = Square(self.surface, pos)
        if not (newSquare.x == start_square.x and newSquare.y == start_square.y ) and not ( newSquare.x == end_square.x and newSquare.y == end_square.y ) :  
            graph.wall[newSquare.y//GAP][newSquare.x//GAP] = newSquare
            graph.visited[newSquare.y//GAP][newSquare.x//GAP] = True
        
    def buttonclick(self,mybutton,pos,event, Buttontype = None):
    
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mybutton.isOver(pos):
                return True

        if event.type == pygame.MOUSEMOTION:
            if Buttontype == None:
                if mybutton.isOver(pos):
                    mybutton.color = (255,0,0)
                else:
                    mybutton.color = (0,255,0)

        return False
    

    def checkButtonClick(self, event, pos ):
        
        #resetButton
        if(self.buttonclick(ResetButton, pos, event)) :
            if (self.currAlgo) : 
                self.currAlgo.reset()
                self.currAlgo = None
            graph.reset()
            reset_square()

        #speedbuttons
        elif (self.buttonclick(FastButton, pos , event , "speed" )):
            self.algoSpeed = FAST
            FastButton.color = RED
            MediumButton.color = GREEN
            SlowButton.color = GREEN
        elif (self.buttonclick(MediumButton, pos , event, "speed" )):
            self.algoSpeed = MEDIUM
            FastButton.color = GREEN
            MediumButton.color = RED
            SlowButton.color = GREEN
        elif (self.buttonclick(SlowButton, pos , event, "speed" )):
            self.algoSpeed = SLOW
            FastButton.color = GREEN
            MediumButton.color = GREEN
            SlowButton.color = RED

        #algoButtons
        elif (self.buttonclick(BfsButton, pos, event )) :
            self.currAlgo = breathFirstSearch
            breathFirstSearch.stop = False
            breathFirstSearch.run(self)
            
        elif (self.buttonclick(DfsButton, pos, event)):
            self.currAlgo = depthFirstSearch
            depthFirstSearch.stop = False
            depthFirstSearch.run(self)

        elif (self.buttonclick(AStarButton, pos, event)):
            self.currAlgo = aStar
            aStar.stop = False
            aStar.run(self)
        
        #mazeButtons
        elif (self.buttonclick(RandomMazeButton, pos , event)):
            if (self.currAlgo) : self.currAlgo.reset()
            graph.drawRandomMaze()
        elif (self.buttonclick(VerticalMazeButton, pos, event)):
            if (self.currAlgo) : self.currAlgo.reset()
            graph.drawVerticalMaze()
        elif (self.buttonclick(HorizentalMazeButton, pos , event)):
            if (self.currAlgo) : self.currAlgo.reset()
            graph.drawHorizentalMaze()
            
        return self.currAlgo

        
    def commanMouseHandler(self):
        for event in pygame.event.get():
            
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()

            if(self.buttonclick(ResetButton, pos, event)) :
                if (self.currAlgo) : 
                    self.currAlgo.reset()
                    self.currAlgo = None
                graph.reset()
                reset_square()




