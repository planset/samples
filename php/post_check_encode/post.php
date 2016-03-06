<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=shift-jis">
  </head>
<body>
<?php

$data = $_POST['data'];

echo "hogehoge\n";
echo "$data\n";
echo mb_convert_encoding($data, "SJIS", "UTF-8") . "\n";
echo mb_convert_encoding($data, "SJIS", "auto") . "\n";
echo mb_convert_encoding($data, "UTF-8", "auto") . "\n";

?>
</body>
</html>
