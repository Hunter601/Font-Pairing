import json, pickle
import pandas as pd

with open('fonts-vectors200.json', encoding = 'utf-8') as f:
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

# print in form of list of lists
#print (data)

attr = []
attr.append('name')

for i in range(1,201) :
	attr.append('attribute ' + str(i))

data = [attr] + data

with open('pickles/vectorlists.pickle', 'wb') as f:
	pickle.dump(data, f)

#in form of pandas dataframe
df = pd.DataFrame(data)

with open('pickles/vectordataframe.pickle', 'wb') as f:
	pickle.dump(data, f)