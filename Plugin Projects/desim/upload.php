<?php
$target_dir = "Source/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
file_put_contents("Command/cmd.txt", "");
file_put_contents("Command/cmd_backup.txt", "");
file_put_contents("visualization/fvisual.txt", "");


$files = glob('Source/*'); // get all file names
foreach($files as $file){ // iterate files
  if(is_file($file))
    unlink($file); // delete file
}

// Check if file already exists
if (file_exists($target_file)) {
    unlink($target_file);
    header("Location: http://localhost/desim/");
    die();
    $uploadOk = 0;
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000000) {
    header("Location: http://localhost/desim/error.php?mes=Sorry, your file is too large.");
    die();
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "zip" ) {
    header("Location: http://localhost/desim/error.php?mes=Sorry, only zip files are allowed.");
    die();
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    header("Location: http://localhost/desim/error.php?mes=Sorry, your file was not uploaded.");
    die();
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        header("Location: http://localhost/desim/");
        die();
    } else {
        header("Location: http://localhost/desim/error.php?mes=Sorry, there was an error uploading your file.");
        die();
    }
}
?>