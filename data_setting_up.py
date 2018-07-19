import numpy as np
import os

root = os.path.dirname(os.path.realpath(__file__))
path_name = r'train_full\audio\unknown_d'
direc_name= os.path.join(root, path_name)
files = os.listdir(direc_name)
print(len(files))
# file = os.listdir(os.path.join(dir_name,files[1]))
# print(len(file))
unknown ='unknown'
new_fldr = os.path.join(direc_name, unknown)
if not os.path.exists(new_fldr):
    os.makedirs(new_fldr)
print(new_fldr)
os.chdir(new_fldr)
for file in files:
	file_path = os.path.join(direc_name, file)
	[os.rename(os.path.join(file_path, f), file+'/'+f) for f in os.listdir(file_path)]

