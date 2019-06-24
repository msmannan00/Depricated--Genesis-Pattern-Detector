<!DOCTYPE html>
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
	                        <h1 class="hero-title mt-0">Matbot | Regex Info</h1>
	                        <p class="hero-paragraph">List of all Regex Obtain against your query. It can also be extended to see actual data</p>
						</div>
                    </div>
                      <div class="list-group">
                <form action="genericDisplay.php" method="post" enctype="multipart/form-data">
                          <?php 
                          $result = file_get_contents('visualization/rvisual.txt');
                          if(strlen($result)<=2)
                          {
                              return;
                          }
                          $resultset = explode("-newstart-",$result);
                                  
                          $counter=0;
                          foreach($resultset as $item) 
                          {
                              $resultsetItem = explode("|",$item);
                              if(sizeof($resultsetItem)>1)
                              {
                                 $link = $resultsetItem[0];
                                 if(strlen($link)>=80)
                                 {
                                     $link = substr($link,0,80);   
                                 }

                                 echo "<input type=\"text\" name=\"title\" value=\"Matbot | Patterns\" hidden>";
                                 echo "<input type=\"text\" name=\"desc\" value=\"Following is the data or code snippets extracted using regex\" hidden>";
                                 echo "<input type=\"text\" name=\"data\" value=\"".urlencode(htmlspecialchars($resultsetItem[1]))."\" hidden>";

                                 echo "<a href=\"#\" onclick=\"$(this).closest('form').submit()\" class=\"list-group-item\" style=\"text-decoration: none\">";
                                 echo "<p class=\"list-group-item-text\" style=\"text-decoration: none\">".$link."</p>";
                                 echo "</a>";
                                 $counter++;
                                 if(sizeof($resultset)<=$counter+1)
                                 {
                                       break;
                                 }
                              }
                          }               
                          ?>

                    </form>
                      </div>
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
