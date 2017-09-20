<?php 
$output = shell_exec(escapeshellcmd("./discount.py 2")); // order_id
if(is_array($output)) {
	var_dump(json_decode($output, true));
} else print $output;


