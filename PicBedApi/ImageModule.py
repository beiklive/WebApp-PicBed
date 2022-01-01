from PIL import Image
import os,base64
import json

def LoadDir():
    file_path = "./thumbnail"
    dir_list = os.listdir(file_path)
    dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
    print("sort finish")
    return dir_list


# 程序启动时先读取一次文件列表
FileList = []
FileList = LoadDir()



def SaveImg(MainPath, name, get):
    img_data = base64.b64decode(get)
    with open(MainPath + name, 'wb') as f:
        f.write(img_data)
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
    image_size = image.resize((w, h), Image.ANTIALIAS)
    image_size.save(ThumbPath + name)
    FileList = LoadDir()

def ImgLoadCMD(self):
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
        