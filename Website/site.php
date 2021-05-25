<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title></title>


</head>
<body>
    <?php

    $myfile = fopen("index.html", "r+") or die("Unable to open file!");
    echo fread($myfile,filesize("index.html"));
    fclose($myfile);
             
    ?>                              
</body>
</html>