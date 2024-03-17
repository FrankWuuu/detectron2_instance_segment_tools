from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
from PIL import Image

coco = COCO('tooth_ins/UESB_t/annotations/test.json')
img_dir = 'tooth_ins/UESB_t/test'
image_id = 178

img = coco.imgs[image_id]
# loading annotations into memory...
# Done (t=12.70s)
# creating index...
# index created!

image = np.array(Image.open(os.path.join(img_dir, img['file_name'])))
plt.imshow(image, interpolation='nearest')
plt.show()

plt.imshow(image)
cat_ids = coco.getCatIds()
anns_ids = coco.getAnnIds(imgIds=img['id'], catIds=cat_ids, iscrowd=None)
anns = coco.loadAnns(anns_ids)
coco.showAnns(anns)
plt.show()

mask = coco.annToMask(anns[0])
for i in range(len(anns)):
    mask += coco.annToMask(anns[i])

plt.imshow(mask)
plt.show()

