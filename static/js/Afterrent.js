

var total=0
var theparent2=document.querySelector("#calkm");
theparent2.addEventListener("click",dothing,false);
function dothing(e)
{
	  
		spn=document.querySelector("#total");
		//const { clicked } = require('./linked.js')	
	    text =document.getElementById("km").value;
	    
	     window.total=text * localStorage.getItem('clicked-item');
	    confirm(total);
	    localStorage.setItem('item',total);
	    //return(text);
		window.location.href= "procdkms";
		 
		
}

//document.getElementById("total").innerHTML="total";