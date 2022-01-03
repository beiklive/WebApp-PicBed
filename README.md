# WebApp-PicBed
# 在线相册服务
# 介绍
    启动脚本`startup.sh`为linux的脚本，图床程序采用python编写，使用tornado实现路由
# 使用
    修改`/templates/index`下的`index.js`和`upload.js`,将url地址改为自己的ip或者域名

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
# 相册网页入口
```
http://beiklive.top:6360
```


# 已有功能
1. 上传图片
2. 使用api来重定向图片
    > http://beiklive.top:6360/redirect?type=random


