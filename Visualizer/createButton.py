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
buttonPos_y = 10

BfsButton = Button(GREEN ,  buttonPos_x  , buttonPos_y , BUTTON_WIDTH, BUTTON_HEIGHT , BREATH_FIRST_SEARCH ) #creates a button

DfsButton = Button(GREEN , buttonPos_x , buttonPos_y + BUTTON_HEIGHT + 10 , BUTTON_WIDTH , BUTTON_HEIGHT , DEPTH_FIRST_SEARCH )

AStarButton = Button(GREEN , buttonPos_x , buttonPos_y + 2 * ( BUTTON_HEIGHT + 10) , BUTTON_WIDTH , BUTTON_HEIGHT , A_STAR )

#speed buttons
speed_button_pos_y = GRID_HEIGHT + 20

FastButton = Button(RED ,  20  , speed_button_pos_y  , BUTTON_WIDTH -20  , BUTTON_HEIGHT - 20, "Fast" ) 
MediumButton = Button(GREEN ,  20  , speed_button_pos_y  + BUTTON_HEIGHT , BUTTON_WIDTH -20  , BUTTON_HEIGHT - 20, "Medium" ) 
SlowButton = Button(GREEN, 20  , speed_button_pos_y + 2 * BUTTON_HEIGHT , BUTTON_WIDTH -20  , BUTTON_HEIGHT - 20, "Slow" ) 


##reset button
buttonPos_reset_y = HEIGHT - BUTTON_HEIGHT -10

ResetButton = Button(GREEN, buttonPos_x, buttonPos_reset_y, BUTTON_WIDTH , BUTTON_HEIGHT, "Reset and Stop"  )