import time
from urllib.request import urlopen

Bakers = ['aqxp', 'ghdx', 'incy', 'amrn', 'blcm', 'avxs', 'hrtx', "alxp", "bcrx", "rigl", "sgmo", "anab", "aevi", "trvn"]

# GET MARKET CAP
def TickerKeyStats(ticker):

    try:
        print("-----------------------------")
        sourceCode = urlopen("https://finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker).read()
        sourceCode = str(sourceCode)

        try:
            cap = sourceCode.split('Ta(end)" data-reactid="21">')[1].split('</td>')[0]
            print(ticker + " market Cap:", str(cap))

            price = sourceCode.split('Mb(-4px) D(ib)" data-reactid="36">')[1].split('</span>')[0]
            print(ticker + " price:", str(price))

            yrLo = sourceCode.split('Ta(end)" data-reactid="315">')[1].split('</td>')[0]
            print(ticker + " annual low:", str(yrLo))

            yrHi = sourceCode.split('Ta(end)" data-reactid="308">')[1].split('</td></tr>')[0]
            print(ticker + " annual high:", str(yrHi))

        except:
            print(ticker + " ERROR")


        print("")
    except:
        print("-----------------------------")
        print(ticker - " - Error!!")

#TickerKeyStats("idra")
for stock in Bakers:
    TickerKeyStats(stock)
    time.sleep(1)

