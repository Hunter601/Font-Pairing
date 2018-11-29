import pickle, sys, math
import numpy as np
import queue as Q

class node(object):
	def __init__(self, i, dist):
		self.i = i
		self.dist = dist
	def __gt__(self, other):
		return self.dist > other.dist

def EuclideanDist(x1, y1, z1, x2, y2, z2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

data = pickle.load(open('pickles/vectorlists.pickle','rb'))

fonts = []
for d in data[1:]:
	fonts.append(d[0])

fonts = [f.lower() for f in fonts]

#fonts.sort()
#for f in fonts:
#	print (f)

transformed = pickle.load(open('pickles/TSNE-trained.pickle', 'rb'))

xs = transformed[:,0]
ys = transformed[:,1]
zs = transformed[:,2]

font = sys.argv[1]
font = font.lower()

idx = fonts.index(font)


distances = Q.PriorityQueue()

for i in range(len(fonts)):
	if i != idx:
		dist = EuclideanDist(xs[i],ys[i],zs[i],xs[idx],ys[idx],zs[idx])
		distances.put( node(i, dist) )

for i in range(4):
	curr = distances.get()
	print(curr.i, fonts[curr.i], curr.dist)

