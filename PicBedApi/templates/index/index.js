var box = document.getElementById("ViewBox");
var height = 200; //格子高度
var ItemHeight = 200; //格子高度

var requestNum = 30;
var g_readyNum = 0;
var yourip = "beiklive.top";

var RequestInfo = "http://beiklive.top:" + 8830;

const RequestUrl = RequestInfo + "/ImgRequest";
const ImgUrl = RequestInfo + "/img/";
const thumbUrl = RequestInfo + "/thumb/";

window.onload = function () {
  FirstQuest();
};

function ImageClick(e) {
  var index = e.getAttribute("data-index");
  console.log("selected-index:" + index);

  var up = document.getElementById("uppp");
  up.innerHTML =
    '<div class="bigPic">\
    <img src="' +
    ImgUrl +
    index +
    '">\
                        </div>';



}

//第一次加载请求数据
function FirstQuest(params) {
  //计算当前页面的大小从而算出第一次要读多少个
  //然后将个数发送给服务器，等待服务器返回图片略缩图链接和原图链接
  var box = document.getElementById("ViewBox");
  var clientHeight = box.clientHeight; // 界面高度
  var clientWidth = box.clientWidth; //界面宽度

  if (clientHeight <= 700) {
    ItemHeight = 130;
  } else {
    ItemHeight = 200;
  }

  var colcount = parseInt(clientWidth / ItemHeight); //能看到的列数
  var RowCount = Math.ceil(clientHeight / ItemHeight);
  var requestNum1 = (RowCount + 4) * colcount; //请求图片的数量
  // console.log("colcount:" + colcount);
  // console.log("RowCount:" + RowCount);
  // console.log("need:" + requestNum)
  $.ajax({
    url: RequestUrl,
    data: {
      cmd: "ImgLoad",
      count: requestNum1,
      readyNum: g_readyNum,
    },
    withCredentials: false,
    type: "get",
    success: function (res) {
      console.log("success");
      var res_Json = JSON.parse(res);
      console.log(res_Json.data);
      for (var j = 0; j < res_Json.count; j++) {
        let name = res_Json.data[j].imgName;
        let index = res_Json.data[j].index;
        box.innerHTML =
          box.innerHTML +
          '<div class="imgItem"  data-bs-toggle="modal" data-bs-target="#myModal2"><img src="' +
          thumbUrl +
          name +
          '" onclick="ImageClick(this)" data-index=' +
          name +
          '>\
                            <marquee><span style="font-weight: bolder;font-size: 15px;color: white;">' +
          index +
          ".jpg</span></marquee>\
                        </div>";
        g_readyNum = g_readyNum + 1;
      }
      var imagesList = document.getElementsByClassName("imgItem");
      var length = imagesList.length; // 一共有多少张图片

      var clientWidth = box.clientWidth; //界面宽度

      var colcount = parseInt(clientWidth / height); //能看到的列数
      var totalRow = Math.ceil(length / colcount); //总行数

      // box.style.cssText="grid-template-rows: repeat(" + totalRow + ", 200px);"
      console.log("Load finish");
    },
  });
}

//一次加载请求数据
function onceQuest(requestNum, readyNum) {
  console.log("requestNum:" + requestNum);
  console.log("readyNum:" + readyNum);

  $.ajax({
    url: RequestUrl,
    data: {
      cmd: "ImgLoad",
      count: requestNum,
      readyNum: readyNum,
    },
    withCredentials: false,
    type: "get",
    success: function (res) {
      console.log("success");
      var res_Json = JSON.parse(res);
      // console.log(res_Json.data)
      for (var j = 0; j < res_Json.count; j++) {
        let name = res_Json.data[j].imgName;
        let index = res_Json.data[j].index;
        box.innerHTML =
          box.innerHTML +
          '<div class="imgItem" data-bs-toggle="modal" data-bs-target="#myModal2"><img src="' +
          thumbUrl +
          name +
          '" onclick="ImageClick(this)" data-index=' +
          name +
          '>\
                            <marquee><span style="font-weight: bolder;font-size: 15px;color: white;">' +
          index +
          ".jpg</span></marquee>\
                        </div>";
        g_readyNum = g_readyNum + 1;
      }
      var imagesList = document.getElementsByClassName("imgItem");
      var length = imagesList.length; // 一共有多少张图片

      var clientWidth = box.clientWidth; //界面宽度

      var colcount = parseInt(clientWidth / height); //能看到的列数
      var totalRow = Math.ceil(length / colcount); //总行数

      // box.style.cssText="grid-template-rows: repeat(" + totalRow + ", 200px);"
      console.log("Load finish");
    },
  });
}

function srollformat() {
  var box = document.getElementById("ViewBox");


  let st = box.scrollTop; //已经卷上去的高度
  let ct = box.clientHeight; //该元素当前的视窗高度
  let sh = box.scrollHeight; //该元素的总高度
  if (st + ct >= sh) {
    onceQuest(requestNum, g_readyNum);
  }
}
