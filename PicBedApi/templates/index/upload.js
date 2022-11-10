var fileList = [];
box = document.getElementById("ViewBox");
var progressValue = {
    value: 0,
    max: 0,
};
var files = document.getElementById("file-input");
files.addEventListener("change", function (event) {
    renderFileList(files);
});

function EmitFileUpload() {
    files.click();
}

function upCancel() {
    // var up = document.getElementById("uppp");
    fileList = [];
    // up.style.cssText = "display: none;";
    // up.innerHTML = ' ';
    location.reload();
}

function CloseView() {
    // var up = document.getElementById("uppp");
    // console.log("close");
    fileList = [];
    // up.style.cssText = "display: none;";
    // up.innerHTML = ' ';
}

function setProcess(value) {
    var bar = document.getElementById("progressbar");
    bar.innerText = value + "%";
    bar.style.cssText = "width: " + value + "%;";
}

function renderFileList(files) {
    // console.log("filecount:" + files.files.length);
    progressValue.max += files.files.length;
    var listSize = files.files.length;
    for (var i = 0; i < files.files.length; i++) {
        fileList.push(files.files[i]);
        readfile(files.files[i]);
    }
}

function readfile(file) {
    var reader = new FileReader();
    var name = file.name;
    reader.onloadstart = function (e) {
        // // console.log("开始读取....");
    };
    reader.onprogress = function (e) {
        // // console.log("正在读取中....");
    };
    reader.onabort = function (e) {
        // // console.log("中断读取....");
    };
    reader.onerror = function (e) {
        // console.log("读取异常....");
    };
    reader.onload = function (e) {
        // console.log("成功读取....");
        // // console.log(e);
        var box = document.getElementById("imgdragbox");
        box.innerHTML +=
            '<div class="boximg"><img class="imgInfo" data-type="' +
            name.split(".")[1] +
            '" src="' +
            this.result +
            '"></div>';
        progressValue.value += 1;
        setProcess(parseInt((progressValue.value / progressValue.max) * 100));
    };
    reader.readAsDataURL(file);
}

function submit() {
    var imglist = document.getElementsByClassName("imgInfo");
    // var imglist = fileList;
    // console.log(imglist.length);
    progressValue.max = imglist.length;// - 1;
    progressValue.value = 0;
    setProcess(0);
    for (var i = 0; i < imglist.length; i++) {
        // imglist[i].src;
        var base64Str = imglist[i].src.split(",")[1];
        var typename = imglist[i].getAttribute("data-type");

        //// console.log(base64Str)
        $.ajax({
            url: RequestInfo + "/ImgUpload",
            data: {
                type: typename,
                base64file: base64Str,
            },
            withCredentials: false,
            type: "post",
            success: function (res) {
                // console.log("success");
                if (res == "complete") {
                    progressValue.value += 1;
                    setProcess(parseInt((progressValue.value / progressValue.max) * 100));
                }
                console.log("progressValue.value : " + progressValue.value)
                console.log("progressValue.max : " + progressValue.max)
                if (progressValue.value == progressValue.max) {
                    MyTips("success", "上传完成");
                    var box = document.getElementById("imgdragbox");
                    box.innerHTML = " ";
                    // setProcess(0);

                    //清空上传列表
                    fileList = [];
                }
            },
        });
    }

}

