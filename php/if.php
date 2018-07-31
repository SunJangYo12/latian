<?php
	$nilai = 50;
	if ($nilai >= 60) {
		echo "1. if==================================\n";
		echo "nilai anda $nilai, anda lulus\n\n";
	} else {
		echo "2. if else=============================\n";
		echo "nilai anda $nilai, anda gagal\n\n";
	}

	echo "3. memeriksa username dan password=====================================\n";
	$user = "ahmad";
	$pass = "123";
	if ($user == "ahmad" && $pass == "123") {
		echo "login berhasil\n\n";
	} else {
		echo "login gagal\n\n";
	}

	echo "4. fungsi isset()====================================\n";
	$user = "";
	if (!isset($user)) {
		echo "variabel tidak ada/belum terbentuk\n\n";
	} else {
		echo "variabel ada\n\n";
	}

	echo "5. if istimewa ==========================================\n";
	$tahun = date("Y");
	$kabisat = ($tahun%4 == 0) ? "KABISAT" : "BUKAN KABISAT";
	echo "tahun <b>$tahun</b> $kabisat";
?>
