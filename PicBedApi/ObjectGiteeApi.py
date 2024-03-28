
import base64

import requests
import configRead

# 程序启动时先读取一次文件列表

FileList = []
JsonList = []
folder_path = configRead.ReadElem("Gitee", "folderPath")
# 设置 Gitee 仓库信息
repo_owner = configRead.ReadElem("Gitee", "repoOwner")
repo_name = configRead.ReadElem("Gitee", "repoName")
api_token = configRead.ReadElem("Gitee", "apiToken")

# 构建 API 请求头
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': f'token {api_token}'
}

# api路径
uri = f'https://gitee.com/api/v5/repos/{repo_owner}/{repo_name}/contents/{folder_path}'

# 查询仓库指定文件夹下的所有文件 返回文件名List
def LoadDirList():
    nameList = []
    # 发送 GET 请求获取仓库文件信息
    response = requests.get(uri,headers=headers)
    if response.status_code == 200:
        files = response.json()
        for file in files:
            if file['type'] == 'file':
                nameList.append(file['name'])
            else:
                print(f"Failed to fetch repository contents. Status code: {response.status_code}")

    print("Read FileList finish")
    return nameList


# 上传文件api
def GiteeUpload(MainPath, name):

    with open(MainPath + name, 'rb') as f:
        date = f.read()

    image_base64 = base64.b64encode(date).decode('utf-8')
    # 构建上传文件的数据
    data = {
        'access_token': api_token,
        'message': 'Upload file ' + name,
        'content': image_base64,  # 使用base64编码后的图片数据
        'committer': {
            'name': 'xxx',
            'email': 'xxx@email'
        }
    }
    response = requests.post(f'{uri}/{name}',
                             headers={'Content-Type': 'application/json'}, json=data)
    if response.status_code == 201:
        print("File uploaded successfully.")
    else:
        print(f"Failed to upload file. Status code: {response}")
    print(name + " save complete")

# 删除文件api
def GiteeDelete(m_fileName):

        url = f'{uri}/{m_fileName}'

        # 获取文件信息
        response = requests.get(url, headers=headers)
        file_info = response.json()
        sha = file_info['sha']  # 获取文件的 SHA 校验值

        # 构建提交信息
        commit_message = "Deleting file  " + m_fileName  # 提交信息可以自定义

        # 构建请求体
        data = {
            "message": commit_message,
            "sha": sha
        }

        response = requests.delete(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"文件 {m_fileName} 删除成功！")
        else:
            print(f"文件 {m_fileName} 删除失败：{response.status_code} - {response.text}")


