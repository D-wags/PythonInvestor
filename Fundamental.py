import re
import time
from urllib.request import urlopen

Bakers = ['aqxp', 'ghdx', 'incy', 'amrn', 'blcm', 'bcrx', 'avxs', 'rigl', 'sgmo', 'anab', 'trvn']

# GET MARKET CAP
def TickerKeyStats(ticker):

    try:
        print("-----------------------------")
        sourceCode = urlopen("https://finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker).read()
        sourceCode = str(sourceCode)


        price = sourceCode.split('Mb(-4px) D(ib)" data-reactid="36">')[1].split('</span>')[0]
        print(ticker + " price:", str(price))

        cap = sourceCode.split('Ta(end)" data-reactid="21">')[1].split('</td>')[0]
        print(ticker + " market Cap:", str(cap))

        # a = re.split(r"\W", s)
        yrHi = re.split('Ta(end)" data-reactid="3[01][49]>', sourceCode)
        print(len(yrHi))


        # yrHi = sourceCode.split('Fz(s) Fw(500) Ta(end)" data-reactid="3')[1].split('</td>')[0]
        # print(ticker + " annual high:", str(yrHi[4:]))


    except:
        print("-----------------------------")
        print(ticker - " - Error!!")

# TickerKeyStats("idra")
for stock in Bakers:
    TickerKeyStats(stock)
    time.sleep(1)

