<?php
	$i = 1;
        while ($i <= 10) {
                echo $i++;
        }
        echo "<br><br>";

        $i = 1;
        while ($i <= 6) {
                echo "<h$i> pesawat $i</h$i>";
                $i++;
        }

	echo "\n\ndo while ========================================================\n";
	$i = 1;
	do {
		echo "$i ";
		$i += 2;
	} while($i <= 20);

?>
