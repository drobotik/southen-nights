<?php 
$output = shell_exec(escapeshellcmd("./discount.py")); 
if(is_array($output)) {
	var_dump(json_decode($output, true));
} else print $output;


