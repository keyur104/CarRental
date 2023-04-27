<html>
<body>
<form action="about.html" method="post">


<?php

$user=$_POST["username"];
$pswd=$_POST["pass"];

if ($user=="admin" and $pswd=="admin123")
{
	print("hey");

}	
	



?>

</form>
</body>
</html>


