
############# to merge children imgs to all_imgs ############
'''
all_imgs # 193
train # 70
test # 30
supplemental  # 93
'''
import  shutil
import os

path_src = "children"
path_dst = "tooth_ins/children/all_imgs/"

os.makedirs(path_dst,exist_ok=True)

child_dirs = os.listdir(path_src)

for dir in child_dirs:
    path_tmp = path_src+'/'+dir+"/images/"
    names_sours = os.listdir(path_tmp)
    for name_ in names_sours:
        path_src_sub = path_tmp + name_
        path_dst_sub = path_dst + name_
        # print(path_src_sub,path_dst_sub)
        shutil.copyfile(src=path_src_sub,dst=path_dst_sub)