<?php

$vs = ['a','e','i','o','u','y'];
$cs = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'];

//echo rand(0,20);
//echo $vs[rand(0,count($vs)-1)];
//echo $cs[rand(0,count($cs)-1)];
$name = '';


$len = rand(3,8);
//echo "<br/>" . $len. "<br/>";

if (isset($_POST['GENERATE'])) {
	for ( $i = 0 ; $i <= $len ; $i++) {
		$j = rand(1,3);
		//echo $j . "<br/>";
		if ($j == 1) {
			$name = $name . $vs[rand(0,count($vs)-1)];
		}
		else {
			$name = $name . $cs[rand(0,count($cs)-1)];
		}
	}
}


echo <<<_END
<html><head></head>
<body>
<pre>
	<input type="submit" value="GENERATE">
		$name
</pre></body></html>
_END;


?>