import time
from urllib.request import urlopen

sp500 = ['a', 'aa', 'aabv', 'abc', 'abt', 'ace']

# GET MARKET CAP
def TickerKeyStats(ticker):
    try:
        sourceCode = urlopen("https://finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker).read()
        sourceCode = str(sourceCode)
        pbr = sourceCode.split('Ta(end)" data-reactid="21">')[1].split('</td>')[0]
        print("Market Cap:", str(pbr))
    except:
        print("Error!!")

TickerKeyStats("IDRA")

