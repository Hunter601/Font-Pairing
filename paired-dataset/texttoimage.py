from PIL import Image, ImageDraw, ImageFont
import os

filenames = next(os.walk('/Users/iprakhar22/Desktop/MinorVSem/dataset/font-ttfs/'))[2]
filenames = filenames[1:]

for f in filenames:

	img = Image.new('RGB', (224, 224), color = 'white')

	if f == 'Pacifico.ttf':
		fnt = ImageFont.truetype('/Users/iprakhar22/Desktop/MinorVSem/dataset/font-ttfs/' + f, 47)	
	else:
		fnt = ImageFont.truetype('/Users/iprakhar22/Desktop/MinorVSem/dataset/font-ttfs/' + f, 52)

	d = ImageDraw.Draw(img)
	d.text((15,7), "Laseg\ndhum\nHloiv", font=fnt, fill=(0, 0, 0))
	img.save('img2vec/getvectors/paired_images/'+ f.split('.')[0] +'.png')