<?php
    if(isset($_GET['email']) && isset($_GET['token']))
    {
       require 'db_connect.php';
       $email=$_GET['email'];
       $token=$_GET['token'];

       $update="UPDATE `create_acc` SET `status` = 'ACTIVE' WHERE `create_acc`.`email` = '$email' AND `create_acc`.`token`='$token'";
       $update_status=mysqli_query($connect,$update);
       if($update_status)
        {    
            $fetch_update="SELECT * FROM `create_acc` WHERE `create_acc`.`token`='$token'";
            $fetch_update_status=mysqli_query($connect,$fetch_update);
            $row=mysqli_fetch_assoc($fetch_update_status);
            if( $row['status']=="ACTIVE")
            {
                header('Location:reg-confirm.html');
            }
            else
            {
                header('Location:../../../index.html');
            }
        }
       else
            echo"ERRO IN UPDATE STATUS";

    }
    else
        header("Location:../index.html?FIRST_CREATE_ACCOUNT");
?>