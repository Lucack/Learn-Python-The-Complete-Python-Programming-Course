html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> <!-- modo como os computadores interpretam caracteres -->
    <title> Simple Website </title>
    <link rel="stylesheet" href="main.css">
</head>
<body class="dark-theme">  
    <h1> Task List </h1>
    <p id="msg"> Current tasks: </p> <!--paragrafo-->
    <ul> <!--Lista nao ordenada-->
        <li class="list"> Add  visual styles</li> <!--elementos da lista com classe lista -->
        <li class="list"> Add light and dark themes</li>
        <li> Enable switching the theme </li>
    </ul>
     
    <div>
        <button class="btn">Light</button>
    </div>   
</body>
</html>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html.parser")
print(soup.prettify())
print("\n \n")
print(soup.head)
print("\n \n")
print(soup.body)
print("\n \n")
print(soup.body.h1)
 
array = soup.find_all('li')
print(len(array))
print(array)
print(array[0])
print(array[1])
print(array[2])
