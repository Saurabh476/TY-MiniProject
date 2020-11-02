<?php
    $id = $_GET['id'];
    $fp=fopen('area_name.txt','w');
    fwrite($fp,"$id");
    fclose($fp);

    header('Location:../1-2.py');
?>