<?php

	$data = ['name' => 'Sunjang', 'umur' => 18];
	header('Content-Type: application/json');
	echo json_encode($data);
?>
