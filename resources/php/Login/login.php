
<?php
    $login_feedback=NULL;
    if(isset($_POST['login']))
    {
        require 'db_connect.php';
        $email=$_POST['email'];
        $password=$_POST['passwd'];
        if($db_select)
        {
            $get_result="SELECT * FROM `create_acc` WHERE `email`= '$email'";
            $result_status=mysqli_query($connect,$get_result);
            $row_affected=mysqli_num_rows($result_status);
            if($row_affected!=0)
            {
                $row=mysqli_fetch_assoc($result_status);
                // if($row['status']=='INACTIVE')
                // {
                //     $login_feedback="<br>YOU HAVE REGISTERED. KINDLY CHECK YOUR E-MAIL FOR CONFIRMATION AND ACTIVATION ";
                // }
                if($password==$row['password'])
                {
                    //STARTING SESSION
                    session_start();
                    $_SESSION['id']=$email;
                    header("Location:../Mainpage/index.html");
                    exit();
                }
                    //CHECKING PASSWORD AND EMAIL FOR AUTHENTICATION
                //IF MATCH NOT FOUND
                else
                {
                    $login_feedback=" INVALID USERNAME/PASSWORD ";
                }
            }
            else
            {
                $login_feedback="EMAIL ID NOT REGISTERED<br>KINDLY REGISTER YOUR EMAIL FIRST";
            }
        }
        else
        {
            echo mysqli_error($select_db);
        }
    }
?>

<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Login</title>
		<link rel="stylesheet" href="../../css/style_login.css">
	</head>
	<body>
        <div class="feedback">
            <p><?php echo $login_feedback;?></p>
        </div>
		<div class="loginBox">
			<h2>Log In Here</h2>
			<form method="POST" action="#">
				<p>Email</p>
				<input type="email" name="email" placeholder="Email" required>
				<p>Password</p>
				<input type="password" name="passwd" placeholder="Password" required>
				<input type="submit" name="login" value="Log In">
				<a href="#">Forget Password</a>
			</form>
		</div>
	</body>
</html>
