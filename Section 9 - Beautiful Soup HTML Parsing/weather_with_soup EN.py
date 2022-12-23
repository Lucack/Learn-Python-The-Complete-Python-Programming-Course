from bs4 import BeautifulSoup
import requests


# https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml

try:
    url = "https://g1.globo.com/previsao-do-tempo/"
    sigla = input("Enter the state abbreviation: ")
    cid = input("Now, enter the name of the city: ")

    #sigla,cid = "sp","sao-paulo"
    cidPrint = cid
    sigla = sigla.replace(" ","")
    cid = cid.replace(" ","-",1)
    cid = cid.replace(" ","")



    url+= sigla+"/"+cid+".ghtml"

    data =  requests.get(url)
    #data= data.text
    soup = BeautifulSoup(data.text,"html.parser")

    day = soup.find('p',{'class':'forecast-header__date'}).string
    local = soup.find('p',{'class':'forecast-header__place'}).string
    weather = soup.find('p',{'class':'forecast-header__summary'}).string


    maxTemp = soup.find('div',{'class':'forecast-today__temperature forecast-today__temperature--max'}).contents
    minTemp = soup.find('div',{'class':'forecast-today__temperature forecast-today__temperature--min'}).contents

    print("The weather forecast for",day, "in", local,"is: \n  - ", weather)
    print("  -  With a maximum", maxTemp[0])
    print("  -  And minimum", minTemp[0])



except:
      print("Desculpe, não temos informações sobre este lugar, confira e tente novamente")