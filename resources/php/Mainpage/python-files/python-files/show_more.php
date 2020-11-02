<?php
    $id = $_GET['id'];
    $fp=fopen('costly-afford.txt','w');
    fwrite($fp,"$id");
    fclose($fp);

     header('Location:../2-2.py');
?>