var thepar=document.querySelector("#prcd");
var Final=localStorage.getItem('item')
//var fso = new ActiveXObject("Scripting.FileSystemObject");
//var fh = fso.OpenTextFile("static\data.txt");
var car=localStorage.getItem('car-selected')

thepar.addEventListener("click",dothing,false);

function dothing(e)
{
	alert(window.Final)
	//var Final=localStorage.getItem('item');
    alert(window.car)
 
var blob=new Blob([window.Final , "\n",window.car] , {type: "text/plain;charset=utf-8"});
alert("hey")
saveAs(blob,"data.txt");
alert("hello")
}


 