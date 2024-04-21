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

path_sour_json = "data_pre/teeth/tooth_new_name.json"

parser = argparse.ArgumentParser(description='Splits COCO annotations file into training and test sets.')
parser.add_argument('-annotations', default=path_sour_json, type=str, help='Path to COCO annotations file.')
parser.add_argument('-train_path', default='data_pre/train_tooth.json', type=str, help='Where to store COCO training annotations')
parser.add_argument('-test_path', default='data_pre/test_tooth.json', type=str, help='Where to store COCO test annotations')
# parser.add_argument('-s', dest='split', type=float, default=0.9, help="A percentage of a split; a number in (0, 1)")
parser.add_argument('-s', dest='split', type=float, default=100, help="A percentage of a split; a number in (0, 1)")
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

        X_train, X_left = train_test_split(images, train_size=100)
        X_test, X_left_ = train_test_split(X_left, train_size=100)

        print(len(X_train),len(X_test),len(X_left_))

        anns_train = filter_annotations(annotations, X_train)
        # anns_left = filter_annotations(annotations, X_left)
        anns_test = filter_annotations(annotations, X_test)

        train_path = "data_pre/teeth/train.json"
        test_path = "data_pre/teeth/test.json"

        save_coco(train_path, info, licenses, X_train, anns_train, categories)
        save_coco(test_path, info, licenses, X_test, anns_test, categories)

        # print("Saved {} entries in {} and {} in {}".format(len(anns_train), args.train_path, len(anns_left), args.test_path))
        
if __name__ == "__main__":
    main(args)