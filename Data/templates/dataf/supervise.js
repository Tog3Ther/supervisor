window.onload = function() {
    var inputdata = document.getElementById("inputdata");
    var supervisebtn = document.getElementById("supervisebtn");
    document.getElementById("enter").onclick = function() {
    splitt(inputdata.value,"-")
    }
    function splitt(string,separator){
        arraydata = string.split(separator);
        console.log(arraydata);
        var timestart = Date.parse(arraydata[0]);
        var timeend = Date.parse(arraydata[1]);
        console.log(timestart,timeend);
        var tap = "https://supervisor.pallas-ludens.com/contributions/users?page=1&perPage=8000&timestampStartInMs="+ timestart + "&timestampEndInMs=" + timeend + "&groupName=MDY";
        var tag = "https://supervisor.pallas-ludens.com/contributions/users?page=1&perPage=8000&timestampStartInMs="+ timestart + "&timestampEndInMs=" + timeend + "&groupName=MDY";
        var btn1 = document.createElement("a");
        var btn2 = document.createElement("a");
        btn1.className = "btn btn-dark";
        btn1.innerHTML = "Tap Tool";
        btn1.target = "_blank";
        btn1.id = "taptool";
        btn1.style.marginLeft = "10px";
        btn1.href = tap;

        btn2.className = "btn btn-dark";
        btn2.innerHTML = "Tag Tool";
        btn2.target = "_blank";
        btn2.id = "tagtool";
        btn2.style.marginLeft = "10px";
        btn2.href = tag;
        if(supervisebtn.childNodes.length == 0){
            supervisebtn.appendChild(btn1);
            supervisebtn.appendChild(btn2);
        }
        else{
            supervisebtn.removeChild(supervisebtn.firstChild);
            supervisebtn.removeChild(supervisebtn.firstChild);
            supervisebtn.appendChild(btn1);
            supervisebtn.appendChild(btn2);
        }
        

    }
    

}
