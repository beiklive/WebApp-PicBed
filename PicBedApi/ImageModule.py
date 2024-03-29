from PIL import Image
import os,base64
import json
import time
import random

import ObjectCos
import configRead
import ObjectGiteeApi
# 程序启动时先读取一次文件列表

FileList = []
JsonList = []

def ReadConfig():
    with open('./templates/config.json', 'r') as f:
        config = json.load(f)
        return config['url']

def UpdateFileList(filename):
    global FileList
    FileList += [filename]

def LoadDir():
    global FileList
    file_path = "./thumbnail"
    dir_list = []
    if len(FileList) == 0:
        flagTXCos = configRead.ReadElem("TXCos", "Active")
        flagGitee = configRead.ReadElem("Gitee", "Active")
        if(flagTXCos == "true" and flagGitee == "true"):
            raise Exception("TXCos和Gitee 不允许同时为true")

        if (flagTXCos == "true"):
            dir_list = ObjectCos.LoadCosList()
            dir_list = sorted(dir_list, key=str.lower)
        elif (flagGitee == "true"):
            dir_list = ObjectGiteeApi.LoadDirList()
            dir_list = sorted(dir_list, key=str.lower)
        else:
            dir_list = os.listdir(file_path)
            dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
    else:
        dir_list = FileList
    print("Read FileList finish")
    print(dir_list)
    return dir_list

def PreLoad():
    global FileList
    FileList = LoadDir()

def SaveImgInfo(name):
    with open('ImgData.json', encoding='utf-8') as f:
        line = f.read()
        if line == '':
            JsonList = {'ImageData': [{'Name': 'default', 'CreateTime': 'default', 'Tags': ['default'], 'url': 'default'}]}
        else:
            JsonList = json.loads(line)
        f.close()
    JsonList['ImageData'] +=[{
        "Name": name,
            "CreateTime":time.strftime("%Y-%m-%d %X",time.localtime()),
            "Tags":["anima", "adult"],
            "url": ReadConfig() + "/img/"+name
    }]
    file = 'ImgData.json'
    fp = open(file, 'w')
    fp.write(json.dumps(JsonList))
    print(JsonList)

def SaveImg(MainPath, name, get):
    img_data = base64.b64decode(get)
    with open(MainPath + name, 'wb') as f:
        f.write(img_data)

    if (configRead.ReadElem("TXCos", "Active") != "false"):
        ObjectCos.TxCosUpload(name, MainPath)
        # SaveImgInfo(name)
    elif (configRead.ReadElem("Gitee", "Active") != "false"):
        ObjectGiteeApi.GiteeUpload(MainPath,name)

    print(name + " save complete")

def SaveThumb(MainPath, ThumbPath, name):
    image = Image.open(MainPath + name)
    w, h = image.size
    ImgSize = 160
    if w > ImgSize or h > ImgSize:
        if w > h:
            h = h * ImgSize / w
            w = ImgSize
        else:
            w = w * ImgSize / h
            h = ImgSize
    h = int(h)
    w = int(w)
    image_size = image.resize((w, h), Image.LANCZOS)
    image_size.save(ThumbPath + name)
    ObjectCos.TxCosUpload(name, ThumbPath)
    UpdateFileList(name)
    # FileList = LoadDir()

def ImgLoadCMD(self):
    global FileList
    m_count = int(self.get_argument("count"))
    m_readyNum = int(self.get_argument("readyNum"))
    FileList = LoadDir()
    ListLength = len(FileList)
    m_sendcount = m_count
    # 当数量不足时
    if ListLength - m_readyNum < m_count:
        m_sendcount = ListLength - m_readyNum
    dataDict = []
    for i in range(m_sendcount):
        Imgid =  m_readyNum + i
        dataDict += [{"imgName" : FileList[Imgid], "index" : str(Imgid)}]
    ReturnDict = {"cmd" : "ImgLoad", "count" : str(m_sendcount), "data": dataDict}
    # print(ReturnDict)
    self.write(json.dumps(ReturnDict))

def GetRandom():
    Namelist = LoadDir()
    length = len(Namelist)
    # print(length)
    ran = random.randint(1,length - 1)
    # print(ran)
    return ObjectCos.GetUrl() + "/" + Namelist[ran]

def ImgDeleteCMD(self):
    m_fileName = self.get_argument("name")

    imgPath = "./imgSource/" + m_fileName
    thumbPath = "./thumbnail/" + m_fileName

    if (configRead.ReadElem("TXCos", "Active") != "false"):
        ObjectCos.TxCosDelete(imgPath)
        ObjectCos.TxCosDelete(thumbPath)

    elif (configRead.ReadElem("Gitee", "Active") != "false"):
        ObjectGiteeApi.GiteeDelete(m_fileName)

    if(os.path.isfile(imgPath)):
        os.remove(imgPath)
    if(os.path.isfile(thumbPath)):
        os.remove(thumbPath)

    FileList.remove(m_fileName)
    ReturnDict = {"cmd" : "ImgDelete", "status" : "success"}
    return ReturnDict
