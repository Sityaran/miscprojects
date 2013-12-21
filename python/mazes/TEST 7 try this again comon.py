# do it with this

def makegrid():
	grid =[]

	for x in range(0,dx):
		if x < dx-1:
			grid.append([0]*(rdx))
			
			grid.append([0,3]*dx)
			
		else:
			grid.append([0]*(rdx))
	
	return grid

#TODO : add borders, makes neighbor checking easier