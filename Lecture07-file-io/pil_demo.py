import sys
from PIL import Image

images=[]

for arg in sys.argv[1:]:
    image=Image.open(arg)
    images.append(image)

images[0].save(
    "cat.gif",
    save_all=True,
    append_images=[images[1]],
    duration=200,
    loop=0
)

'''
We will run like this python pil_demo.pes/cat1.jpg images/cat2.jpg
and it will create cat.gif file 
'''