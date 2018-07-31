<?php
	$data = file_get_contents("php://input");
	$json = json_decode($data, true);
	foreach ($json as $key => $value) {
		if (!is_array($value)) {
			echo "The $key is $value\n";
		}
		else {
			foreach ($value as $key => $val) {
				echo "The $key is $value\n";
			}
		}
}
?>
