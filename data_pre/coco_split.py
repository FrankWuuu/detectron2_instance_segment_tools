import json
import argparse
from sklearn.model_selection import train_test_split


def filter_annotations(annotations, images):
    image_ids = map(lambda i: int(i['id']), images)
    image_ids = list(image_ids)
    annos = filter(lambda a: int(a['image_id']) in image_ids, annotations)
    annos = list(annos)
    return annos

def save_coco(file, info, licenses, images, annotations, categories):
    with open(file, 'wt', encoding='UTF-8') as coco:
        json.dump({ 'info': info, 'licenses': licenses, 'images': images, 
            'annotations': annotations, 'categories': categories}, coco, indent=2, sort_keys=True)

parser = argparse.ArgumentParser(description='Splits COCO annotations file into training and test sets.')
parser.add_argument('-annotations', default='UESB/test/annotations/test.json', type=str, help='Path to COCO annotations file.')
parser.add_argument('-train_path', default='data_pre/train.json', type=str, help='Where to store COCO training annotations')
parser.add_argument('-test_path', default='data_pre/test.json', type=str, help='Where to store COCO test annotations')
parser.add_argument('-s', dest='split', type=float, default=0.9, help="A percentage of a split; a number in (0, 1)")
args = parser.parse_args()

def main(args):

    with open(args.annotations, 'rt', encoding='UTF-8') as annotations:
        coco = json.load(annotations)
        info = coco['info']
        licenses = coco['licenses']
        images = coco['images']
        annotations = coco['annotations']
        categories = coco['categories']
        
        number_of_images = len(images)
        print("len images: ",number_of_images)

        X_train, X_test = train_test_split(images, train_size=args.split)

        anns_train = filter_annotations(annotations, X_train)
        anns_test = filter_annotations(annotations, X_test)

        save_coco(args.train_path, info, licenses, X_train, anns_train, categories)
        save_coco(args.test_path, info, licenses, X_test, anns_test, categories)

        print("Saved {} entries in {} and {} in {}".format(len(anns_train), args.train_path, len(anns_test), args.test_path))
        
if __name__ == "__main__":
    main(args)