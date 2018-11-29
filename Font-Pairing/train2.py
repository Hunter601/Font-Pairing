import json
import pandas as pd
import numpy as np


with open('fonts-vectors200.json') as f:
	x = json.loads(f.read())


x = x['items']

data = []

for item in x :

	variants =  item['variants']

	i = 0 
	for vec in item['vectors'] :
		temp = [item['family']+' '+variants[i]] + vec
		data.append(temp)
		i = i+1

# in form of list of lists
#print (data)

attr = []
attr.append('name')

for i in range(1,201) :
	attr.append('attribute ' + str(i))

data = [attr] + data
#print (data)

df = pd.DataFrame(data)

x_train = []
y_train = []
import csv

with open('vectors.csv') as d2:
    spamreader = csv.reader(d2, delimiter=',')
    for row in spamreader:
        temp = np.array(df[df[0] == row[0]])
        tempx = []
        for i in range(1,201):
            tempx.append(float(temp[0][i]))

        x_train.append(tempx)

        temp = np.array(df[df[0] == row[1]])
        tempy = []
        for i in range(1,201):
            tempy.append(float(temp[0][i]))

        y_train.append(tempy)


x_train = np.asarray(x_train, dtype= 'float')
y_train = np.asarray(y_train, dtype= 'float')
print(x_train.shape)
print(y_train.shape)
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(100, input_dim=200, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(200, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer='SGD', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=400)
scores = model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))