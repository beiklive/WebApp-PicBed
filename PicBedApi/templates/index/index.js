var box = document.getElementById("ViewBox");
var height = 190;   //格子高度
var yourip = "beiklive.top"

const RequestUrl = "http://"+yourip+":6360/ImgRequest"
const ImgUrl = "http://"+yourip+":6360/img/"
const thumbUrl = "http://"+yourip+":6360/thumb/"

window.onload= function(){

    
    
    

    FirstQuest();



}

function ImageClick(e) {
    var index = e.getAttribute("data-index");
    console.log("selected-index:" + index);

    var up = document.getElementById("uppp");
    up.innerHTML = '<div class="bigPic">\
    <img src="'+ImgUrl+index+'">\
                        </div>'

    up.innerHTML += '		<a href="#" class="closeIcon" onclick="CloseView()">\
    <img src="/static/Resource/close.png">\
                        </a>'
    

    up.style.cssText = "visibility: visible;";

}

//第一次加载请求数据
function FirstQuest(params) {
    //计算当前页面的大小从而算出第一次要读多少个
    //然后将个数发送给服务器，等待服务器返回图片略缩图链接和原图链接
    var box = document.getElementById("ViewBox");
	var clientHeight = box.clientHeight;  // 界面高度
    var clientWidth = box.clientWidth;  //界面宽度

    var colcount = parseInt(clientWidth / height);      //能看到的列数
    var RowCount = Math.ceil(clientHeight / height);
    var requestNum = (RowCount + 1) * colcount;  //请求图片的数量
    console.log("colcount:" + colcount);
    console.log("RowCount:" + RowCount);
    console.log("need:" + requestNum)
    $.ajax({
        url: RequestUrl,
        data: {
            "cmd": "ImgLoad",
            "count": requestNum,
            "readyNum" : "0"
        },
        withCredentials: false,
        type: "get",
        success: function (res) {
            console.log("success")
            var res_Json = JSON.parse(res);
            console.log(res_Json.data)
            for(var j = 0; j < res_Json.count; j++){
                let name = res_Json.data[j].imgName;
                let index = res_Json.data[j].index
                box.innerHTML = box.innerHTML + '<div class="imgItem"><img src="'+ thumbUrl + name +'" onclick="ImageClick(this)" data-index='+name+'>\
                            <marquee><span style="font-weight: bolder;font-size: 15px;color: white;">'+index+'.jpg</span></marquee>\
                        </div>';
        
            }
            var imagesList = document.getElementsByClassName("imgItem");
            var length = imagesList.length; // 一共有多少张图片
        
            var clientWidth = box.clientWidth;  //界面宽度
        
            var colcount = parseInt(clientWidth / height);      //能看到的列数
            var totalRow = Math.ceil(length / colcount);        //总行数

            box.style.cssText="grid-template-rows: repeat(" + totalRow + ", 190px);"
            console.log("Load finish")
        }
    })
}

//第一次加载请求数据
function onceQuest(requestNum, readyNum) {
    console.log("need:" + requestNum)
    console.log("readyNum:" + readyNum)

    $.ajax({
        url: RequestUrl,
        data: {
            "cmd": "ImgLoad",
            "count": requestNum,
            "readyNum" : readyNum
        },
        withCredentials: false,
        type: "get",
        success: function (res) {
            console.log("success")
            var res_Json = JSON.parse(res);
            console.log(res_Json.data)
            for(var j = 0; j < res_Json.count; j++){
                let name = res_Json.data[j].imgName;
                let index = res_Json.data[j].index
                box.innerHTML = box.innerHTML + '<div class="imgItem"><img src="'+ thumbUrl + name +'" onclick="ImageClick(this)" data-index='+name+'>\
                            <marquee><span style="font-weight: bolder;font-size: 15px;color: white;">'+index+'.jpg</span></marquee>\
                        </div>';
        
            }
            var imagesList = document.getElementsByClassName("imgItem");
            var length = imagesList.length; // 一共有多少张图片
        
            var clientWidth = box.clientWidth;  //界面宽度
        
            var colcount = parseInt(clientWidth / height);      //能看到的列数
            var totalRow = Math.ceil(length / colcount);        //总行数

            box.style.cssText="grid-template-rows: repeat(" + totalRow + ", 190px);"
            console.log("Load finish")
        }
    })
}


function srollformat() {


    var imagesList = document.getElementsByClassName("imgItem");
    var length = imagesList.length; // 一共有多少张图片

	var clientHeight = box.clientHeight;  // 界面高度
    var clientWidth = box.clientWidth;  //界面宽度

    var colcount = parseInt(clientWidth / height);      //能看到的列数

    var top = imagesList[length - 1].getBoundingClientRect().top;
    var lastTop = imagesList[length - 1].getBoundingClientRect().bottom;
    var totalRow = Math.ceil(length / colcount);        //总行数

    box.style.cssText="grid-template-rows: repeat(" + totalRow + ", 190px);"
    if (clientHeight > lastTop || clientHeight > top) {
        onceQuest(colcount*3, length)
    }
    // console.log("========");
    // console.log("clientHeight + height:"+ (clientHeight + height))
    // console.log("viewHeight:"  + clientHeight);      //界面高度
    // console.log("lastTop:" + lastTop);
    // console.log("col:" + colcount);
    // console.log("row:" + RowCount);
    // console.log("totalrow:" + totalRow);



}