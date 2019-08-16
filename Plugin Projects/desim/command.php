<?php 
    $fp_back = fopen('Command/cmd_backup.txt', 'a');
    $fp = fopen('Command/cmd.txt', 'a');

    if($_POST["command"]=="clear_history" || $_POST["command"]=="clear_all")
    {
        file_put_contents("Command/cmd_backup.txt", "");
        file_put_contents("visualization/fvisual.txt", "");
        file_put_contents("visualization/rvisual.txt", "");
        file_put_contents("visualization/mvisual.txt", "");
        file_put_contents("visualization/pvisual.txt", "");
        if($_POST["command"]=="clear_history")
        {
            header("Location: http://localhost/desim/");
            die();
        }
    }


    fwrite($fp, $_POST["command"]."\n");
    fwrite($fp_back, $_POST["command"]."\n");
    fclose($fp);
    fclose($fp_back);

    if($_POST["command"]=="compile")
    {
        file_put_contents("visualization/fvisual.txt", "");
    }

 
    header("Location: http://localhost/desim/");
    die();
?>
