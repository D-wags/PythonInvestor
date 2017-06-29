# on vid 13
# dl idra monthly price data from yahoo saved as IDRA.csv for numpy

import re
import csv
import time
import urllib.request
import quandl

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

# quandl name = bigdindacity
# pass = Hi#po###
# API key = "-pj7iy-RshhTAs4i2J89"

def grabQuandl():

    quandl.ApiConfig.api_version = '2015-04-09'
    quandl.ApiConfig.api_key = "-pj7iy-RshhTAs4i2J89"


    #mydata = quandl.get_table('ZACKS/FC', ticker='AAPL')
    mydata = quandl.get("WIKI/IDRA", trim_start="2005-12-12")

    # works data is a pandas dataframe I think
    print (len(mydata))

#grabQuandl()

#will take data from quandl and plot it....
def plotPrice(dates, prices):
    dates, prices = np.loadtxt(netIncomeAr, delimiter=', ', unpack=True,
                               converters={0: mdates.strpdate2num("%Y-%m-%d")})
    fig = plt.figure()
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=4)
    ax1.plot(dates, prices)
    plt.show()



def getBakers():
    holdings = []
    with open('BBtransactions-2017-06-27_02_33_11.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            if float(row['Market Value']) > 0:
                print(row['Symbol']+": Shares held:", row['Shares Held'], "Market Value:", row['Market Value'], "% Change:", row['% Change'])
                holdings.append(row['Symbol'])
    return holdings



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

#Bakers = ['aqxp', 'ghdx', 'incy', 'amrn', 'blcm', 'bcrx', 'avxs', 'rigl', 'sgmo', 'anab', 'trvn']

# GET MARKET DATA on tickers
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

#Bakers = getBakers()
# Russells = getRussell3000()

#TickerStats("idra")
#for stock in Bakers:
#    TickerStats(stock)
#    time.sleep(1)

# draw graph
plt.plot([1,2,3],[5,7,4])
# show graph
plt.show()
