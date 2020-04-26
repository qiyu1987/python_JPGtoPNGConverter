import sys
import os
from PIL import Image
'''
taking two commandline arguments as source and target folder
converting all jpg files in the source folder to png and save in the target folder
'''
src_folder = sys.argv[1]
tar_folder = sys.argv[2]

# if target folder does not exist, create one
if not os.path.isdir(tar_folder):
    os.mkdir(tar_folder)

file_names = os.listdir(src_folder)

# loop through all files in source folder and save them as png in target folder
for file_name in file_names:
    file = Image.open(src_folder + file_name)
    file.save(tar_folder+file_name.replace('jpg', 'png'), 'png')

