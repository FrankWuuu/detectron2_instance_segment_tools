import json
import pycocotools
import numpy as np
import pycocotools.mask
import pycocotools.mask as mask_util
import cv2

json_name_mask = 'tooth_ins/UESB_t/annotations/test.json'
json_name_pred = 'tooth_ins_out/inference/UESB_t_test/coco_instances_results.json'

# there is no annotations 'id' in the detectron2 inference result

with open(json_name_mask) as json_file:
    data_mask = json.load(json_file)

with open(json_name_pred) as json_file:
    data_pred = json.load(json_file)

new_json = data_mask.copy()
new_json["annotations"] = data_pred

id = 0
for index, anno in enumerate(new_json["annotations"]):
    anno['id'] = id
    anno['iscrowd']=1
    area = int(mask_util.area(anno["segmentation"]))
    anno['area']=area
    print(anno['area'])
    size = anno["segmentation"]["size"]
    anno['height']=size[0]
    anno['width']=size[1]
    new_json["annotations"][index]=anno

    id+=1
    # print(anno['id'])

path_newjson = "tooth_ins_out/inference/UESB_t_test/output_demo.json"
with open(path_newjson, 'w') as outfile:
    json.dump(new_json, outfile)