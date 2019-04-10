<?php
session_start();


// $get_url = $_SESSION['search_text'];
// exec("py main.py $get_url 2>&1", $aResult);
if (isset($_POST['Submit'])) { 
    $get_text = $_POST['search_text'];
    exec("py main.py $get_text 2>&1", $aResult);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8' /> 
    <title>Document</title>
</head>
<body>
    <form action="" method="post">
    <input type="text" name="search_text"/>
    <input type="submit" name="Submit" value="Submit" />
    </form>
</body>
</html>

