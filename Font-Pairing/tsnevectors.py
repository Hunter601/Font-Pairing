import pickle
from sklearn.manifold import TSNE


data = pickle.load(open('pickles/vectorlists.pickle', 'rb'))
data = data[1:]

for i in range(len(data)):
	data[i] = data[i][1:]

model = TSNE(learning_rate = 100, n_components = 3, n_iter=2000)
transformed = model.fit_transform(data)

#saving in pickle
with open('pickles/TSNE-trained.pickle', 'wb') as f:
	pickle.dump(transformed, f)

print ("Dataset trained for TSNE model")