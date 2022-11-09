# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import json
import logging

import configRead
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 填写对象存储中的相关信息
secret_id = configRead.ReadElem("TXCos", "secret_id")
secret_key = configRead.ReadElem("TXCos", "secret_key")
bucket = configRead.ReadElem("TXCos", "Bucket")
region = configRead.ReadElem("TXCos", "region")



token = None
scheme = 'https'
prefixName = 'imgSource/'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

def ReadCosConfig():
    return configRead.ReadElem("TXCos", "Active")



def TxCosUpload(filename, path):
    if ReadCosConfig() != "false":
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

def TxCosDelete(prefix, filename):
    if ReadCosConfig() != "false":
        print("start delete to Cos : " +filename)
        response = client.delete_object(
            Bucket=bucket,
            Key=prefix + filename
        )
        print(response)

def GetUrl():
    url = ''
    if ReadCosConfig() != "false":
        url = "https://"+ bucket +".cos."+ region +".myqcloud.com/imgSource/"
    else:
        url = configRead.ReadElem("Server", "WebSite")
    return url

def LoadCosList():
    response = client.list_objects(
        Bucket=bucket,
        Prefix=prefixName
    )
    nameList=[]
    for i in response.get('Contents'):
        Name = i.get('Key')
        if prefixName != Name:
            Name = Name[len(prefixName) : ]
            nameList += [Name]
    return nameList

