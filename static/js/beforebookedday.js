var thepar=document.querySelector("#prcd1");
var Final=localStorage.getItem('item')

var car=localStorage.getItem('car-selected')

thepar.addEventListener("click",dothing,false);

function dothing(e)
{	alert("hey")
	//alert(window.Final)
	alert(window.car)
	
 // var bl=new Blob([window.Final , "\n",window.car] , {type: "text/plain;charset=utf-8"});
	alert("hey")
	//saveAs(bl,"data.txt");

}


 