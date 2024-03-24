import os

path_csv_train = "data_pre/train.csv"
path_csv_test = "data_pre/test.csv"

names_in_UESB_t_train = []
names_in_UESB_t_test = []

with open(path_csv_train,'r') as fc1:
    for line in fc1:
        name_1 = line.split("\n")[0]
        # print(name_1)
        names_in_UESB_t_train.append(name_1)
print(len(names_in_UESB_t_train))
with open(path_csv_test,'r') as fc2:
    for line in fc2:
        name_2 = line.split("\n")[0]
        names_in_UESB_t_test.append(name_2)
print(len(names_in_UESB_t_test))

path_dir = "UESB/test/images"
names_in_dir = os.listdir(path_dir)
print(len(names_in_dir))

names_not_use = list(set(names_in_dir)-set(names_in_UESB_t_train)\
    -set(names_in_UESB_t_test))
print(len(names_not_use))

######## to save the not_use img names to csv #########
import csv
path_csv_not_use = "data_pre/not_use.csv"
with open(path_csv_not_use, "w+") as csvFile:
    writer = csv.writer(csvFile)
    for i in range(len(names_not_use)):
        writer.writerow([names_not_use[i]])


############# to save imgs to different dirs ############
'''
names_in_dir #total 478
names_in_UESB_t_test # 20
names_in_UESB_t_train # 173
names_not_use # 285
'''
import  shutil

path_UESB_t_train = "tooth_ins/UESB_t/train"
path_UESB_t_test = "tooth_ins/UESB_t/test"
path_not_use = "data_pre/not_use"

os.makedirs(path_UESB_t_train,exist_ok=True)
os.makedirs(path_UESB_t_test,exist_ok=True)
os.makedirs(path_not_use,exist_ok=True)

for f1 in names_in_UESB_t_test:
    # print(f1)
    src = path_dir +'/'+ f1
    dst = path_UESB_t_test +'/'+ f1
    shutil.copyfile(src=src,dst=dst)

for f2 in names_in_UESB_t_train:
    src = path_dir +'/'+ f2
    dst = path_UESB_t_train +'/'+ f2
    shutil.copyfile(src=src,dst=dst)

for f3 in names_not_use:
    src = path_dir +'/'+ f3
    dst = path_not_use +'/'+ f3
    shutil.copyfile(src=src,dst=dst)