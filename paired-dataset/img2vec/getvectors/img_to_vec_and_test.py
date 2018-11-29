import sys
import os
sys.path.append("..")  # Adds higher directory to python modules path.
from img_to_vec import Img2Vec
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity


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
    print(filename, file=open("fontjoy-font-vectors.txt",'a'))
    for v in vec:
        print(v,end=",", file=open("fontjoy-font-vectors.txt",'a'))
    pics[filename] = vec

pic_name = ""
while pic_name != "exit":
    pic_name = str(input("Which filename would you like similarities for?\n"))

    try:
        sims = {}
        for key in list(pics.keys()):
            if key == pic_name:
                continue

            pics[pic_name] = temp
            sims[key] = cosine_similarity(pics[pic_name].reshape((1, -1)), pics[key].reshape((1, -1)))[0][0]

        d_view = [(v, k) for k, v in sims.items()]
        d_view.sort(reverse=True)
        for v, k in d_view:
            print(v, k)

    except KeyError as e:
        print('Could not find filename %s' % e)

    except Exception as e:
        print(e)