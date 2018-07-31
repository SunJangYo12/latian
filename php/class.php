<?php

$str = <<<EOD
ini string bebas
karena ada eod
ok
oke.
EOD;

class foo {
	var $foo;
	var $bar;
	function foo() {
		$this->foo = 'FOO';
		$this->bar = array('bar1', 'bar2', 'bar3');
	}
}

$foo = new foo();
$name = 'sunjang';

echo <<<EOT
<u>$str</u><br>
My name is "<b>$name</b>". I am printing some <b>$foo->foo</b>.
Now, I am printing some <b>{$foo->bar[1]}</b>.
This should print a capital 'A': \x41
EOT;

?>
