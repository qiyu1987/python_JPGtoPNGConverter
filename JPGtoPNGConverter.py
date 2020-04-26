import sys
import os
from PIL import Image

src_folder = sys.argv[1]
tar_folder = sys.argv[2]

file_names = os.listdir(src_folder)
if not os.path.isdir(tar_folder):
    os.mkdir(tar_folder)
for file_name in file_names:
    file = Image.open(sys.argv[1] + file_name)
    file.save(sys.argv[2]+file_name.replace('jpg', 'png'), 'png')

