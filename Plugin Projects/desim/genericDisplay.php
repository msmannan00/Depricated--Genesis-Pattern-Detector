<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Matbot</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=IBM+Plex+Sans:400,600" rel="stylesheet">
    <link rel="stylesheet" href="dist/css/style.css">
	<script src="https://unpkg.com/animejs@3.0.1/lib/anime.min.js"></script>
    <script src="https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js"></script>
    <link rel="shortcut icon" type="image/png" href="dist/images/logo.png"/>

</head>
    
    <body class="is-boxed has-animations">
    <div class="body-wrap">

        <main>
            <section class="hero">
                <div class="container">
                    <div class="hero-inner">
						<div class="hero-copy">
	                        <h1 class="hero-title mt-0"><?php echo $_POST["title"]; ?></h1>
	                        <p class="hero-paragraph"><?php echo $_POST["desc"]; ?></p>
						</div>
                    </div>
                    <?php $decoded_data = urldecode($_POST["data"]); echo "<p style=\"word-wrap: break-word;padding-bottom:45px;border:1px solid;padding-left:50px;padding-top:50px;border-radius: 10px;color:white;overflow-wrap: break-word\">".str_replace("_____","<br><br><br>",$decoded_data)."</p>"; ?>
                    <br><br>
                </div>
            </section>

            
        </main>

        <footer class="site-footer" style="margin-top: -200px">
            <div class="container">
                <div class="site-footer-inner">
                    <div class="brand footer-brand">
						<a href="#">
							<img class="header-logo-image" src="dist/images/logo.svg" alt="Logo">
						</a>
                    </div>
                     &nbsp;                    <div class="footer-copyright">&copy; 2019 Solid, all rights reserved</div>
                </div>
            </div>
        </footer>
    </div>

    <script src="dist/js/main.min.js"></script>
</body>
</html>
