<?php

$path = $_SERVER['DOCUMENT_ROOT'];
$tmp  = "temp/smarty";
require "$path/Smarty/Smarty.class.php";

$smarty = new Smarty();
$smarty->template_dir = "$path/$tmp/templates";
$smarty->compile_dir  = "$path/$tmp/templates_c";
$smarty->cache_dir    = "$path/$tmp/chache";
$smarty->config_dir   = "$path/$tmp/configs"; 

$vs = ['a','e','i','o','u','y'];
$cs = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'];

echo rand(0,20);


$smarty->assign('name', $name);
$smarty->assign('title',"00 - Name Generator");
$smarty->display("00.tpl");
?>