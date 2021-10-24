import requests
import pandas as pd

url = "https://gasoline.weiyuan.com.tw/"

data = requests.get(url)

#用pandas直接取得網址裡的表格
tables = pd.read_html(url)

#下週預估油價漲幅
Nextweek = tables[0]

#這週油價
Thisweek = tables[1]

NextweekPrice = Nextweek.iloc[0:4,3:4]

ThisweekPrice = Thisweek.iloc[0:1,:]

#取出當週油價
ThisweekPrice98 = str(ThisweekPrice["98無鉛"][0])
ThisweekPrice95 = str(ThisweekPrice["95無鉛"][0])
ThisweekPrice92 = str(ThisweekPrice["92無鉛"][0])
ThisweekPriceDiesel = str(ThisweekPrice["超級柴油"][0])

#取出下週油價
NextweekPrice98 = str(NextweekPrice["預估幅度"][0])
NextweekPrice95 = str(NextweekPrice["預估幅度"][1])
NextweekPrice92 = str(NextweekPrice["預估幅度"][2])
NextweekPriceDiesel = str(NextweekPrice["預估幅度"][3])


headers = {
        "Authorization": "Bearer " + "XXX權杖",
        "Content-Type": "application/x-www-form-urlencoded"
    }

params = {"message": "\n"
          "中油98汽油:"+ThisweekPrice98+"  預計漲幅:"+NextweekPrice98+"\n"+
          "中油95汽油:"+ThisweekPrice95+"  預計漲幅:"+NextweekPrice95+"\n"+
          "中油92汽油:"+ThisweekPrice92+"  預計漲幅:"+NextweekPrice92+"\n"+
          "超級柴油:"+ThisweekPriceDiesel+"  預計漲幅:"+NextweekPriceDiesel}
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
print(r.status_code)  #200
print("成功")