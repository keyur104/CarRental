

//var theparent=document.querySelector("#thebtneve1");
var clicked,clicked1;
var car
//let a=[1,2,3,4,5,6,7,8,9];
var element = document.getElementsByName("Button");
for(i=0;i<20;i++)
{
		
	element[i].onclick = function(e)
	{
	window.car=e.target.value	
	localStorage.setItem('car-selected',car);
	alert("hello" )
	window.clicked=e.target.id;
	localStorage.setItem('clicked-item',clicked);
	window.location.href = "rent";
}
}






//theparent.addEventListener("click",dosomething,false);
/*function dosomething(e)
{
		
		 window.clicked=e.target.id;
		 alert(clicked);
		 //alert ("hello " + clickedItem)
		 localStorage.setItem('clicked-item',clicked);
		 
		 window.location.href = "rent";
		 
		
}


var theparent1=document.querySelector("#thebtneve");
theparent1.addEventListener("click",dosome,false);

function dosome(e)
{
		 window.clicked1=e.target.id;
		 alert (clicked1)
		  localStorage.setItem('clicked-item',clicked1);
		 //module.exports = { clicked1 };
		 window.location.href = "rentd";
		
	
}
*/

/*var theparent2=document.querySelector("#calkm");
theparent2.addEventListener("click",dothing,false);
function dothing(e)
{
	  
	 	var tar=window.clicked;
		//const { clicked } = require('./linked.js')	
	    text =document.getElementById("km").value;
	    
	    var total=8 * text;
	    alert(total);
	    //return(text);
		window.location.href= "procdkms";
		 
		
}
*/

/*var theparent3=document.querySelector("#calday");
theparent3.addEventListener("click",thing,false);
function thing(e)
{
	  	//tar=window.clicked1;
		//const { clicked1 } = require('./linked.js')
	    text =document.getElementById("day").value;
	    //var total=1200 * text;
	    alert(text);
		 window.location.href = "procdday";
		 
		
}

*/

/*function getVal(id)
{
	
	text =document.getElementById(id).value;
	//var total=clicked * text;	
	//var queryString = "?para1=" + total;
	window.location.href = "procdkms" ;	
}

function getValue(id)
{
	
	text = document.getElementById(id).value;
	//var total1=clicked1 * text;
	//var queryString = "?para1=" + total1;
	window.location.href = "procdday" ;	
}
*/