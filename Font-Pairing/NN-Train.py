import json, pickle
import pandas as pd
import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense
from sklearn.model_selection import train_test_split

data = pickle.load(open('pickles/NN-traindata.pickle', 'rb'))

x = data[0]
y = data[1]


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2) 

x_train = np.asarray(x_train, dtype= 'float')
y_train = np.asarray(y_train, dtype= 'float')

x_test = np.asarray(x_test, dtype= 'float')
y_test = np.asarray(y_test, dtype= 'float')

print (x_train.shape)
print (y_train.shape)

model = Sequential()
model.add(Dense(100, input_dim=512, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(512, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='SGD', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=400)
scores = model.evaluate(x_test, y_test)
print ("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


pickle.dump(model,open('pickles/trained-NN-model.pickle','wb'))
