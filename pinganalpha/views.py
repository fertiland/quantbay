# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime
import matplotlib
matplotlib.use('Agg')
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg

import datetime
import MySQLdb as mdb 
import urllib2
import matplotlib.pyplot as plt  
import numpy as np
import os
import sys


from pyalgotrade.technical import ma 
from pyalgotrade import dataseries
        
sys.path.append('/home/qipingli/stock/python/baiduPushService/pusher_python_sdk/python_sdk')
import baiduPushMessage
        
def queryBuyRatioBySection(sectionName, field='buyRatio'):
    # Obtain a database connection to the MySQL instance
    db_host = '192.168.1.105'
    db_user = 'root'
    db_pass = 'mysql106'
    db_name = 'security_finance'
    #MySQLdb.converters.conversions
    con = mdb.connect(db_host, db_user, db_pass, db_name)
    """Obtains a list of the ticker symbols in the database."""
    with con: 
        cur = con.cursor()
        cur.execute("""SELECT %s FROM summary_trade_info where section='%s' and (HOUR(createTime)>=9 and HOUR(createTime)<=15)""" % (field,sectionName))
        data = cur.fetchall()
        return [ float(d[0]) for d in data]

def queryCreateTimeBySection(sectionName, field='createTime'):
    # Obtain a database connection to the MySQL instance
    db_host = '192.168.1.105'
    db_user = 'root'
    db_pass = 'mysql106'
    db_name = 'security_finance'
    #MySQLdb.converters.conversions
    con = mdb.connect(db_host, db_user, db_pass, db_name)
    """Obtains a list of the ticker symbols in the database."""
    with con: 
        cur = con.cursor()
        cur.execute("""SELECT %s FROM summary_trade_info where section='%s' and (HOUR(createTime)>=9 and HOUR(createTime)<=15)""" % (field,sectionName))
        data = cur.fetchall()
        return [ datetime.datetime.strptime(str(d[0]), '%Y-%m-%d %H:%M:%S') for d in data]

def queryCorrectBuyRatioBySection(sectionName, field='correctBuyRatio'):
    # Obtain a database connection to the MySQL instance
    db_host = '192.168.1.105'
    db_user = 'root'
    db_pass = 'mysql106'
    db_name = 'security_finance'
    #MySQLdb.converters.conversions
    con = mdb.connect(db_host, db_user, db_pass, db_name)
    """Obtains a list of the ticker symbols in the database."""
    #SELECT (values) FROM myapp_my_object \ WHERE myapp_my_object.datetime_attr LIKE BINARY 2009-08-22%
    with con: 
        cur = con.cursor()
        cur.execute("SELECT %s FROM summary_trade_info where section='%s' and (HOUR(createTime)>=9 and HOUR(createTime)<=15) " % (field,sectionName))
        data = cur.fetchall()
        return [ float(d[0]) for d in data]

def buyRatioMatplotlib(request):
    fig, ax = plt.subplots()
    #f = figure(figsize=(16,6))
    #autodates = AutoDateLocator()  
    #yearsFmt = DateFormatter('%Y-%m-%d %H:%M:%S')  
    #f.autofmt_xdate()        #设置x轴时间外观  
    #ax.xaxis.set_major_locator(autodates)       #设置时间间隔  
    #ax.xaxis.set_major_formatter(yearsFmt)      #设置时间显示格式  
    #ax.set_xticks() #设置x轴间隔  
    #ax.set_xlim()   #设置x轴范围

    # 0.191、0.382、0.618、0.809
    todayBuyRatio = queryBuyRatioBySection('today')
    todayCorrectBuyRatio = queryCorrectBuyRatioBySection('today')
    todayTotalCount = queryBuyRatioBySection('today', 'totalCount')
    activeRatio = np.array(todayTotalCount)/100 * 1.382


    passedDaysTotalCount = queryBuyRatioBySection('passedDays', 'totalCount')
    pActiveRatio = np.array(passedDaysTotalCount)/500*1.91
    passedDaysBuyRatio = queryBuyRatioBySection('passedDays')
    passedDaysCorrectBuyRatio = queryCorrectBuyRatioBySection('passedDays')
    combineBuyRatio = queryBuyRatioBySection('combine')
    combineCorrectBuyRatio = queryBuyRatioBySection('combine')
    createTime = np.arange(0,len(todayBuyRatio))
    #createTime = matplotlib.dates.date2num(queryCreateTimeBySection('today'))
    ax.plot(createTime, activeRatio*np.array(todayBuyRatio), 'r', label='todayBuyRatio')
    ax.plot(createTime, activeRatio, 'y', label='todayActiveRatio')
    createTime = np.arange(0,len(combineBuyRatio))
    ax.plot(createTime, np.array(combineBuyRatio), 'g', label='combineBuyRatio')
    createTime = np.arange(0,len(passedDaysBuyRatio))
    #plt.plot(createTime, pActiveRatio*np.array(passedDaysBuyRatio), 'b')
    ax.plot(createTime, np.array(passedDaysBuyRatio), 'b', label='passedDaysBuyRatio')
    #ax.plot(createTime, np.array(combineBuyRatio)*np.array(passedDaysBuyRatio), 'c', label='combine*passedDays')
    wmOnes = np.ones_like(createTime)
    hwm = 0.8 * wmOnes
    mwm = 0.5 * wmOnes
    lwm = 0.2 * wmOnes
    ax.plot(createTime, hwm, 's')
    ax.plot(createTime, mwm, 's')
    ax.plot(createTime, lwm, 's')
    #fig = plt.buildFigure()
    #fig.set_size_inches(10, 8)
    #png = os.path.join("./", "buyRatio.png")
    #plt.savefig(png)
    #title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
    fig.set_size_inches(16, 6)
    ax.legend(loc='best')
    plt.grid(True)
    #plt.gcf().autofmt_xdate()

    bp = baiduPushMessage.BaiduPushMessage()
    if isBigChange(passedDaysBuyRatio,0.1) or isBigChange(combineBuyRatio, 0.05):
        plt.xlabel("big change!")
        bp.sendPushMessageToUser("Alert", "big change")  
    else:
        plt.xlabel("normal change")

    plt.ylabel("Follow the rule")
    if passedDaysBuyRatio[-2] >= 0.8 and passedDaysBuyRatio[-1] < 0.8:
        plt.title("start to sell")
        bp.sendPushMessageToUser("Alarm:Critical", "start to SELL")  
    elif passedDaysBuyRatio[-2] < 0.2 and passedDaysBuyRatio[-1] >= 0.2:
        plt.title("start to buy")
        bp.sendPushMessageToUser("Alarm:Critical", "start to BUY")  
    elif isBuyState(passedDaysBuyRatio, 0.618):
        plt.title("Buy")
        bp.sendPushMessageToUser("Message", "Buying")  
    elif isSellState(passedDaysBuyRatio, 0.618):
        plt.title("Sell")
        bp.sendPushMessageToUser("Message", "Selling")  
    else :
        plt.title("Do Not Action")
        bp.sendPushMessageToUser("Message", "Do Not Action")  
        
    canvas = FigureCanvasAgg(fig)        
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    matplotlib.pyplot.close(fig)
    return response

def sellRatioMatplotlib(request):
    f = figure(figsize=(16,6))

    # 0.191、0.382、0.618、0.809
    todayBuyRatio = queryBuyRatioBySection('today', 'sellRatio')
    todayCorrectBuyRatio = queryCorrectBuyRatioBySection('today', 'correctSellRatio')
    todayTotalCount = queryBuyRatioBySection('today', 'totalCount')
    activeRatio = np.array(todayTotalCount)/500*8.09
    passedDaysTotalCount = queryBuyRatioBySection('passedDays', 'totalCount')
    pActiveRatio = np.array(passedDaysTotalCount)/500*1.91
    passedDaysBuyRatio = queryBuyRatioBySection('passedDays', 'sellRatio')
    passedDaysCorrectBuyRatio = queryCorrectBuyRatioBySection('passedDays', 'correctSellRatio')
    combineBuyRatio = queryBuyRatioBySection('combine', 'sellRatio')
    combineCorrectBuyRatio = queryCorrectBuyRatioBySection('combine', 'correctSellRatio')
    createTime = np.arange(0,len(todayBuyRatio))
    #createTime = matplotlib.dates.date2num(queryCreateTimeBySection('today'))
    plt.plot(createTime, activeRatio*np.array(todayBuyRatio), 'r')
    plt.plot(createTime, activeRatio, 'y')
    createTime = np.arange(0,len(combineBuyRatio))
    plt.plot(createTime, np.array(combineBuyRatio), 'g')
    createTime = np.arange(0,len(passedDaysBuyRatio))
    #plt.plot(createTime, pActiveRatio*np.array(passedDaysBuyRatio), 'b')
    plt.plot(createTime, np.array(passedDaysBuyRatio), 'b')
    wmOnes = np.ones_like(createTime)
    hwm = 0.8 * wmOnes
    mwm = 0.5 * wmOnes
    lwm = 0.2 * wmOnes
    plt.plot(createTime, hwm, 's')
    plt.plot(createTime, mwm, 's')
    plt.plot(createTime, lwm, 's')
    #fig = plt.buildFigure()
    #fig.set_size_inches(10, 8)
    #png = os.path.join("./", "buyRatio.png")
    #plt.savefig(png)
    #title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
    plt.gcf().autofmt_xdate()
    plt.xlabel("Day")
    plt.ylabel("Ratio")
        
    canvas = FigureCanvasAgg(f)        
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    matplotlib.pyplot.close(f)
    return response

def correctCompositeRatioMatplotlib(request):
    f = figure(figsize=(16,6))

    # 0.191、0.382、0.618、0.809
    todayCorrectBuyRatio = queryCorrectBuyRatioBySection('today', 'correctCompositeRatio')
    passedDaysCorrectBuyRatio = queryCorrectBuyRatioBySection('passedDays', 'correctCompositeRatio')
    ownedCorrectBuyRatio = queryCorrectBuyRatioBySection('owned', 'correctCompositeRatio')
    hotCorrectBuyRatio = queryCorrectBuyRatioBySection('hot', 'correctCompositeRatio')
    combineCorrectBuyRatio = queryCorrectBuyRatioBySection('combine', 'correctCompositeRatio')

    sma = buildSMA(5, todayCorrectBuyRatio )
    createTime = np.arange(0,len(todayCorrectBuyRatio))
    plt.plot(createTime, sma, 'r')
    sma = buildSMA(5, passedDaysCorrectBuyRatio )
    createTime = np.arange(0,len(passedDaysCorrectBuyRatio))
    plt.plot(createTime, passedDaysCorrectBuyRatio, 'g')
    createTime = np.arange(0,len(ownedCorrectBuyRatio))
    #plt.plot(createTime, ownedCorrectBuyRatio, 'y')
    createTime = np.arange(0,len(hotCorrectBuyRatio))
    #plt.plot(createTime, hotCorrectBuyRatio, 'g')
    createTime = np.arange(0,len(combineCorrectBuyRatio))
    plt.plot(createTime, combineCorrectBuyRatio, 'b')

    #fig = plt.buildFigure()
    #fig.set_size_inches(10, 8)
    #png = os.path.join("./", "buyRatio.png")
    #plt.savefig(png)
    #title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
    plt.gcf().autofmt_xdate()
    plt.xlabel("Day")
    plt.ylabel("correctCompositeRatio")
        
    canvas = FigureCanvasAgg(f)        
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    matplotlib.pyplot.close(f)
    return response

def isBigChange(data, rate):
    for i in range(-6, 0):
        if abs(data[-1] - data[i]) >  rate: 
            return True
    return False

def isBuyState(data, rate):
    for i in range(-6, 0):
        if data[i] < rate: 
            return False
    return True

def isSellState(data, rate):
    for i in range(-6, 0):
        if data[i] > rate: 
            return False
    return True

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def buildSMA(period, values, smaMaxLen=dataseries.DEFAULT_MAX_LEN):
    seqDs = dataseries.SequenceDataSeries()
    ret = ma.SMA(seqDs, period, smaMaxLen)
    for value in values:
        seqDs.append(value)
    return ret

