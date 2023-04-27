<?php
$con=mysqli_connect("localhost","root","","carrental");
$records=mysqli_query($con,"select * from carcust");


?>
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Table V01</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util2.css">
	<link rel="stylesheet" type="text/css" href="css/main2.css">
<!--===============================================================================================-->
</head>
<body>
	
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<div class="table100">
					<table>
						<thead>
							<tr class="table100-head">
								<th class="column1">ContactNO</th>
								<th class="column2">Name</th>
								<th class="column3">Email</th>
								<th class="column4">CarName</th>
								<th class="column5">PickLoc</th>
								<th class="column6">DropLoc</th>
								<th class="column7">Rent</th>

							</tr>
						</thead>
						<tbody>
								
<?php
while($ep=mysqli_fetch_assoc($records))
{
	echo"<tr>";
	echo"<td>".$ep['contactno']; "</td>";
	echo"<td>".$ep['custName'] ;"</td>";
	echo"<td>".$ep['email'] ;"</td>";
	echo"<td>".$ep['carName'] ;"</td>";
	echo"<td>".$ep['pickLoc'] ;"</td>";
	echo"<td>".$ep['dropLoc'] ;"</td>";
	echo"<td>".$ep['estRent'] ;"</td>";
	echo"</tr>";
}




?>

<!--===============================================================================================-->	
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

</body>
</html>

