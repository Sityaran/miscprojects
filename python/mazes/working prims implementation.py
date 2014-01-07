# do it with this
from random import randrange
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
	
# # # # # # # # # # # #
# first things first  #
# # # # # # # # # # # #

# set dims
width = int(raw_input("width: "))
height = int(raw_input("height: "))

# initialization
grid = makegrid(width,height)
walls = [] # each tuple in walls should be (x,y,xo,yo) where xo and yo are the opposite cell coords
for i in checkadjacents(grid,1,1):
	walls.append(i)

#prims loop
while len(walls)>0:
	currentwall = walls[randrange(len(walls))]
	if not(grid[currentwall[3]][currentwall[2]]):
		grid[currentwall[1]][currentwall[0]] = 1
		grid[currentwall[3]][currentwall[2]] = 1
		walls.remove(currentwall)
		for i in checkadjacents(grid,currentwall[2],currentwall[3]):
			walls.append(i)
	else:
		grid[currentwall[1]][currentwall[0]] = 3
		walls.remove(currentwall)
			
# simple conversion and printing function

for i in range(len(grid)):
	string = ""
	for n in range(len(grid[i])):
		if (i,n) == (1,1):
			string += 'S'
		elif (i,n) == (len(grid)-2,len(grid[i])-2):
			string += 'E'
		elif grid[i][n] == 3:
			string += u'\u2593'
		elif grid[i][n] == 1:
			string += ' '
	print string

raw_input()

#now all you need to do is find a starting cell, check adjacents, check if opposites
#if opposite is found, add to a cell list, then randomly pick a cell from the list, repeat
#once a cell does not have any more opposites that can be made, name it part of the maze, make the adjacent passages that cant be made into world tiles
# best to use a list like 
#	potential maze tile = 0
#	cell tile = 1
#	permanent maze tile = 2
#	wall/world tile = 3 (this will only be for passages that cant become apart of the maze(2), borders, and parts of the array irrelevant to the algorithm)

