<html>
   <head><title>Login here </title></head>
   <head>
	<form action="" method="POST" name="input">
	   <h2> Login here...</h2>
	   username : <input type="text" name="username"><br>
	   password : <input type="password" name="password"><br>
	   <input type="submit" name="Login" value="Login">
	   <input type="reset" name="reset" value="Reset">
	</form>
     </body>
</html>

<?php
	if (isset($_POST['Login'])) {
		$user = $_POST['username'];
		$pass = $_POST['password'];
		if ($user == "admin" && $pass == "123") {
			echo "<h1> Login berhasil ^_^ </h1>";
		} else {
			echo "<h1> Login gagal !!!! </h1>";
		}
	}

?>
