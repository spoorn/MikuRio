<?php

	DEFINE ('DB_HOST', 'vergil.u.washington.edu');
	DEFINE ('DB_USER', 'root');
	DEFINE ('DB_PASSWORD', 'c67lw3ld');
	DEFINE ('DB_NAME', 'mikurio');
	DEFINE ('DB_PORT', '6534');

	$dbc = new MySQLi(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT);

	if($dbc->connect_error)
	{
	   echo "Not connected, error: ".$dbc->connect_error;
	}
	else
	{
	   echo "Connected.";
	}

?>