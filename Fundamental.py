# on vid 10
import re
import time
import urllib.request

def getRussell3000():
    tickers = []
    inFile = open("Russell3000.txt", "r").read()
    lines = inFile.split("\n")

    try:
        for line in lines:
            splitter = line.split(" ")
            ticker = splitter[-1]
            tickers.append(ticker)
            print(ticker)

    except Exception as e:
        print(e)

    return tickers


Bakers = ['aqxp', 'ghdx', 'incy', 'amrn', 'blcm', 'bcrx', 'avxs', 'rigl', 'sgmo', 'anab', 'trvn']

# GET MARKET DATA
def TickerStats(ticker):

    try:
        req = urllib.request.Request("https://finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker)
        with urllib.request.urlopen(req) as response:


            sourceCode = response.read()
            print("-----------------------------")
            sourceCode = str(sourceCode)

            price = sourceCode.split('Mb(-4px) D(ib)" data-reactid="36">')[1].split('</span>')[0]
            print("{} price: {}".format(ticker,str(price)))

            cap = sourceCode.split('Ta(end)" data-reactid="21">')[1].split('</td>')[0]
            print("{} market Cap: {}".format(ticker, str(cap)))

            outFile = open("html_text.txt", 'w')
            outFile.write(sourceCode)
            outFile.close()

            regex = 'Fz\(s\) Fw\(500\) Ta\(end\)" data-reactid="3[01][0-9]">'
            yrHi = sourceCode.split('52 Week High')
            yrHi = re.split(regex, yrHi[1])
            yrHi = yrHi[1].split("</td>")[0]
            print("52 week high: {}".format(str(yrHi)))

            regex = 'Fz\(s\) Fw\(500\) Ta\(end\)" data-reactid="3[12][0-9]">'
            yrLow = sourceCode.split('52 Week Low')
            yrLow = re.split(regex, yrLow[1])
            yrLow = yrLow[1].split("</td>")[0]
            print("52 week low: {}".format(str(yrLow)))

    except Exception as inst:
        print("-----------------------------")
        print(ticker - " - Error!!")
        print(inst)


getRussell3000()

#TickerStats("idra")
#for stock in Bakers:
#    TickerStats(stock)
#    time.sleep(1)
