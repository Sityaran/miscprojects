import random

dims = 10,10
maze = []

walls = [(x,y,x+1,y)
	for x in range(dims[0]-1)
	for y in range(dims[1])]
walls.extend([(x,y,x,y+1)
	for x in range(dims[0])
	for y in range(dims[1]-1)])

cell_sets = [set([(x,y)])
	for x in range(dims[0])
	for y in range(dims[1])]

# shitty weighting
walls_copy = walls[:]
random.shuffle(walls_copy)

#some bullshit (aka the algorithim) (NOT WORKING AS INTENDED)
for wall in walls_copy:
	set_a = None
	set_b = None
	
	for s in cell_sets:
		if (wall[0], wall[1]) in s:
			set_a = s
		if (wall[2], wall[3]) in s:
			set_b = s
	if set_a is not set_b:
		cell_sets.remove(set_a)
		cell_sets.remove(set_b)
		cell_sets.append(set_a.union(set_b))
		walls.remove(wall)
		
		
# printing to maze (WORKS AS INTENDED)
maze.append(['_'] + [1] + (['_'] * (dims[0]*2-1)))

for x in xrange(dims[0]):
	row = ['_']
	for y in xrange(dims[1]):
		row.append('.')
		if y < dims[1]-1:
			if int( (x,y,x,y+1) in walls ):
				row.append(".")
			else:
				row.append('_')
	row.append('_')
	maze.append(row)

	
	if x < dims[0]-1:
		for y in xrange(dims[1]):
			if int( (x,y,x+1,y) in walls ):
				row.append(".")
			else:
				row.append('_')
			row.append('_')
		maze.append(row)


maze.append((['_'] * (dims[0]*2-1)) + [2] + ['_'] )
	
		



for x in xrange(dims[0]*2+1):
	for y in xrange(dims[1]*2+1):
		print maze[x][y],
	print
raw_input()