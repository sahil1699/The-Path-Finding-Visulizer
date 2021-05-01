import pygame 

from Visualizer.constants import WIDTH, HEIGHT,WIN,GRID_HEIGHT,GRID_WIDTH

from Visualizer.mouseHandler import MouseHandler

from Visualizer.redrawwindow import Redrawwindow

FPS = 100

pygame.display.set_caption("Path Finding Visulizer")


mouseHandler = MouseHandler(WIN)
redrawwindow = Redrawwindow(WIN)



def main():
    
    run = True
    clock = pygame.time.Clock()
    
    currAlgo = None

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            pos = pygame.mouse.get_pos()
            mouse_x , mouse_y = pos
            if mouse_x <= GRID_WIDTH and mouse_y <= GRID_HEIGHT : 
                mouseHandler.mouseDrag(event)
            else :
               currAlgo = mouseHandler.checkButtonClick(event, pos )
            
            
        redrawwindow.draw(currAlgo)

    pygame.quit()


if __name__ == "__main__":
    main()