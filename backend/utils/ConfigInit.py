import json
import os
import logging

# 设置日志记录器
logging.basicConfig(level=logging.INFO)
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(format=LOG_FORMAT)
# logger = logging.getLogger(__name__)

class ConfigInitialize:
    def __init__(self) -> None:
        self.m_apiUrl = "http://localhost:8961"
        self.m_configFile = "config.json"
        self.m_basePath = None

        self.m_path_cache = "../.cache"
        self.m_path_cache_config = "../.cache/config"
        self.m_path_cache_database = "../.cache/database"
        self.m_path_checklist = [
            self.m_path_cache, 
            self.m_path_cache_config, 
            self.m_path_cache_database
        ]


    # 检查数据目录是否存在并创建
    def dirCheck(self, basePath):
        self.m_basePath = basePath
        for directory in self.m_path_checklist:
            joined_path = os.path.join(basePath, directory)

            if os.path.exists(joined_path):
                logging.info(f"目录存在: {joined_path}")
            else:
                logging.info(f"创建目录: {joined_path}")
                os.makedirs(joined_path)

    def readConfig(self):
        if self.m_basePath == None:
            print("please use dirCheck(basepath) function in advance")
        else:
            file_path = os.path.join(self.m_basePath, self.m_path_cache_config, self.m_configFile)
            if not os.path.exists(file_path):
                print(f"文件'{file_path}'不存在，正在创建...")
                # 确保文件的目录存在，如果目录不存在，则创建它
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                # 打开文件进行写操作，如果文件不存在将会被创建
                with open(file_path, 'w') as file:
                    file.write('')  # 可以在文件中写入初始内容
                print(f"文件'{file_path}'已创建。")
            else:
                print(f"文件'{file_path}'已存在。")
        pass
