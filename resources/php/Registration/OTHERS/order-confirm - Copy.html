<?php
	require 'db_connect.php';

    require '../../../vendor/autoload.php';
    
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;


    session_start();
    $email=$_SESSION['id'];
   
    if(isset($_POST['submit']))
    {
        
        $order_feedback=NULL;
        $name=$_POST['name'];
        $mobile_no=$_POST['mobile_no'];
        $address=$_POST['address'];
        $pin=$_POST['pin'];
        $quantity=$_POST['quantity'];
        $insert="INSERT INTO `order-info` (`name`, `mobile_no`, `quantity`, `address`, `pin`) VALUES ('$name', '$mobile_no', '$quantity', '$address', '$pin')";
        $check_insert=mysqli_query($connect,$insert);

        if($check_insert)
                {
                    //USING PHPMailer TO SEND MAILS ON EMAIL
                    $mail = new PHPMailer(true);
                    $mail->IsSMTP(); // enable SMTP
                    $mail->SMTPAuth = true; // authentication enabled
                    $mail->SMTPSecure = 'ssl'; // secure transfer enabled REQUIRED for Gmail
                    $mail->Host = "ssl://smtp.gmail.com";
                    $mail->Port = 465; // or 587
                    $mail->IsHTML(true);
                    $mail->Username = "studenthelper27@gmail.com";
                    $mail->Password = "student27";
                    $mail->SetFrom("studenthelper27@gmail.com","OmiFood");
                    $mail->Subject = "ORDER CONFIRMATION";
                    $mail->Body="Your order will reach you within 30 minutes<br>Regards Omnifood ;";
                    $mail->AddAddress("$email");
                    if($mail->send())
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
                    <h1> YEAH!!!</h1>
                    <h2>ORDER CONFIRMED!!!!</h2>
                </div>
                <div class="message">
                    <p>Yummy Food is Yours.<br>
                        Your Order will reach you within 30 minutes.<br>
                        <a href="mainpage.php" class="btn btn-btn">CLICK HERE</a>
                    </p>
                </div>
            </div>
        </header>
    </body>
</html>
<?php
      }
  }
}
?>