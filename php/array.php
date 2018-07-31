<?php
	$arrbuah = array("jambu","jeruk","pisang","apel");
	echo $arrbuah[0];
	echo $arrbuah[3];

	$arrwarna = array();
	$arrwarna[] = "merah";
	$arrwarna[] = "biru";
	$arrwarna[] = "hijau";
	$arrwarna[] = "putih";
	echo $arrwarna[0];
	echo $arrwarna[2];

	$arrnilai = array("ani" => 80, "tim" => 90, "ana" => 75, "budi" => 85);
	echo $arrnilai['ani'];
	echo $arrnilai['tim'];
	print_r($arrnilai);
	krsort($arrnilai);
	print_r($arrnilai);

	$warna = array("Blue","Black","Red","Yellow","Green");
	echo "Menampilkan isi array dengan for : <br>";
	for ($i=0; $i<count($warna); $i++) {
		echo "do you like <font color=$warna[$i]>".$warna[$i]."</font> ?<br>";
	}
	echo "<br>menampilkan isi array dengan foreach : <br>";
	foreach ($warna as $ku) {
		echo "do you like <font color=$ku?".$ku."</font> ?,<br>";
	}
?>
