import pandas as pd
import requests

url="https://rate.bot.com.tw/xrt?Lang=zh-TW"
res = pd.read_html(url)

#獲得表格
df = res[0]

#全部的row(行)以及0~5的index(列)
currency=df.iloc[:,:5]

#自訂欄位名稱
currency.columns=[u"幣別",u"現金匯率-本行買入",u"現金匯率-本行賣出",u"即期匯率-本行買入",u"即期匯率-本行賣出"]

#修正’幣別’欄位
currency[u"幣別"]=currency[u"幣別"].str.extract('\((\w+)\)')

AUD = currency[u"幣別"][3]
CashBuy = currency[u"現金匯率-本行買入"][3]
CashSell = currency[u"現金匯率-本行賣出"][3]

headers = {
        "Authorization": "Bearer " + "XXX權杖",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
params = {"message": "澳幣"+AUD+"\n"+"現金匯率-本行買入"+CashBuy+"\n"+"現金匯率-本行賣出"+CashSell}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200