#! /bin/bash
APP_DIR="./PicBedApi/"
APP_NAME="PicBedApp"

startFun(){
    echo "正在启动程序..."
    cd $APP_DIR
    nohup python3 $APP_NAME.py > $APP_NAME.log 2>&1 &
    if [ $? -eq 0 ]; then
        echo "程序pid:" `ps -aux | grep "python3 $APP_NAME.py"| head -n 1| awk '{print $2}'`
        echo "程序启动成功"
    else
        echo "程序启动失败"
    fi
}

closeFun(){
    echo "正在停止程序..."
    ps -aux | grep "python3 $APP_NAME.py"| head -n 1| awk '{print $2}'| xargs kill -9
    if [ $? -eq 0 ]; then
        echo "程序pid:" `ps -aux | grep "python3 $APP_NAME.py"| head -n 1| awk '{print $2}'`
        echo "停止程序成功"
    else
        echo "关闭程序出现错误"
    fi
}

# ===================================main========================================
if [ $# -eq 0 ]; then
    echo "[help]"
    echo "./startup.sh close    [关闭程序] "
    echo "./startup.sh start    [启动/重启程序] "
    echo "./startup.sh show    [显示程序进程信息] "
else
    if [ "$1" == "start" ]; then
        res=`ps -aux | grep -c "python3 $APP_NAME.py"`
        if [ $res -eq 1 ]; then
            echo "程序未运行"
            startFun
        else
            closeFun
            sleep 1
            startFun
        fi
    fi

    if [ "$1" == "close" ]; then
        res=`ps -aux | grep -c "python3 $APP_NAME.py"`
        if [ $res -eq 1 ]; then
            echo "程序未运行"
        else
            closeFun
        fi
    fi

    if [ "$1" == "show" ]; then
        res=`ps -aux | grep -c "python3 $APP_NAME.py"`
        if [ $res -eq 1 ]; then
            echo "程序未运行"
        else
            echo `ps -aux | grep "python3 $APP_NAME.py"| head -n 1`
        fi
    fi

    if [ "$1" == "clean" ]; then
        echo "正在清理..."
        cd PicBedApi
        echo "正在清理api数据"
        rm ImgData.json
        echo "正在清理图片数据"
        rm -rf imgSource
        echo "正在清理略缩图"
        rm -rf thumbnail
        echo "清理完成，请重启服务"
    fi
    
fi
# ===================================main========================================
