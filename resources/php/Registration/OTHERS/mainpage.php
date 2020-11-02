//MAINPAGE

<?php
session_start();
$email=$_SESSION['id'];
if($_SESSION)
{
?>
    <!DOCTYPE HTML>
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
                        <li><a href="#">Orders</a></li>
                        <li><a href="../Login/logout.php">logout</a></li>
                    </ul>
                    <h1 class="heading">
                        Omnifood
                        <hr>
                    </h1>
                </div>
            </nav>
        </header>
        <section>
            <div class="row">
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/chapati1.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">TANDOORI<br>Rs 14/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=1 ">Order Now</a></li>
                        </ul>
                    </div>
                </div >
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/chapati2.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">PARATHA<br>Rs 20/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=2">Order Now</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/chapti3.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">CHAPATI<br>Rs 12/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=3">Order Now</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/daal.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">DAAL<br>Rs 99/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=4">Order Now</a></li>
                        </ul>
                    </div>
                </div >
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/omni-special.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">MIX-DISH<br>Rs 149/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=5">Order Now</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/paneer.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">PANNER<br>Rs 149/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=6">Order Now</a></li>
                        </ul>
                    </div>
                </div>
            </div><div class="row">
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/pasta.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">PASTA<br>Rs 79/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=7">Order Now</a></li>
                        </ul>
                    </div>
                </div >
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/noodles.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">NOODLES<br>Rs 69/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=8">Order Now</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/dosa.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">DOSA<br>Rs 79/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=9">Order Now</a></li>
                        </ul>
                    </div>
                </div>
            </div><div class="row">
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/coke.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">COKE<br>Rs 20/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=10">Order Now</a></li>
                        </ul>
                    </div>
                </div >
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/desertimg3.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">JAMUN<br>Rs 79/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=11">Order Now</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col span-1-of-3">
                    <div class="images"><img src="../../css/img/desertimg1.jpg"></div>
                    <div class="info">
                        <ul>
                            <li><h3 class="info">DESERT<br>Rs 49/-</h3></li>
                            <li><a class="btn btn-full" href="order.php?id=12">Order Now</a></li>
                        </ul>
                    </div>
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
    {
        header("Location:../Login/login.php?Login_First");
        exit();
    }
?>