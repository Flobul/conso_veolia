<?php
require_once '/var/www/html/core/php/core.inc.php';
if (count($argv)!=4){
    echo "Php : unexpected number of arguments\r\n";
    die;
}
echo "Php argv3: " . $argv[3] . "\r\n\r\n";
echo "Php : using jeedom cmd ".$argv[1]." for total index and ".$argv[2]." for daily conso\r\n";


$data = json_decode($argv[3]);
echo "Php : ".count($data)." lines\r\n";
foreach ($data as $value){
    echo "date=".$value[0] . " total=" .$value[1] ." jour=".$value[2]."\r\n";
    # Total en L
    $cmd = cmd::byId($argv[1]);
    $cmd->addHistoryValue($value[1], $value[0]);
    #Journalier en L
    $cmd = cmd::byId($argv[2]);
    $cmd->addHistoryValue($value[2], $value[0]);
}

?>