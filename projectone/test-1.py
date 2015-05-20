import ConfigParser
import tushare as ts
config = ConfigParser.ConfigParser()
config.readfp(open('e:\lu_git\python_stock\projectone\stlist.ini'))

a=str(config.get("listname","name"))

b=a

print "%s" %(a)

print b

ts.get_hist_data(a)

df = ts.get_hist_data(a)

df.to_csv('c:/day/'+a+'.csv')


df.to_csv('c:/day/'+a+'.csv',columns=['open','high','low','close','volume','price_change','p_change','ma5','ma10','ma20','v_ma5','v_ma10','v_ma20','turnover'])