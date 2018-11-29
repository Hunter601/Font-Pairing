import pickle
import plotly
import plotly.graph_objs as go
import numpy as np


data = pickle.load(open('pickles/vectorlists.pickle','rb'))

names = []
for d in data[1:]:
	names.append(d[0])

#loading the pickle
transformed = pickle.load(open('pickles/TSNE-trained.pickle', 'rb'))

xs = transformed[:,0]
ys = transformed[:,1]
zs = transformed[:,2]


plot1 = go.Scatter3d(
	x=xs,
	y=ys,
	z=zs,
	name = "TSNE-plot",
	hovertext = names,
	mode='markers',
	marker=dict(
		size=4,
		color = ys,
		colorscale='Electric',
		opacity=0.97
	)
)

data = [plot1]

layout = go.Layout(
	margin=dict(
		l=0,
		r=0,
		b=0,
		t=0
	)
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='TSNE-plot.html')