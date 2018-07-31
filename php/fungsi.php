<?php
function cetak_ganjil ($awal, $akhir) {
	echo "<b> ganjil dari $awal-$akhir : </b><br>";
	for ($i=$awal; $i<$akhir; $i++) {
		if ($i%2 == 1) {
			echo "$i ";
		}
	}
}
function luas_lingkaran($jari) {
	return 3.14* $jari * $jari;
}

cetak_ganjil(10, 50);
echo "luas lingkaran 30 :".luas_lingkaran(30);
?>
