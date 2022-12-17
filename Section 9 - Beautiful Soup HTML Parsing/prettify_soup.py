from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><p> asfasfsdag<strong> Hello <a> Hello</html>","html.parser")
print(soup.prettify())

print(soup)
