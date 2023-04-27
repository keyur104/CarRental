var car
var clicked
var element = document.getElementsByName("Butt");
for(i=0;i<30;i++)
{	
  element[i].onclick = function(e) 
	{
			window.car=e.target.value;	
			localStorage.setItem('car-selected',car);
			alert("hello" )
			alert(car)
			window.clicked=e.target.id;
			localStorage.setItem('clicked-item',clicked);
			window.location.href = "rentd";
}
}
