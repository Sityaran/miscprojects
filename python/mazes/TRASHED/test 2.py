from random import randrange
import sys
maxdim = 20,20
mat = []
adjpos = []

#for the purposes of this learning, 0 = wall, 1 = maze, 2 = adjacent to maze, 3 = permawall
def gridp(grid):
	for x in range(0,len(grid)):
		print grid[x], "\n"
		
def gg(matte):

	grid = matte

	#create grid
	for x in range(0,maxdim[0]):
		grid.append([])
		for y in range(0,maxdim[1]):
			if (x==0) or (x==maxdim[0]-1):
				grid[x].append(3)
			elif (y==0) or (y==maxdim[1]-1):
				grid[x].append(3)
			else:
				grid[x].append(0)

	# determine starting position
	currentcell = 0,0
	while True:
		start = randrange(1,4), randrange(1,4)
		if (start[0] != 1) and (start[1] != 1):
			grid[start[0]][start[1]] = 1
			currentcell = start[0],start[1]
			break
	
	#adding to maze
	while True:
		breakit = 0
		
		#mark adjacents
		for x in range(-1,2):
			for y in range (-1,2):
				checkit = grid[currentcell[0]+x][currentcell[1]+y] 
				if (x==0 and y==0) or (x!=0 and y!=0): #avoid current cell and diagonals
					continue
				elif checkit == 1 or checkit == 3 :
					continue
				else:
					grid[currentcell[0]+x][currentcell[1]+y] = 2
					adjpos.append((currentcell[0]+x,currentcell[1]+y))	

		#check frontiers
		for x in range(1,maxdim[0]-1):
			if 2 in grid[x]:
				breakit += 1 #no more adjacents
			else:
				continue
		
		if breakit == 0:
			break
		#change current cell
		while True:
			pos = randrange(0,len(adjpos))
			currentcell = adjpos[pos]
			grid[currentcell[0]][currentcell[1]] = 1
			adjpos.remove(adjpos[pos])
			break
			
		
	gridp(grid)



gg(mat)

raw_input("GG")