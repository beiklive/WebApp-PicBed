import yaml

ConfigPath='../config.yml'

def ReadElem(root, son):
    f = open(ConfigPath, "r", encoding="utf-8")      # open方法打开直接读出来
    cfg = f.read()
    f.close()
    # print(type(cfg))       # 读出来是字符串
    d = yaml.load(cfg, Loader=yaml.FullLoader)[root]      # 用load方法转字典
    for element in d:
        if element.get(son) is not None :
            return(element.get(son))

def PageConfig():
    mUrl = ReadElem("Server", "WebSite")
    mTitle = ReadElem("Server", "SiteTitle")
    museCos = ReadElem("TXCos", "Active")
    mBucket = ReadElem("TXCos", "Bucket")
    mRegion = ReadElem("TXCos", "region")

    mRepoOwner = ReadElem("Gitee", "repoOwner")
    mRepoName = ReadElem("Gitee", "repoName")
    museGitee = ReadElem("Gitee", "Active")
    folderPath = ReadElem("Gitee", "folderPath")
    apiToken = ReadElem("Gitee", "apiToken")

    ReturnDict = {"url": mUrl, "title": mTitle, "useCos": museCos, "Bucket": mBucket, "region": mRegion,
                  "repoOwner": mRepoOwner, "repoName": mRepoName, "useGitee": museGitee, "folderPath": folderPath,
                  "apiToken": apiToken}
    print("return ReturnDict")
    return ReturnDict

