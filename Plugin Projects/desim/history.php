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
        <header class="site-header">
            <div class="container">
                <div class="site-header-inner">
                    <div class="brand header-brand">
                        <h1 class="m-0">
							<a href="#">
								<img class="header-logo-image" src="">
                            </a>
                        </h1>
                    </div>
                </div>
            </div>
        </header>

        <main>
            <section class="hero">
                <div class="container">
                    <div class="hero-inner">
						<div class="hero-copy">
	                        <h1 class="hero-title mt-0">Matbot | History</h1>
	                        <p class="hero-paragraph">List of all Commands and queries currently supported by our system</p>
						</div>
                    </div>
                      <div class="list-group">
                          <?php 
                              $fn = fopen("Command/cmd_backup.txt","r");

                              while(! feof($fn))  
                              {
                                $result = fgets($fn);
                                if($result=="")
                                {
                                    break;
                                }
                                echo "<a href=\"#\" class=\"list-group-item\" style=\"text-decoration: none\">";
                                echo "<p class=\"list-group-item-text\" style=\"text-decoration: none\">".$result."</p>";
                                echo "</a>";
                              }

                              fclose($fn);                          
                          ?><br><br><br>
                      </div>
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
