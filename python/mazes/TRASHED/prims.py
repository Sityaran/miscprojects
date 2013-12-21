import random

#create initial grid 0 = unadded wall, 1 = maze, 2 = added 3 = not maze, 4 = passage, 5 = full passage
dx,dy = 10,10
rdx, rdy = dx*2-1,dy*2-1
walls = []
cells = []
first = 0

def makegrid():
	grid =[]

	for x in range(0,dx):
		if x < dx-1:
			grid.append([0]*(rdx))
			
			grid.append([0,3]*dx)
			
		else:
			grid.append([0]*(rdx))
	
	return grid

# def makespacedgrid(): #CHANGE THIS LATER, this incase, after prims and walls you need to space out the cells (so you actually have walls inbetween) (refer to test 3.py for more info)
	# grid =[]

	# grid.append( [3]*(dx*2+2) ) #outer border

	# for x in range(1,dx*2+1):
		# grid.append([])
		# grid[x].append(3) #outer border
		# for y in range(0,dy*2):
			# grid[x].append(0)
		# grid[x].append(3) #outer border
			
	# grid.append( [3]*(dx*2+2) ) #outer border
	
	# return grid

def checkwalls(grid, cell): #adding walls to the list (ONLY FOR ADDING UNADDED)
	for x in range(-1,2):
		for y in range(-1,2):
			if (x != y) and (-1*x != y) and (x != -1*y):
			#apparently list[0-1] is like list[maxlen] ?? like wtf
				if (cell[0]+x != -1) and (cell[1]+y != -1) and (grid[cell[0]+x][cell[1]+y] == 0): 
					walls.append((cell[0]+x,cell[1]+y))
					if x == 0:
						cells.append((cell[0],cell[1]+y+1))
					else:
						cells.append((cell[0]+x+1,cell[1]))
					cells.append((cell[0],cell[1]))
					grid[cell[0]+x][cell[1]+y] = 4
					
					
def ranadjwall(grid, cell): #adding walls to the list (ONLY FOR ADDING UNADDED)
	while True:
		select = random.randrange(0,4)
		
		# 0 = x+1, 1 = y+1, 2 = x-1, 3 = y-1
		# OH GOD DONT LOOK AT THIS
		if neighborsfull(grid, cell) == 4:
			grid[cell[0]][cell[1]] = 5
			return 0
			break
		else:
			if select == 0:
				if (cell[0]+1 < rdx) and (maze[cell[0]+1][cell[1]] == 4):
					return cell[0]+1,cell[1],2,0 #by adding the last two values, i get the direct opposite cell coords with each return
					break
				
			elif select == 1:
				if (cell[1]+1 < rdy) and (maze[cell[0]][cell[1]+1]  == 4):
					return cell[0],cell[1]+1,0,2
					break
				
			elif select == 2:
				if (cell[0]-1 != -1) and (maze[cell[0]-1][cell[1]] == 4):
					return cell[0]-1,cell[1],-2,0
					break
				
			elif select == 3:
				if (cell[1]-1 != -1) and (maze[cell[0]][cell[1]-1]== 4):
					return cell[0],cell[1]-1,0,-2
					break
					
def neighborsfull(grid, cell):
	neighbors = 0
	
	if (cell[0]+1 < rdx) and (maze[cell[0]+1][cell[1]] == 1):
		neighbors += 1
	if (cell[0]+1 < rdy) and (maze[cell[0]][cell[1]+1]  == 1):
		neighbors += 1
	if (cell[0]-1 != -1) and (maze[cell[0]-1][cell[1]] == 1):
		neighbors += 1
	if (cell[1]-1 != -1) and (maze[cell[0]][cell[1]-1]== 1):
		neighbors += 1
		
	return neighbors
		

# initializing
maze = makegrid()
sx, sy = 0,0
maze[sx][sy] = 1
checkwalls(maze, (sx,sy))
currentcell = sx, sy


for i in xrange(rdx):
	print maze[i], "\n"
raw_input()

while walls: #while walls has frontier coords added
	
	#THE ACTUAL ALGORITHIM
	# 1. start with a grid full of walls CHECK
	# 2. pick a cell, mark it as part of the maze, add the walls to the wall list CHECK
	# 3. whil there are walls in the list: 
	ranwall = ranadjwall(maze, currentcell) #pick a random wall from the list
	if ranwall != 0:
		cwall, op = (ranwall[0],ranwall[1]), maze[ranwall[2]][ranwall[3]]
		if op != 1:
			maze[ranwall[0]][ranwall[1]] = 4
			checkwalls(maze, cwall)
		print walls
		raw_input()
		walls.remove((ranwall[0],ranwall[1])) #removes checked wall

	cells.remove(currentcell)
	currentcell = cells[random.randrange(len(cells))]
	print
	for i in xrange(rdx):
		print maze[i], "\n"


raw_input()