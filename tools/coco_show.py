from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)


# dataDir="tooth_ins/children/train/images"
dataDir="tooth_ins/UESB_t/test"
# dataType='val2017'
# annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
# annFile=dataDir +'/annotations/train.json'
# annFile=dataDir +'/annotations/train.json'

# annFile="train_rle.json"
annFile="tooth_ins_out/inference/UESB_t_test/coco_instances_results.json"
annFile="tooth_ins_out/inference/UESB_t_test/output_demo.json"
# annFile="O2PR/test/annotations/test.json"
# annFile="DEMO_OUTPUT/inference/my_dataset_val/output_demo.json"

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories, select one at random
catIds = coco.getCatIds(catNms=['1'])
imgIds = coco.getImgIds(catIds=catIds )
imgIds = coco.getImgIds(imgIds = [230])
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
# load and display image
# I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
# I = io.imread(dataDir+'/images/%s'%(img['file_name']))
I = io.imread(dataDir+'/%s'%(img['file_name']))
# use url to load image
# I = io.imread(img['coco_url'])
plt.axis('off')
plt.imshow(I)
plt.show()

# load and display instance annotations
plt.imshow(I)
plt.axis('off')
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
coco.showAnns(anns)
plt.savefig("o2pr_data_demo.png")
plt.show()

