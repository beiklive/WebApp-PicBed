# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import json
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 填写对象存储中的相关信息
secret_id = 'xxxxxxx'
secret_key = 'xxxxxxx'
bucket = 'xxxxxxx'
region = 'xxxxxxx'



token = None
scheme = 'https'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

def ReadCosConfig():
    with open('./templates/config.json', 'r') as f:
        config = json.load(f)
        return config['useCos']


def TxCosUpload(filename, path):
    if ReadCosConfig():
        print("start upload to Cos : " +path + filename)
        response = client.upload_file(
            Bucket=bucket,
            LocalFilePath=path + filename,
            Key=path + filename,
            PartSize=1,
            MAXThread=10,
            EnableMD5=False
        )
        print(response)

def GetUrl():
    return "https://"+ bucket +".cos."+ region +".myqcloud.com/imgSource/"



