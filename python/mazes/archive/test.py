from math import *
from random import randrange
maxdim = 10,10

#checking diagonals
def checkcells(checkmat,x,y):
	dia = 0
	for x2 in range(-1,2):
		for y2 in range(-1,2):
			#diagonals
			if (x2==y2 or (-1*x2)==y2 or x2==(-1*y2)) and (x2!=0 and y2!=0):
				if checkmat[x+x2][y+y2] == 1:
					dia += 1
			else:
				dia += 0

def prims():
	# makes the 2d array to hold everything in
	# could be changed to, generate mat elsewhere, ask prims() to take a [] argument so like def prims(mat):

	mat = []
	check = []
	for x in range(0,maxdim[0]):
		mat.append([])
		check.append([])
		for y in range(0,maxdim[1]):
			if x==0 or x==maxdim[0]-1:
				# for check 0 = a wall, 1 = not a wall
				check[x].append(1)
			elif y==0 or y==maxdim[1]-1:
				check[x].append(1)
			else:
				# for mat 0 = wall, 1= maze
				check[x].append(0)
			mat[x].append(0)

	# check + algorithm

	for x in range(1,maxdim[0]-2):
		for y in range(1,maxdim[1]-2):
			if check[x][y] == 0:
				if checkcells(check,x,y) < 1:
					mat[x][y] =1
					check[x][y] = 1

					check3 = ((check[x+1][y], x+1, y), (check[x-1][y], x-1, y), (check[x][y+1], x, y+1), (check[x][y-1], x, y-1))
					for c in range(0,4):
						if check3[c][0] ==  0:
							x3 = check3[c][1]
							y3 = check3[c][2]
							if (checkcells(check,x3,y3) < 1) and (randrange(0,2) == 1) and (check[x][y] != 1):
								mat[x3][y3] = 1
						check[x3][y3] = 1

	for x in range(0,len(mat)):
		print mat[x], "\n"



