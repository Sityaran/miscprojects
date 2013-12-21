# Copyright (c) 2011 Brian Gordon
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import random, heapq, argparse

class undirected_graph(dict):
	"""A dictionary of unordered pairs."""
	def __setitem__(self, key, value):
		super(undirected_graph, self).__setitem__(tuple(sorted(key)), value)

	def __getitem__(self, key):
		return super(undirected_graph, self).__getitem__(tuple(sorted(key)))

	def __has_key__(self, key):
		return super(undirected_graph, self).__has_key__(tuple(sorted(key)))

def grid_adjacent(vertex):
	"""Return all grid vertices adjacent to the given point."""
	x, y = vertex
	adj = []

	if x > 0:
		adj.append((x-1, y))
	if x < GRID_WIDTH-1:
		adj.append((x+1, y))
	if y > 0:
		adj.append((x, y-1))
	if y < GRID_HEIGHT-1:
		adj.append((x, y+1))

	return adj

def make_grid():
	weights = undirected_graph()
	for x in xrange(GRID_WIDTH):
		for y in xrange(GRID_HEIGHT):
			vertex = (x,y)
			for neighbor in grid_adjacent(vertex):
				weights[(vertex,neighbor)] = random.random()

	return weights

def MCST():
	spanning = undirected_graph()
	weights = make_grid()

	closed = set([(0,0)])
	heap = []
	for neighbor in grid_adjacent((0,0)):
		cost = weights[(0,0),neighbor]
		heapq.heappush(heap, (cost, (0,0), neighbor))

	while heap:
		cost, v1, v2 = heapq.heappop(heap)

		# v1 is the vertex already in the spanning tree
		# it's possible that we've already added v2 to the spanning tree
		if v2 in closed:
			continue

		# add v2 to the closed set
		closed.add(v2)

		# add v2's neighbors to the heap
		for neighbor in grid_adjacent(v2):
			if neighbor not in closed:
				cost = weights[v2, neighbor]
				heapq.heappush(heap, (cost, v2, neighbor))

		# update the spanning tree
		spanning[(v1,v2)] = True

	return draw_tree(spanning)

def RDM():
	spanning = undirected_graph()

	closed = set([(0,0)])
	neighbors = [((0,0), x) for x in grid_adjacent((0,0))]

	while neighbors:
		v1, v2 = neighbors.pop(random.randrange(len(neighbors)))

		# v1 is the vertex already in the spanning tree
		# it's possible that we've already added v2 to the spanning tree
		if v2 in closed:
			continue

		# add v2 to the closed set
		closed.add(v2)

		for neighbor in grid_adjacent(v2):
			if neighbor not in closed:
				neighbors.append((v2, neighbor))

		# update the spanning tree
		spanning[(v1,v2)] = True

	return draw_tree(spanning)

def draw_tree(spanning):
	# Create a big array of 0s and 1s for pypng

	pixels = []
	mazec = u'\u2592' #passages
	wallc = u'\u2588' #anything that isnt a passage or a cell
	borderc = u'\u2593' #basically a wall, but are added manually
	cellc = u'\u2592' #the actual cells (vertexes) that the algorithm bases everything off of
	noncellc = u'\u2580' #a tile that can never be a passage or a cell (because it is overlooked for the algorithm to work
	# Add a row of off pixels for the top
	pixels.append([borderc ] + ["S"] + ([borderc ] * (img_width-2)))

	for y in xrange(GRID_HEIGHT):
		# Row containing nodes
		row = [borderc] # First column is off
		for x in xrange(GRID_WIDTH):
			row.append(cellc)
			if x < GRID_WIDTH-1:
				if int(((x,y),(x+1,y)) in spanning):
					row.append(mazec)
				else:
					row.append(wallc)
		row.append(borderc)
		pixels.append(row)

		if y < GRID_HEIGHT-1:
			# Row containing vertical connections between nodes
			row = [borderc] # First column is off
			for x in xrange(GRID_WIDTH):
				if int(((x,y),(x,y+1)) in spanning):
					row.append(mazec)
				else:
					row.append(wallc)
				if x < GRID_WIDTH-1:
					row.append(noncellc)
				else:
					row.append(borderc)
			pixels.append(row)

	# Add a row of off pixels for the bottom
	pixels.append(([borderc] * (img_width-2)) + ["E"] + [borderc])

	return pixels

# Handle arguments



GRID_WIDTH, GRID_HEIGHT = 15,10

img_width = GRID_WIDTH * 2 + 1
img_height = GRID_HEIGHT * 2 + 1

mazesddd = MCST()
print
for i in xrange(len(mazesddd)):
	string = ""
	string += " "
	for n in xrange(len(mazesddd[i])):
		string += mazesddd[i][n]
	print string


raw_input()
