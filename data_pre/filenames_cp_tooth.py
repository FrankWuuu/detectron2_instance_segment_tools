import os

# copy from data_pre\filenames_count_dir.py

path_csv_train = "data_pre/teeth/train.csv"
path_csv_test = "data_pre/teeth/test.csv"

names_in_tooth_t_train = []
names_in_tooth_t_test = []

with open(path_csv_train,'r') as fc1:
    for line in fc1:
        name_1 = line.split("\n")[0]
        # print(name_1)
        if name_1 !='':
            names_in_tooth_t_train.append(name_1)
print(names_in_tooth_t_train)
print(len(names_in_tooth_t_train))
with open(path_csv_test,'r') as fc2:
    for line in fc2:
        name_2 = line.split("\n")[0]
        if name_2 !='':
            names_in_tooth_t_test.append(name_2)
print(len(names_in_tooth_t_test))

path_dir = "data_pre/tooth"
names_in_dir = os.listdir(path_dir)
print(len(names_in_dir))

names_not_use = list(set(names_in_dir)-set(names_in_tooth_t_train)\
    -set(names_in_tooth_t_test))
print(len(names_not_use))

############# to save imgs to different dirs ############
'''
names_in_dir #total 299
names_in_UESB_t_test # 100
names_in_UESB_t_train # 100

'''
import  shutil

path_tooth_t_train = "data_pre/teeth/train"
path_tooth_t_test = "data_pre/teeth/test"

os.makedirs(path_tooth_t_train,exist_ok=True)
os.makedirs(path_tooth_t_test,exist_ok=True)

for f1 in names_in_tooth_t_test:
    # print(f1)
    src = path_dir +'/'+ f1
    dst = path_tooth_t_test +'/'+ f1
    shutil.copyfile(src=src,dst=dst)

for f2 in names_in_tooth_t_train:
    src = path_dir +'/'+ f2
    dst = path_tooth_t_train +'/'+ f2
    shutil.copyfile(src=src,dst=dst)
