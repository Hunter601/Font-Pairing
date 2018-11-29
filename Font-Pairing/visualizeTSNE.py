import pickle
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D


data = pickle.load(open('pickles/vectorlists.pickle','rb'))

names = []
for d in data[1:]:
	names.append(d[0])

#loading the pickle
transformed = pickle.load(open('pickles/TSNE-trained.pickle', 'rb'))

xs = transformed[:,0]
ys = transformed[:,1]
zs = transformed[:,2]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xs, ys, zs, c=xs,cmap='Greens')

#for i in range(len(names)):
#	ax.text(xs[i], ys[i], zs[i], names[i], size=5, zorder=1, color='k')


ax.set_xlabel('u1')
ax.set_ylabel('u2')
ax.set_zlabel('u3')

plt.show()