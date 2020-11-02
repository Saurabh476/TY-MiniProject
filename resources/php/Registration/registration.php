<?php

//REGISTRATION PAGE
	require("db_connect.php");
    
    require '../../../vendor/autoload.php';
    
    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;
    
    $registration_feedback=NULL;
     if(isset($_POST['signup']))
    {
        $first_name=$_POST['first_name'];
        $sur_name=$_POST['sur_name'];
        $mobile_no=$_POST['mobile_no'];
        $email=$_POST['email'];
        $password=$_POST['passwd'];
        $cpassword=$_POST['cpasswd']; 
        //ERROR CHECK IN FIRSTNAME
        if(!preg_match("/^[a-zA-Z]*$/",$first_name))
        {
            $registration_feedback="IMPROPER FIRST NAME";
        }
        //ERROR CHECK IN SURNAME 
       elseif (!preg_match("/^[a-zA-Z]*$/",$sur_name))
        {
           $registration_feedback="IMPROPER SUR NAME";
        }
        //PASSWORD MATCHING
        elseif($password==$cpassword)
        {
            if($db_select)
            {
                //EMAIL CONFIRMATION 
                //CREATING HASH FROM RANDOM STRING VALUE
                $str="qwertyuiopasdfghklxhcjglhfglfgjhjkklsdoeurtnmvncxchvopejrlzxcvbnms";
                $str=str_shuffle($str);
                $token=substr($str,0,30);
                //STORING VALUES IN DATABASE WITH STATUS = 0
                $insert="INSERT INTO `create_acc` (`first_name`, `sur_name`, `mobile_no`, `email`, `password`) VALUES ('$first_name', '$sur_name', '$mobile_no', '$email', '$password')";
                 $check_insert=mysqli_query($connect,$insert);
                
                // if($check_insert)
                // {
                //     //USING PHPMailer TO SEND MAILS ON EMAIL

                //     $mail = new PHPMailer(true);
                //     $mail->IsSMTP(); // enable SMTP
                //     $mail->SMTPAuth = true; // authentication enabled
                //     $mail->SMTPSecure = 'ssl'; // secure transfer enabled REQUIRED for Gmail
                //     $mail->Host = "ssl://smtp.gmail.com";
                //     $mail->Port = 465; // or 587
                //     $mail->IsHTML(true);
                //     $mail->Username = "studenthelper27@gmail.com";
                //     $mail->Password = "student27";
                //     $mail->SetFrom("studenthelper27@gmail.com","OmiFood");
                //     $mail->Subject = "ACCOUNT CONFIRMATION";
                //     $mail->Body="PLEASE CLICK ON THE LINK BELOW TO VERIFY YOUR EMAIL ADDRESS.<BR>
                //         <a href='http://localhost/WPL/resources/php/Registration/confirm.php?email=$email&token=$token'>CLICK HERE</a>";
                //     $mail->AddAddress("$email");
                //     if($mail->send())
                //     {
                //         $registration_feedback="CONFIRMATION MAIL SENT<br>CHECK YOUR EMAIL ID<bR>
                //         CLICK ON THE ACTIVATION LINK<br> TO ACTIVATE YOUR ACCOUNT<br>
                //         THANK YOU FOR REGISTERING ";
                //     }
                //     else
                //         $registration_feedback="KINDLY CHECK YOUR EMAIL. IT DOES NOT EXIST";
                // }
                // else
                // {
                //     $registration_feedback="KINDLY USE DIFFERENT EMAIL ID<br> YOUR ENTERED EMAIL ID IS <br>ALREADY
                //      REGISTERED WITH US";    
                // }
            }
            else
            {
                $registration_feedback="SITE IS IN DEVELOPMENT<br>KINDLY TRY AFTER SOME TIME";
            }
        }
        else   
        {
            $registration_feedback="PASSWORD AND CONFIRM PASSWORD DOESN'T MATCH <br> RETRY";
        }
    }
?>

<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Registraion</title>
		<link rel="stylesheet" href="../../css/style_registration.css">
	</head>
	<body>
        <div class="feedback">
            <p><?php echo $registration_feedback;?></p>
        </div>
		<div class="registrationBox">
			<h2>Sign Up Here</h2>
			<form method="POST" action="#">
                <p>First Name</p>
                <input type="text" name="first_name" placeholder="First Name" required>
                <p>Surname</p>
                <input type="text" name="sur_name" placeholder="Last Name" required>
                <p>Mobile Number</p>
                <input type="number" name="mobile_no" placeholder="Mobile Number" required>
                <p>Email</p>
                <input type="email" name="email" placeholder="Email Id" required>
                <p>Password</p>
                <input type="password" name="passwd" placeholder="Password" required>
                <p>Confirm Password</p>
                <input type="password" name="cpasswd" placeholder="Confirm Password" required>

                <button type="submit" name="signup" >SIGN UP</button>
			</form>
		</div>
	</body>
</html>
