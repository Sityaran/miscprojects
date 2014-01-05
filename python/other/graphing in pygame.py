import pygame, sys, math    
from pygame.locals import *

pygame.init()
#fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame graphing like wow')

#catSurfaceObj = pygame.image.load('cat.png')
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
#mousex, mousey = 0,0
center = (640/2),(480/2)
n = 0
#fontObj = pygame.font.Font('freesansbold.ttf', 16)
#msg = 'Look ma im graphin'

while True:
    windowSurfaceObj.fill(whiteColor)
    
    ##### all of the following is redundant example code for pygame
    
    #pygame.draw.circle(windowSurfaceObj, blueColor,(center),20,0)
    #windowSurfaceObj.blit(catSurfaceObj, (mousex,mousey))
    #msgSurfaceObj = fontObj.render(msg,False,blueColor)
    #msgRectobj = msgSurfaceObj.get_rect()
    #msgRectobj.topleft = (10,20)
    #windowSurfaceObj.blit(msgSurfaceObj,msgRectobj)

    #####

    #make our x and y coords
    pygame.draw.line(windowSurfaceObj, blueColor, (center[0]-320,center[1]), (center[0]+320,center[1]), 1)
    pygame.draw.line(windowSurfaceObj, blueColor, (center[0],center[1]-240), (center[0],center[1]+240), 1)

    n += 1 #like a time function
    
    #make graph array
    graph = pygame.PixelArray(windowSurfaceObj)

    ymax = 4*math.pi #by default this will be 2pi
    scale = 170 #just something that will make viewing graph easier
    timescale = .1*n #relatively slow graph over time
    d = 0
    
    for x in range(0,640):
            #want 640 to be 0 to 2pi so, assuming pi3.14
            # x*640 = 2pi -> x = 2pi/640 so
            xs = (x-320)*ymax/640
            ys = int(scale*math.sin(xs)) #the function
            
            y = (240-ys) #so 0,0 actually plots at center of screen
            #the actual value used in displaying the graph of the function is y (and x, of course)
            
            #printing the x,y coord to the array to be shown on screen
            for i in range(-1,2):
                graph[x][y+i] = redColor

            if (x*ymax/640.0) == d:
                for m in range(-25,26):
                    graph[x][y+m] = greenColor
                d += math.pi/4.0
            print (x*ymax/640.0),d

    del graph

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    
