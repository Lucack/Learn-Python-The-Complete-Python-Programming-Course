import re
import urllib.request

try:
    #https://g1.globo.com/previsao-do-tempo/mg/belo-horizonte.ghtml
    url = "https://g1.globo.com/previsao-do-tempo/"
    sigla = input("Digite a sigla do estado: ")
    cid = input("Agora, digite o nome da cidade: ")

    #sigla,cid = "mg","betim"
    cidPrint = cid
    cid = cid.replace(" ","-")


    url+= sigla+"/"+cid+".ghtml"

    data = urllib.request.urlopen(url).read()
    data = data.decode("utf-8")
    #print(data)

    m = re.search('class="forecast-header__summary"',data)
    start = m.start()
    end = m.end() + 50
    data1=data[start:end]
    #print(data1)

    m = re.search('summary">',data1)
    start = m.start() + len('summary">')
    m = re.search('.</p>',data1)
    end = m.start()+1

    weather = data1[start:end]
    print("A previsão do tempo para hoje em", cid.capitalize(),"-", sigla.upper(),"é: \n ",weather)

except:
    print("Desculpe, não temos informações sobre este lugar, confira e tente novamente")