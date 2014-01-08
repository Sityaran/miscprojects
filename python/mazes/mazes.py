import pygame, sys, math
from pygame.locals import *
from random import randrange
pygame.init()

def makegrid(width,height):
	world= 3
	maze= 0
	cell= maze 	
	# change cell to be maze when you actually do the algorithm, 
	# because you ll mark cells that are opposites of created cells,
	# which will never be passages

	grid=[]
	grid.append([world]*width*2 + [world]) # top border
	for y in range(0,height):
		grid.append([world] + [cell,maze]*((width-1)) + [cell,world])
		if y<height-1:
			grid.append([world] + [maze,world]*width)
	grid.append([world]*width*2 + [world]) # bottom border
	return grid

def checkadjacents(grid,x,y):
	wall = []
	for i in [-1,1]:
		if not(grid[y+i][x]):
			wall.append((x,y+i,x,y+i+i))
		if not(grid[y][x+i]):
			wall.append((x+i,y,x+i+i,y))
	return wall
	

width = int(raw_input("width: "))
height = int(raw_input("height: "))

#prims
grid = makegrid(width,height)
walls = [] # each tuple in walls should be (x,y,xo,yo) where xo and yo are the opposite cell coords
for i in checkadjacents(grid,1,1):
	walls.append(i)
grid[1][1] = 1

#pygame
windowSurfaceObj = pygame.display.set_mode((width*2 + 1,height*2 +1))
pygame.display.set_caption('Mazes')
grey = pygame.Color(125,125,125)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)

# # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # 

while True:
	graph = pygame.PixelArray(windowSurfaceObj)
	graph[1][1] = white
#	for i in range(len(grid)):
#		for n in range(len(grid[i])):
#			if grid[i][n] == 1:
#				graph[i][n] = white

		
	if len(walls)>0:

		currentwall = walls[randrange(len(walls))]
		
		if not(grid[currentwall[3]][currentwall[2]]):
			grid[currentwall[1]][currentwall[0]] = 1
			grid[currentwall[3]][currentwall[2]] = 1	
			graph[currentwall[1]][currentwall[0]] = white
			graph[currentwall[3]][currentwall[2]] = white
			walls.remove(currentwall)
			for i in checkadjacents(grid,currentwall[2],currentwall[3]):
				walls.append(i)
		else:
			grid[currentwall[1]][currentwall[0]] = 3
			walls.remove(currentwall)

	# simple conversion and printing function
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
	if not(len(walls)):
		break
	pygame.display.update()
for i in range(len(graph)):
	s = ""
	for n in range(len(graph[i])):
		if graph[i][n] > 1:
			s += ' ' 
		else:
			s += '$'
	print s
raw_input()
			