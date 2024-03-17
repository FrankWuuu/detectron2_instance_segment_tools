from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
from PIL import Image
import cv2

coco = COCO('tooth_ins/UESB_t/annotations/test.json')
img_dir = 'tooth_ins/UESB_t/test'
image_id = 85

img = coco.imgs[image_id]
file_name = img["file_name"]
print(file_name)
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

# new_a = mask/2*255
new_a=np.where(mask==0,0,1)*255


plt.imshow(mask)
cv2.imwrite("mask.jpg",new_a)

plt.savefig(file_name+'_mask.jpg')
# plt.axes("off")
plt.axis('off')
plt.savefig("demo1.jpg", bbox_inches="tight")
# plt.show()

