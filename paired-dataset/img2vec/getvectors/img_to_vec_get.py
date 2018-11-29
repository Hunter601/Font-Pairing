import sys
import os,pickle
sys.path.append("..")  # Adds higher directory to python modules path.
from img_to_vec import Img2Vec
from PIL import Image


#input_path = './paired_images'
input_path = './fontjoy_images'

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
    #print(filename, file=open("paired-font-vectors.txt",'a'))
    #for v in vec:
    #    print(v,end=",", file=open("paired-font-vectors.txt",'a'))
    pics[filename] = vec

with open('../../../Font-Pairing/pickles/fontjoy-custom-vectors.pickle', 'wb') as f:
    pickle.dump(pics, f)