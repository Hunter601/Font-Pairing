import csv, sys, os, pickle
sys.path.append("..")  # Adds higher directory to python modules path.
from img_to_vec import Img2Vec
from PIL import Image


input_path = './paired_images'

img2vec = Img2Vec()

# For each test image, we store the filename and vector as key, value in a dictionary
pics = {}
for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    if(filename == '.DS_Store'):
        continue
    img = Image.open(os.path.join(input_path, filename))
    img = img.convert('RGB')
    vec = img2vec.get_vec(img)

    filename = filename.replace(" ","-")
    pics[filename] = vec

NNdata = [[],[]]

with open('paired-fonts-dataset.csv') as d2:
    reader = csv.reader(d2, delimiter=',')
    for row in reader:
    	NNdata[0].append( pics[row[0]+'.png'] )
    	NNdata[1].append( pics[row[1]+'.png'] )


with open('../../../Font-Pairing/pickles/NN-traindata.pickle', 'wb') as f:
    pickle.dump(NNdata, f)
