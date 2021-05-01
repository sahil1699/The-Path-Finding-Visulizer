import pygame

from .constants import GAP,GRID_HEIGHT,GRID_WIDTH,RED,GREEN,BLACK,WIN,OTHER_SQUARE,START_SQUARE,END_SQUARE,BROWN


class Square:
    
    def __init__(self,surface,pos,color = BLACK , square_type = OTHER_SQUARE ):
        self.surface = surface
        self.x , self.y = pos
        self.color  = color
        self.backToSquare()
        self.row = self.x//GAP
        self.col = self.y//GAP
        self.square_type = square_type

    def draw(self, outline = False):
        
            if self.square_type != START_SQUARE and self.square_type != END_SQUARE and start_square.x == self.x and start_square.y == self.y:
                pass
            else:
                if outline:
                    pygame.draw.rect(self.surface,BROWN,(self.x ,self.y ,GAP + 1 ,GAP + 1 ))

                pygame.draw.rect(self.surface,self.color,(self.x + 1,self.y + 1,GAP -1 ,GAP -1 ))
                

    

    def collidepoint(self,pos):
        mouse_x , mouse_y = pos
        return self.x  <= mouse_x and self.x + GAP  >= mouse_x and self.y <= mouse_y and self.y + GAP >= mouse_y

    def backToSquare(self):
        self.x = self.x - (self.x % GAP)
        self.y = self.y - (self.y % GAP)
        self.row = self.x//GAP
        self.col = self.y//GAP
        



start_pos_default = (GRID_WIDTH//8 , GRID_HEIGHT//2)
end_pos_default = (GRID_WIDTH -  GRID_WIDTH//8 , GRID_HEIGHT//2)

start_square = Square(WIN, start_pos_default, GREEN , START_SQUARE)
end_square = Square(WIN, end_pos_default , RED , END_SQUARE )

def reset_square():
    start_square.x , start_square.y = start_pos_default
    end_square.x , end_square.y = end_pos_default

    start_square.backToSquare()
    end_square.backToSquare()

    start_square.row , start_square.col =  start_square.x//GAP , start_square.y//GAP
    end_square.row , end_square.col = end_square.x//GAP, end_square.y//GAP

    start_square.color = GREEN
    end_square.color = RED

    