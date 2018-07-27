<?php

//variable dan tipe data
$nim  = "54374573";
$nama = 'sunjang kuu';
$umur = 18;
$nilai= 85.53;
$status = TRUE;

echo "NIM : ".$nim."<br>";
echo "Nama : $nama<br>";
print "Umur : ".$umur; print "<br>";
printf ("Nilai : %.3f<br>", $nilai);
if ($status)
	echo "Status : Aktif";
else
	echo "Status : Tidak aktif";
