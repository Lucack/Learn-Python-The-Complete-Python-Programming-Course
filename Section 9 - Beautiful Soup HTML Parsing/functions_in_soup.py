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

print("")
head_tag = soup.head
print(head_tag)

print("")
    # .contents  # inside the head for example
a = head_tag.contents
print(a)

   # for

print("")
print("children: ----")
print("")
body_tag = soup.body
for i in body_tag.children: # separately
    print(i)



print("")
print("descendants: ----")
print("")

for i in body_tag.descendants: # separately
    print(i)


    # .string
print(head_tag.title)
print(head_tag.title.string) # Simple Website

    # .parent