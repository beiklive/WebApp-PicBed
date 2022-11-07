#  用于将thumbnail和imgSource中的图片更新到腾讯cos中，仅在这次添加腾讯cos的更新中使用

import json
import ObjectCos
import os,base64


file_path = "./thumbnail"
dir_list = os.listdir(file_path)
dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))

for file in dir_list:
    ObjectCos.TxCosUpload(file, "./imgSource/")
    ObjectCos.TxCosUpload(file, "./thumbnail/")
    print(file + " ----> upload")

