from utils import ConfigInit
import os




# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
obj = ConfigInit.ConfigInitialize()
obj.dirCheck(current_dir)
obj.readConfig()


# 拼接路径
