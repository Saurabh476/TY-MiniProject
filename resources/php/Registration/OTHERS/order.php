<?php
session_start();
$email=$_SESSION['id'];
if(isset($_GET['id']))
{
    require 'db_connect.php';
    $id=$_GET['id'];
    $fetch_query="SELECT * FROM `price_list` WHERE `price_list`.`id`='$id'";
    $fetch_status=mysqli_query($connect,$fetch_query);
    $row=mysqli_fetch_assoc($fetch_status);
    $name=$row['name'];
    $price=$row['price'];
?>
<!DOCTYPE html>
<html>
    <head>
        <link type="text/css" href="../../css/style-mainpage.css" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../../css/Grid.css">
        <link rel="stylesheet" type="text/css" href="../../css/normalize.css">
        <link rel="stylesheet" type="text/css" href="../../../vendors/css/ionicons.min.css">
        <link href='http://fonts.googleapis.com/css?family=Lato:100,300,400,300italic' rel='stylesheet' type='text/css'>
        <script src="https://unpkg.com/ionicons@4.3.0/dist/ionicons.js"></script>
    </head>
    <body>
        <header>
            <nav class="nav">
                <div class="row">
                    <img src="../../css/img/logo.png" class="logo">
                    <ul class="main-nav">
                        <li><a href="../Login/logout.php">logout</a></li>
                    </ul>
                    <h1 class="heading">
                        Omnifood
                    </h1>
                    <hr>
                </div>
            </nav>
        </header>
        <section class="section-contact-form">
            <div class="row line">
                <h2 class="head"><center>ORDER INFO</center></h2>
            </div>
            <div class="row">
                <h2 class="head1"><center><?php echo "$name is Rs $price Only"?> per Unit</center></h2>
            </div>
            <div class="contact-box">
                <div class="row">
                    <form method="POST" action="order-confirm.php">
                        <div class="col span-1-of-3">
                            <label>NAME</label>
                        </div>
                        <div class="col span-2-of-3">
                            <input type="text" size="50" placeholder="YOUR NAME" name="name" required>
                        </div>
                    <div class="row">
                        <div class="col span-1-of-3">
                            <label>MOBILE NUMBER</label>
                        </div>
                        <div class="col span-2-of-3">
                            <input type="number" size="10" placeholder="MOBILE NUMBER" name="mobile_no" required>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col span-1-of-3">
                            <label>QUANTITY</label>
                        </div>
                        <div class="col span-2-of-3">
                            <select name="quantity">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                            </select>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col span-1-of-3">
                            <label>ADDRESS</label>
                        </div>
                        <div class="col span-2-of-3">
                            <textarea type="text" size="500" placeholder="ADDRESS" name="address" required></textarea>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col span-1-of-3">
                            <label>PIN CODE</label>
                        </div>
                        <div class="col span-2-of-3">
                            <input type="number" name="pin" size="6" placeholder="pin" required>
                        </div>
                        <div class="col span-2-of-3">
                            <input type="submit" name="submit" value="Submit">
                        </div>
                    </div>
                </form>
            </div> 
            </div>
        </section>        
        <footer class="footer">
            <div class="row">
                <div class="col span-1-of-2">
                    <ul class="footer-nav website-box">
                        <li><a href="#">ABOUT US</a></li>
                        <li><a href="#">PRESS</a></li>
                        <li><a href="#">BLOG</a></li>
                        <li><a href="#">IOS APP</a></li>
                        <li><a href="#">ANDROID APP</a></li>
                    </ul>
                </div>
                <div class="col span-1-of-2 icon-box">
                    <ul class="footer-nav1 footer-nav">
                        <li><a href="#"><ion-icon name="logo-facebook"></ion-icon></a></li>
                        <li><a href="#"><ion-icon name="logo-twitter"></ion-icon></a></li>
                        <li><a href="#"><ion-icon name="logo-googleplus"></ion-icon></a></li>
                        <li><a href="#"><ion-icon name="logo-instagram"></ion-icon></a></li>
                    </ul>
                </div>
            </div>
            <div class="row para-box">
                <p> COPYRIGHT &copy; 2015 BY OMNIFOOD. ALL RIGHTS RESERVED.</p>
            </div>
        </footer>
    </body>
</html>
<?php
}
        else
            header("Location:../Login/login.php?Login_first");
?>