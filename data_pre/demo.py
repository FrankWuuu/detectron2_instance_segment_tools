import json


path_train = "data_pre/train.json"
path_test = "data_pre/test.json"

def main():

    with open(path_test, 'rt', encoding='UTF-8') as annotations:
        coco = json.load(annotations)
        info = coco['info']
        licenses = coco['licenses']
        images = coco['images']
        print(len(images))
        annotations = coco['annotations']
        print(len(annotations))

if __name__ == "__main__":
    main()