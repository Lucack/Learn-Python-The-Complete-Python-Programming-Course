import re
import urllib.request
try:
    #https://www.google.com/finance/quote/BTC-BRL
    url = "https://www.google.com/finance/quote/"
    stock = input("Enter your stock: ")

    #stock = "BTC-BRL"
    url += stock
    #print(url)

    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8") # bits in bytes

    #print(data1)

    #The last closing price</div></span><div class="P6K39c">88,243.49
    m=re.search('class="YMlKec fxKbKc">',data1)
    #print(m)
    start = m.start()
    end = m.end() + 10
    newstr = data1[start:end]
    #print(newstr)

    m=re.search('"YMlKec fxKbKc">',newstr)
    start = (m.start())+len('"YMlKec fxKbKc">')
    m=re.search('<',newstr)
    end = m.end()-1
    price = newstr[start:end]
    print("The value of", stock,"is",price)
except:
    print(" Este programa funciona apenas para cryptomoedas, tente digitar o par, como por exemplo: BTC-BRL")