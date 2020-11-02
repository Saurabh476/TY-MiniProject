<?php
    require("db_connect.php");
    if(isset($_POST['submit']))
    {
        
?>

<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="../../css/Grid.css">
        <link rel="stylesheet" type="text/css" href="../../css/normalize.css">
        <link rel="stylesheet" type="text/css" href="../../css/login-confirm.css" >
        <link href='http://fonts.googleapis.com/css?family=Lato:100,300,400,300italic' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <header>
            <div class="mainpage">
                <div class="row head">
                    <h1> THANKYOU FOR YOUR FEEDBACK!!!</h1>
                    <h2></h2>
                </div>
                <div class="message">
                    <p>WE'LL GET BACK IN TOUCH WITH YOU AS SOON AS POSSIBLE<br>
                        REGARDS.<br>
                        <a href="../../../index.html" class="btn btn-btn">CLICK HERE</a>
                    </p>
                </div>
            </div>
        </header>
    </body>
</html>
<?php
}
else
    header("Location:../../../");
?>