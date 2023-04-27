
total=0
var theparent3=document.querySelector("#calday");
theparent3.addEventListener("click",thing,false);
function thing(e)
{
		spn=document.querySelector("#total");
		//const { clicked1 } = require('./linked.js')
	    text =document.getElementById("day").value;
	    window.total=text * localStorage.getItem('clicked-item');
	    
	    alert(total);
	    localStorage.setItem('item',total);
		 window.location.href = "procdday";
		 
		
}
