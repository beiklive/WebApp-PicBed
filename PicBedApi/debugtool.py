#  用于将thumbnail和imgSource中的图片更新到腾讯cos中，仅在这次添加腾讯cos的更新中使用

import json
import ObjectCos
import os,base64
import configRead

# 本地全部上传到对象存储
# file_path = "./thumbnail"
# dir_list = os.listdir(file_path)
# dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))

# for file in dir_list:
#     ObjectCos.TxCosUpload(file, "./imgSource/")
#     ObjectCos.TxCosUpload(file, "./thumbnail/")
#     print(file + " ----> upload")



# 从对象存储下载
bucket = configRead.ReadElem("TXCos", "Bucket")
region = configRead.ReadElem("TXCos", "region")
url1 = "https://" +bucket+".cos."+region+".myqcloud.com/imgSource/"
url2 = "https://" +bucket+".cos."+region+".myqcloud.com/thumbnail/"
Namelist = ObjectCos.LoadCosList()
for name in Namelist:
    os.system("wget "+url1+name)
    os.system("mv "+ name + " " + "./imgSource/")
    os.system("wget "+url2+name)
    os.system("mv "+ name + " " + "./thumbnail/")
    print(name + "---------> download")