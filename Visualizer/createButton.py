import pygame

from .constants import BREATH_FIRST_SEARCH, GREEN , BUTTON_HEIGHT , BUTTON_WIDTH , WIDTH , HEIGHT ,DEPTH_FIRST_SEARCH , GRID_HEIGHT,RED,A_STAR

class Button():
    def __init__(self,color,x,y,width,height,text = ''):

        self.color = color
        self.x = x
        self.y = y
        self.width  = width
        self.height = height
        self.text = text

    def draw(self,win,outline = None):

        if outline:
            pygame.draw.rect(win,outline, (self.x-2,self.y -2,self.width-4,self.height),0)

        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)


        if self.text != '':
            pygame.init()
            font = pygame.font.SysFont('comicsans',30)
            text = font.render(self.text,1,(0,0,0))
            win.blit(text,(self.x + (self.width/2 - text.get_width()/2),self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self,pos):

        if pos[0] > self.x and pos[0] < self.x  + self.width :
            if pos[1] > self.y  and pos[1] < self.y  + self.height:
                return True
        return False



# algo buttons 

buttonPos_x =  WIDTH - BUTTON_WIDTH - 10
algo_buttonPos_y = 30

BfsButton = Button(GREEN ,  buttonPos_x  , algo_buttonPos_y , BUTTON_WIDTH, BUTTON_HEIGHT , BREATH_FIRST_SEARCH ) 
DfsButton = Button(GREEN , buttonPos_x , algo_buttonPos_y + BUTTON_HEIGHT + 10 , BUTTON_WIDTH , BUTTON_HEIGHT , DEPTH_FIRST_SEARCH )
AStarButton = Button(GREEN , buttonPos_x , algo_buttonPos_y + 2 * ( BUTTON_HEIGHT + 10) , BUTTON_WIDTH , BUTTON_HEIGHT , A_STAR )


##reset button
reset_buttonPos_y = HEIGHT - BUTTON_HEIGHT - 30

ResetButton = Button(GREEN, buttonPos_x, reset_buttonPos_y, BUTTON_WIDTH , BUTTON_HEIGHT, "Reset and Stop"  )

#Maze buttons
Maze_buttonPos_y = reset_buttonPos_y - BUTTON_HEIGHT - 100

RandomMazeButton = Button(GREEN ,  buttonPos_x  , Maze_buttonPos_y , BUTTON_WIDTH, BUTTON_HEIGHT , "Random Maze") 
VerticalMazeButton = Button(GREEN ,  buttonPos_x  , Maze_buttonPos_y - BUTTON_HEIGHT - 10 , BUTTON_WIDTH, BUTTON_HEIGHT , "Vertical Maze") 
HorizentalMazeButton = Button(GREEN ,  buttonPos_x  , Maze_buttonPos_y - 2 * (  BUTTON_HEIGHT +  10)   , BUTTON_WIDTH, BUTTON_HEIGHT , "Horizental Maze") 

#speed buttons
speed_buttonPos_y = GRID_HEIGHT + 20

FastButton = Button(RED ,  20  , speed_buttonPos_y  , BUTTON_WIDTH -20  , BUTTON_HEIGHT - 20, "Fast Speed" ) 
MediumButton = Button(GREEN ,  20  , speed_buttonPos_y  + BUTTON_HEIGHT , BUTTON_WIDTH -20  , BUTTON_HEIGHT - 20, "Medium Speed" ) 
SlowButton = Button(GREEN, 20  , speed_buttonPos_y + 2 * BUTTON_HEIGHT , BUTTON_WIDTH -20  , BUTTON_HEIGHT - 20, "Slow Speed" ) 
