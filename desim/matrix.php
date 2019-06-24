<!DOCTYPE html>
<html>
<body onload="typeWriter()" style="background-color:black">

<p id="demo" style="color:#00e600;font-weight:bold;"></p>

<script>
var i = 0;
var txt = readTextFile("visualization/uvisual.txt");
var speed = 0;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("demo").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    var allText = "";
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                allText = rawFile.responseText;
            }
        }
    }
    rawFile.send(null);

    return allText;
}
</script>

</body>
</html>


