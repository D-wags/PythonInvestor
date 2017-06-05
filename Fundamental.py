import re
import time
import urllib.request

Bakers = ['aqxp', 'ghdx', 'incy', 'amrn', 'blcm', 'bcrx', 'avxs', 'rigl', 'sgmo', 'anab', 'trvn']

# GET MARKET DATA
def TickerKeyStats(ticker):

    #try:
    req = urllib.request.Request("https://finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker)
    with urllib.request.urlopen(req) as response:

        try:
            sourceCode = response.read()
            print("-----------------------------")
            sourceCode = str(sourceCode)

            price = sourceCode.split('Mb(-4px) D(ib)" data-reactid="36">')[1].split('</span>')[0]
            print(ticker + " price:", str(price))

            cap = sourceCode.split('Ta(end)" data-reactid="21">')[1].split('</td>')[0]
            print(ticker + " market Cap:", str(cap))

            outFile = open("html_text.txt", 'w')
            outFile.write(sourceCode)

            regex = 'Fz\(s\) Fw\(500\) Ta\(end\)" data-reactid="3[01][0-9]">'
            yrHi = sourceCode.split('52 Week High')
            yrHi = re.split(regex, yrHi[1])
            yrHi = yrHi[1].split("</td>")[0]
            print("52 week high: " + str(yrHi))

            regex = 'Fz\(s\) Fw\(500\) Ta\(end\)" data-reactid="3[12][0-9]">'
            yrLow = sourceCode.split('52 Week Low')
            yrLow = re.split(regex, yrLow[1])
            yrLow = yrLow[1].split("</td>")[0]
            print("52 week low: " + str(yrLow))




        except:
            print("-----------------------------")
            print(ticker - " - Error!!")

#TickerKeyStats("idra")


for stock in Bakers:
    TickerKeyStats(stock)
    time.sleep(1)
