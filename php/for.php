<?php
/* contoh 1 */
for ($i = 1; $i <= 10; $i++) {
	echo "$i ";
}
echo "<br><br>";
/* contoh 2 */
for ($i = 1; ; $i++) {
	if ($i > 10) {
		break;
	}
	echo "$i ";
}
echo "<br><br>";

/* contoh 3 */
$i = 1;
for (; ; ) {
	if ($i > 10) {
		break;
	}
	echo "$i ";
	$i++;
} echo "<br><br>";

/* contoh 4 */
for ($i = 1; $i <= 10; print "$i ", $i++);

echo "\n\nbreak continue ==============================================\n";
for ($i=1; $i<=10; $i++) {
	if ($i == 5)
		continue;
	if ($i == 8)
		break;
	echo "$i ";
}
?>
