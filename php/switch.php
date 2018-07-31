<?php

	$day = date("D");
        switch ($day) {
                case 'Sun' : $hari = "Minggu"; break;
                case 'Mon' : $hari = "senin"; break;
                case 'Tue' : $hari = "selasa"; break;
                case 'Wed' : $hari = "rabu"; break;
                case 'Thu' : $hari = "kamis"; break;
                case 'Fri' : $hari = "jumat"; break;
                case 'Sat' : $hari = "sabtu"; break;
                default    : $hari = "kiamat";
        }
        echo "Hari ini hari <b>$hari</b>";
?>

