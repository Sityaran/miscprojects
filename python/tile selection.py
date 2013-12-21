import pygame, sys, math    
from pygame.locals import *

pygame.init()

# basic values
wx, wy = 256,256
mx, my = 0,0
tilesize = 16
tilesizeexact = 16.0
tiles = []

#pygame values and inits
windowSurfaceObj = pygame.display.set_mode((wx,wy))
pygame.display.set_caption('Tile Selection')
grey = pygame.Color(125,125,125)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

#make tile array. for ref: 0 = unselected, 1 = selected, 2 = highlighted ??
for x in range(0,wx,tilesize):
		tiles.append([])
		for y in xrange(0,wy,tilesize):
			tiles[x/tilesize].append(0) # append (x,y) for top-left x,y coords
			
#main program
while True:
	windowSurfaceObj.fill(black)

	mx, my = pygame.mouse.get_pos() # mouse position
	mxr, mxy = int(math.floor(mx/tilesizeexact)), int(math.floor(my/tilesizeexact))
	
	a = tilesize
	xn = mxr*tilesize
	yn = mxy*tilesize
	for x in xrange(tilesize):
		for y in xrange(tilesize):
			if tiles[x][y] == 1:
				pygame.draw.rect(windowSurfaceObj, white, Rect((x*a,y*a),(a,a)))
			else:
				continue
				
	pygame.draw.rect(windowSurfaceObj, grey, Rect((xn,yn),(a,a)))
	 
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
		elif event.type == MOUSEBUTTONDOWN: #when you click, check if tile is highlighted
			if tiles[mxr][mxy] == 0:
				tiles[mxr][mxy] = 1
			else:
				tiles[mxr][mxy] = 0
	pygame.display.update()