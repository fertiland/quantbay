# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AnalyzeTradeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.CharField(max_length=64)
    code = models.CharField(max_length=16)
    stockname = models.CharField(db_column='stockName', max_length=64) # Field name made lowercase.
    tradetype = models.CharField(db_column='tradeType', max_length=32) # Field name made lowercase.
    algorithm = models.CharField(max_length=32)
    today = models.CharField(max_length=32)
    correctratio = models.DecimalField(db_column='correctRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    evaluationcumulativereturns = models.DecimalField(db_column='evaluationCumulativeReturns', max_digits=10, decimal_places=2) # Field name made lowercase.
    evaluationfinalportfolio = models.DecimalField(db_column='evaluationFinalPortfolio', max_digits=10, decimal_places=2) # Field name made lowercase.
    evaluationdrawdownduration = models.CharField(db_column='evaluationDrawdownDuration', max_length=64) # Field name made lowercase.
    evaluationmaxdrawdown = models.DecimalField(db_column='evaluationMaxDrawdown', max_digits=10, decimal_places=2) # Field name made lowercase.
    evaluationsharperatio = models.DecimalField(db_column='evaluationSharpeRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalavgprofit = models.DecimalField(db_column='finalAvgProfit', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalavgreturn = models.DecimalField(db_column='finalAvgReturn', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalmaxprofit = models.DecimalField(db_column='finalMaxProfit', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalmaxreturn = models.DecimalField(db_column='finalMaxReturn', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalminprofit = models.DecimalField(db_column='finalMinProfit', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalminreturn = models.DecimalField(db_column='finalMinReturn', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalprofitsstddev = models.DecimalField(db_column='finalProfitsStdDev', max_digits=10, decimal_places=2) # Field name made lowercase.
    finalreturnsstddev = models.DecimalField(db_column='finalReturnsStdDev', max_digits=10, decimal_places=2) # Field name made lowercase.
    finaltrades = models.IntegerField(db_column='finalTrades') # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime') # Field name made lowercase.
    industryname = models.CharField(db_column='industryName', max_length=64) # Field name made lowercase.
    valueatrisk = models.DecimalField(db_column='valueAtRisk', max_digits=10, decimal_places=2) # Field name made lowercase.
    hurst = models.DecimalField(db_column='hurst', max_digits=10, decimal_places=2) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'analyze_trade_info'

class BollingerParameters(models.Model):
    id = models.IntegerField(primary_key=True)
    instrument = models.CharField(max_length=16)
    bbandsperiod = models.IntegerField(db_column='bBandsPeriod') # Field name made lowercase.
    numstddev = models.IntegerField(db_column='numStdDev') # Field name made lowercase.
    create_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'bollinger_parameters'

class CombineTradeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.CharField(max_length=64)
    amplitude = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=16)
    sharperatio = models.DecimalField(db_column='sharpeRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    today = models.CharField(max_length=32)
    preprice = models.DecimalField(db_column='prePrice', max_digits=10, decimal_places=2) # Field name made lowercase.
    curprice = models.DecimalField(db_column='curPrice', max_digits=10, decimal_places=2) # Field name made lowercase.
    tradetype = models.CharField(db_column='tradeType', max_length=32) # Field name made lowercase.
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    portfilio = models.DecimalField(max_digits=10, decimal_places=2)
    algorithm = models.CharField(max_length=32)
    stockname = models.CharField(db_column='stockName', max_length=64) # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'combine_trade_info'

class TechnicalsTradeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.CharField(max_length=64)
    amplitude = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=16)
    sharperatio = models.DecimalField(db_column='sharpeRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    today = models.CharField(max_length=32)
    preprice = models.DecimalField(db_column='prePrice', max_digits=10, decimal_places=2) # Field name made lowercase.
    curprice = models.DecimalField(db_column='curPrice', max_digits=10, decimal_places=2) # Field name made lowercase.
    tradetype = models.CharField(db_column='tradeType', max_length=32) # Field name made lowercase.
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    portfilio = models.DecimalField(max_digits=10, decimal_places=2)
    algorithm = models.CharField(max_length=32)
    stockname = models.CharField(db_column='stockName', max_length=64) # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'technicals_trade_info'

class DualmaParameters(models.Model):
    id = models.IntegerField(primary_key=True)
    instrument = models.CharField(max_length=16)
    shortperiod = models.IntegerField(db_column='shortPeriod') # Field name made lowercase.
    longperiod = models.IntegerField(db_column='longPeriod') # Field name made lowercase.
    create_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'dualma_parameters'

class MacdParameters(models.Model):
    id = models.IntegerField(primary_key=True)
    instrument = models.CharField(max_length=16)
    fastperiod = models.IntegerField(db_column='fastPeriod') # Field name made lowercase.
    slowperiod = models.IntegerField(db_column='slowPeriod') # Field name made lowercase.
    signalperiod = models.IntegerField(db_column='signalPeriod') # Field name made lowercase.
    create_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'macd_parameters'

class Rsi2Parameters(models.Model):
    id = models.IntegerField(primary_key=True)
    instrument = models.CharField(max_length=16)
    entrysma = models.IntegerField(db_column='entrySMA') # Field name made lowercase.
    exitsma = models.IntegerField(db_column='exitSMA') # Field name made lowercase.
    rsiperiod = models.IntegerField(db_column='rsiPeriod') # Field name made lowercase.
    overboughtthreshold = models.IntegerField(db_column='overBoughtThreshold') # Field name made lowercase.
    oversoldthreshold = models.IntegerField(db_column='overSoldThreshold') # Field name made lowercase.
    create_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'rsi2_parameters'

class SummaryTradeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.CharField(max_length=64)
    totalcount = models.IntegerField(db_column='totalCount') # Field name made lowercase.
    buycount = models.IntegerField(db_column='buyCount') # Field name made lowercase.
    sellcount = models.IntegerField(db_column='sellCount') # Field name made lowercase.
    buyratio = models.DecimalField(db_column='buyRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    sellratio = models.DecimalField(db_column='sellRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    correctbuyratio = models.DecimalField(db_column='correctBuyRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    correctsellratio = models.DecimalField(db_column='correctSellRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    correctcompositeratio = models.DecimalField(db_column='correctCompositeRatio', max_digits=10, decimal_places=2) # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'summary_trade_info'

class VwapParameters(models.Model):
    id = models.IntegerField(primary_key=True)
    instrument = models.CharField(max_length=16)
    vwapwindowsize = models.IntegerField(db_column='vwapWindowSize') # Field name made lowercase.
    buythreshold = models.IntegerField(db_column='buyThreshold') # Field name made lowercase.
    sellthreshold = models.IntegerField(db_column='sellThreshold') # Field name made lowercase.
    create_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'vwap_parameters'

