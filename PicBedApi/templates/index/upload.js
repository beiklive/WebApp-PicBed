var fileList = [];
var progressbar = 1;

function uploadImg(){
    var up = document.getElementById("uppp");
    up.innerHTML = '<div class="uploadBox">\
                                <div class="btnBox">\
                                    <a href="javascript:;" class="file">Browse...\
                                        <input type="file" name="" id="file-input" multiple accept="image/*">\
                                    </a>\
                                    <h2>图片上传</h2>\
                                    <a href="javascript:;" class="Cancel" onclick="upCancel()">Cancel\
                                    </a>\
                                </div>\
                                <div class="dragbox" id="imgdragbox">\
                                </div>\
                                <div class="submitbox">\
                                    <meter id="m1" value="0" min="0" max="100"></meter>\
                                    <a href="javascript:;" class="Cancel"  onclick="submit()">Submit\
                                    </a>\
                                </div>\
                            </div>'
    up.style.cssText = "visibility: visible;";
    var files = document.getElementById("file-input")
    
    files.addEventListener("change", function (event) {

        renderFileList(files);
    });
    
}

function upCancel(){
    var up = document.getElementById("uppp");
    fileList = [];
    up.style.cssText = "visibility:hidden;";
    up.innerHTML = ' ';
    location.reload();
}

function CloseView(){
    var up = document.getElementById("uppp");
    fileList = [];
    up.style.cssText = "visibility:hidden;";
    up.innerHTML = ' ';
}

function renderFileList(files) {
    console.log("filecount:" + files.files.length);
    
    var bar = document.getElementById("m1");
    bar.max = files.files.length;
    bar.value = 0;
    console.log(bar.max)
    for (var i = 0; i < files.files.length; i++) {
        fileList.push(files.files[i]);
        
        readfile(files.files[i]);
        
        // console.log(files.files[i]);
    }
    var length = fileList.length;
    var box = document.getElementById("imgdragbox");
    var clientWidth = box.clientWidth;  //界面宽度
    var colcount = parseInt(clientWidth / height);      //能看到的列数
    var totalRow = Math.ceil(length / colcount);        //总行数
    box.style.cssText="grid-template-rows: repeat(" + totalRow + ", 170px);"

}

function readfile(file) {
    var reader = new FileReader();
    var name = file.name
    reader.onloadstart = function (e) {

        console.log("开始读取....");
    }
    reader.onprogress = function (e) {
        console.log("正在读取中....");
    }
    reader.onabort = function (e) {
        console.log("中断读取....");
    }
    reader.onerror = function (e) {
        console.log("读取异常....");
    }
    reader.onload = function (e) {
        console.log("成功读取....");
        // console.log(e);
        var box = document.getElementById("imgdragbox");
        box.innerHTML += '<div class="boximg"><img class="imgInfo" data-type="'+ name.split(".")[1]+'" src="' + this.result+ '"></div>';
        var bar = document.getElementById("m1");
        bar.value = bar.value + 1;
    }
    reader.readAsDataURL(file);
}


function submit(){
    var imglist = document.getElementsByClassName("imgInfo");
    // var imglist = fileList;
    console.log(imglist.length);
    var bar = document.getElementById("m1");
    bar.max = imglist.length - 1;
    bar.value = 0;
    for (var i = 0; i < imglist.length; i++){
        // imglist[i].src;
        var base64Str = imglist[i].src.split(",")[1];
        var typename = imglist[i].getAttribute("data-type")
        
                //console.log(base64Str)
        $.ajax({
            url: "http://110.42.252.237:6360/ImgUpload",
            data: {
                "type":typename,
                "base64file": base64Str
            },
            withCredentials: false,
            type: "post",
            success: function (res) {
                console.log("success")
                if(res == "complete"){
                    bar.value += 1;
                }

            }
        })
    }
    var box = document.getElementById("imgdragbox");
    box.innerHTML = ' ';
    //清空上传列表
    fileList = [];
}


function sendfile(file) {
    var sender = new FileReader();
    sender.onloadstart = function (e) {

        console.log("开始读取....");
    }
    sender.onprogress = function (e) {
        console.log("正在读取中....");
    }
    sender.onabort = function (e) {
        console.log("中断读取....");
    }
    sender.onerror = function (e) {
        console.log("读取异常....");
    }
    sender.onload = function (e) {
        console.log("成功读取....开始发送");
        upload(this.result);
    }

    sender.readAsArrayBuffer(file)
}

//文件上传
function upload(binary){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://110.42.252.237/ImgUpload:6360");
    xhr.overrideMimeType("application/octet-stream");
    //直接发送二进制数据
    if(xhr.sendAsBinary){
        xhr.sendAsBinary(binary);
    }else{
        xhr.send(binary);
    }
    
    // 监听变化
    xhr.onreadystatechange = function(e){
        if(xhr.readyState===4){
            if(xhr.status===200){
                // 响应成功       
            }
        }
    }
}