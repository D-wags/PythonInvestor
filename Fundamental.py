
# dl idra monthly price data from yahoo saved as IDRA.csv for numpy
# quandl name = bigdindacity
# pass = Hi#po###
# on fun 14
# on sci-kit 18
# API key = "-pj7iy-RshhTAs4i2J89"

import re
import csv
import os
import time
import urllib.request
import quandl
import pandas as pd

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

#pull quandl data
def grabQuandl():

    quandl.ApiConfig.api_version = '2015-04-09'
    quandl.ApiConfig.api_key = "-pj7iy-RshhTAs4i2J89"

    #mydata = quandl.get_table('ZACKS/FC', ticker='AAPL')
    mydata = quandl.get("WIKI/IDRA", trim_start="2005-12-12", authtoken="-pj7iy-RshhTAs4i2J89")

    #data is a pandas dataframe
    #print (mydata["Adj. Close"], mydata["Date"])

#grabQuandl()


# Better quandl pull
def stockPrices():
    path = "/Users/Drew/Desktop/intraQuarter"
    df = pd.DataFrame()
    statspath = path+"_KeyStats"

    errors = 0
    stock_list = ["IDRA", "GILD", "SGEN"]

    for stock in stock_list:
        try:
            ticker = stock
            name = "WIKI/"+ticker.upper()
            data = quandl.get(name, trim_start="2005-12-12", authtoken="-pj7iy-RshhTAs4i2J89")
            data[ticker.upper()] = data["Adj. Close"]

            df = pd.concat([df, data[ticker.upper()]], axis=1)
            print("SUCCESS")

        except Exception as e:
            errors +=1
            print(str(e), str(errors))
            time.sleep(10)

    df.to_csv("stock_prices.csv")

    # generate lists for plotting
    # need to generalize this to be independent of array size; unpacking perhaps?
    dates = []
    s1 = []
    s2 = []
    s3 = []

#IDRA,GILD,SGEN
    with open('stock_prices.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            dates.append(row["Date"])
            s1.append(row["IDRA"])
            s2.append(row["GILD"])
            s3.append(row["SGEN"])

    return [dates, s1, s2, s3]


# XX
#will take data from quandl and plot it....
def plotPrice(dates, prices):
    dates, prices = np.loadtxt(netIncomeAr, delimiter=', ', unpack=True,
                               converters={0: mdates.strpdate2num("%Y-%m-%d")})
    fig = plt.figure()
    ax1 = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=4)
    ax1.plot(dates, prices)
    plt.show()


# Function builds array of all BB holdings for HT analyis
# Got BB transactions from whalewisdom?
def getBakers():
    holdings = []
    with open('BBtransactions-2017-06-27_02_33_11.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            if float(row['Market Value']) > 0:
                print(row['Symbol']+": Shares held:", row['Shares Held'], "Market Value:", row['Market Value'], "% Change:", row['% Change'])
                holdings.append(row['Symbol'])
    return holdings


# Function builds array of all Russell3000 stocks for HT analyis
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


# Function scrapes basic stock data from yahoo finance
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


def makeGraph(dte, s1, s2):

    print(dte)
    # draw graph
    plt.plot(dte, s2, label="IDRA")
    #plt.plot(str(dte),s2,label="SGEN")

    plt.xlabel("DATE")
    plt.ylabel("PRICE($)")
    plt.title("Price vs Time")
    plt.legend()

    # show graph
    plt.show()


threeStocks = stockPrices()
#makeGraph(threeStocks[0], threeStocks[1], threeStocks[2])
