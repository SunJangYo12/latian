<html>
   <head><title>pengolahan form</title></head>
   <body>
	<FORM ACTION="" METHOD="POST" NAME="input">
	  nama anda : <input type="text" name="nama"><br>
	  <input type="submit" name="Input" value="Input">
	</FORM>
  </body>
</html>

<?php
if (isset($_POST['Input'])) {
	$nama = $_POST['nama'];
	echo "nama anda : <b>$nama</b>";
}
?>
