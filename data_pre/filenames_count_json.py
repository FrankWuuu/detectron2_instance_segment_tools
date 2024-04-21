import json
import argparse
import csv

parser = argparse.ArgumentParser(description='count COCO annotations images file_names into CSV.')
parser.add_argument('-json', default="data_pre/teeth/test.json", help="annotation json file path")
parser.add_argument('-csv', default="data_pre/teeth/test.csv", help="the file_name list csv file path")
args = parser.parse_args()

def main(args):

    with open(args.json, 'rt', encoding='UTF-8') as annotations:
        coco = json.load(annotations)
        info = coco['info']
        licenses = coco['licenses']
        images = coco['images']
        annotations = coco['annotations']
        categories = coco['categories']
        
        number_of_images = len(images)

        file_names = []
        for img in images:
            file_names.append(img["file_name"])
        
        print("len images: ",number_of_images)

    with open(args.csv, "w+") as csvFile:
        writer = csv.writer(csvFile)
        for i in range(len(file_names)):
            writer.writerow([file_names[i]])


if __name__ == "__main__":
    main(args)

    