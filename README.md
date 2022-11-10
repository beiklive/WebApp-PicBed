# WebApp-PicBed
# 在线相册服务

![Alt](https://repobeats.axiom.co/api/embed/c9d3ba2f9aa90b8e25786691e17054d4f35a93f1.svg "Repobeats analytics image")

# 介绍
一个简易的相册系统，更多功能后续再开发

图床程序采用python编写，使用tornado框架驱动web服务器

主旨： 开箱即用，不需要过多的环境和配置




# 使用

## 环境安装

`python >= 3.6`

```bash
source requirements.txt
```



## 初始配置修改（必须修改！！！）

1. 修改`WebApp-PicBed\PicBedApi\templates\config.json`

    | Key    | Type     | Value                                                        |
    | ------ | -------- | ------------------------------------------------------------ |
    | url    | `string` | 启动后服务的地址，如：`http://picture.xxx.com `  或者   `127.0.0.1:8080` |
    | title  | `string` | 网站标题栏名称                                               |
    | port   | `number` | 服务的端口号                                                 |
    | passwd | `string` | 默认进入服务是未登录状态，使用该密码登录                     |
    | useCos | `string` | 是否使用腾讯云cos，为true时是使用，填写任意其他字符为不使用，会使用服务本地存储 |
    | Bucket | `string` | 腾讯对象存储桶名称                                           |
    | region | `string` | 存储桶所属地区如： `ap-beijing`                              |

2. 修改log图标

​		替换`WebApp-PicBed\PicBedApi\templates\Resource\logo.png`文件即可

## 启动

```shell
./startup.sh start
```
## 关闭
```shell
./startup.sh close
```
## 查看运行状态
```shell
./startup.sh show
```
# 预览
### 主界面

![image-20221007225633029](img/image-20221007225633029.png)

### 图片预览

![image-20221007225730537](img/image-20221007225730537.png)

### 图片上传

![image-20221007225804288](img/image-20221007225804288.png)


# 功能
- [x] 图片上传
- [x] 随机图片： url + `/redirect?type=random`

​			http://img.example.com/redirect?type=random

- [ ] 登录（目前的登录没有安全性可言）
- [ ] 删除图片
- [ ] GitPage托管
