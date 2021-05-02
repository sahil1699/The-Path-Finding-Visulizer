import pygame

from .constants import KHAKI, GRID_WIDTH, GRID_HEIGHT,GRID_COLS,GRID_ROWS,GAP , ORANGE , WIN, PINK ,BREATH_FIRST_SEARCH, DEPTH_FIRST_SEARCH,YELLOW,BLUE,A_STAR,BLACK,GREEN,RED
from .square import start_square, end_square , Square
from .graph import graph

from .createButton import BfsButton, ResetButton, DfsButton, FastButton, SlowButton, MediumButton, AStarButton, RandomMazeButton,VerticalMazeButton,HorizentalMazeButton

btw = 120
text_size = 25
textShift = 10

class Redrawwindow :

    def __init__(self , surface ):
        self.surface = surface
        
    
    def draw(self,curr_algorithem):
        

        self.surface.fill(KHAKI)

        #drawing grid which will act as my graph 
        self.drawGrid()

        #starting square
        start_square.draw()
        #ending square
        end_square.draw()
        
        #drawing walls
        for i in range(GRID_ROWS):
            for j in range (GRID_COLS):
                if (graph.wall[i][j]) : graph.wall[i][j].draw()
        
        #drawing algorithems
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

        #MazeButtons
        RandomMazeButton.draw(self.surface, True)
        VerticalMazeButton.draw(self.surface, True)
        HorizentalMazeButton.draw(self.surface, True)

        #strating ending wall Info

        pos_x = GRID_WIDTH - ( GRID_WIDTH//2) - 280 

        pos_y = GRID_HEIGHT + 55

        startingSquare = Square(self.surface, (pos_x  , pos_y) , GREEN )
        startingSquare.draw(True)
        self.text("Starting Node" , startingSquare.x + btw , startingSquare.y + textShift , text_size )

        endingSquare = Square(self.surface, (pos_x  , pos_y + GAP + 20  ) , RED )
        endingSquare.draw(True)
        self.text("Ending Node" , endingSquare.x + btw , endingSquare.y + textShift , text_size )

        wallSquare = Square(self.surface,  (pos_x , pos_y + 2 * (GAP + 20) )  , BLACK )
        wallSquare.draw(True)
        self.text("Wall Nodes" , wallSquare.x + btw , wallSquare.y + textShift , text_size )


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

        self.algoHeading("Breath First Search guarantees the shortest path.")

        self.gernalInstructions("Visited Nodes" , "In Queue" , "Current Node")


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
        
        self.algoHeading("Depth First Search does not guarantee the shortest path.")
        self.gernalInstructions("Visited Nodes" , "Current Node")     
        

    def drawAStar(self, curr_algorithem):

        for i in range(len(curr_algorithem.open)):
            curr_algorithem.open[i].draw()
        
        for i in range(len(curr_algorithem.closed)):
            curr_algorithem.closed[i].draw()

        for i in range(len(curr_algorithem.answer)):
            curr_algorithem.answer[i].draw()
        
        self.algoHeading("A* Search guarantees the shortest path.")
        self.gernalInstructions("Closed Nodes" , "Open Nodes")


    def algoHeading(self , text ):
        
        x = GRID_WIDTH - (GRID_WIDTH//2) + 180

        y = GRID_HEIGHT + 30

        self.text(text, x, y , 30 )


    def gernalInstructions(self, blueText, yellowText , pinkText = None):
        
        

        pos_x = GRID_WIDTH - ( GRID_WIDTH//2) - 20

        pos_y = GRID_HEIGHT + 75 

        #left
        blueSquare = Square(self.surface, (pos_x, pos_y ) , BLUE )
        blueSquare.draw(True)
        self.text(blueText , blueSquare.x + btw , blueSquare.y+ textShift , text_size )

        yellowSquare = Square(self.surface, (pos_x, pos_y + GAP  + 20  ) , YELLOW )
        yellowSquare.draw(True)
        self.text(yellowText , yellowSquare.x + btw , yellowSquare.y + textShift , text_size )
        
        if (pinkText):
            pinkSquare = Square(self.surface, (pos_x , pos_y + 2 * (GAP + 20 ) - 12  ) , PINK )
            pinkSquare.draw(True)
            self.text(pinkText , pinkSquare.x + btw , pinkSquare.y + textShift , text_size )

        
       
        #right
        now_x = pos_x + GAP+ btw + 100
        orangeSquare = Square(self.surface, ( now_x , pos_y ) , ORANGE )
        orangeSquare.draw(True)
        self.text("Path Nodes" , orangeSquare.x + btw , orangeSquare.y + textShift, text_size )
        
        kahkiSquare = Square(self.surface, (now_x, pos_y + GAP + 20 ) , KHAKI )
        kahkiSquare.draw(True)
        self.text("Unvisited Nodes" , kahkiSquare.x + btw , kahkiSquare.y + textShift , text_size )

       
    
    def text(self , text , x, y , size ):
        basicfont = pygame.font.SysFont(None, size)
        text = basicfont.render(text , True, BLACK , KHAKI )
        textrect = text.get_rect()
        textrect.centerx = x 
        textrect.centery = y
        self.surface.blit(text, textrect)
