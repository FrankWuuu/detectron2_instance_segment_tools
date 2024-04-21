import os
import shutil

path_csv_test = "data_pre/test_tooth.csv"

names_in_UESB_t_test = []

with open(path_csv_test,'r') as fc1:
    for line in fc1:
        name_1 = line.split("\n")[0]
        # print(name_1)
        if name_1 == '':
            continue
        # name_1 = name_1.split('\n')
        # if name_1!='\n':
        names_in_UESB_t_test.append(name_1)


path_img_train = "E:/files/data/smartee/datateeth/datatrain/img/"
names_in_train = os.listdir(path_img_train)
path_img_test = "E:/files/data/smartee/datateeth/datatest/img/"
names_in_test = os.listdir(path_img_test)

name_blank_train = []
name_blank_test = []

path_dest = 'data_pre/tooth/'
os.makedirs(path_dest,exist_ok=True)

for name in names_in_UESB_t_test:
    tmp = 'img_'+name
    if tmp in names_in_train:
        name_blank_train.append(tmp)
        src = path_img_train + tmp
        dst = path_dest + name
        print(src,dst)
        shutil.copyfile(src=src,dst=dst)
    if tmp in names_in_test:
        name_blank_test.append(tmp)
        src = path_img_test + tmp
        dst = path_dest + name
        print(src,dst)
        shutil.copyfile(src=src,dst=dst)
        # print(tmp)

print(len(name_blank_train))
print(len(name_blank_test))

