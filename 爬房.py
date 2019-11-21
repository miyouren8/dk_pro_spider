import re
import time
import requests
import pandas as pd
from retrying import retry
from concurrent.futures import ThreadPoolExecutor
import ssl
from bs4 import BeautifulSoup
areas=["bj","sz","sh","hz","tj","wh","nj","gz","cd"]
# areas=["bj"]
def gethtml(url):
    page = requests.get(url)
    page.content.decode()
    html = page.text
    return html
ssl._create_default_https_context = ssl._create_unverified_context
url="https://www.dankegongyu.com/room/bj?page=2"
# url="https://www.dankegongyu.com/room/bj?search=1&search_text=TBD%E4%B8%87%E7%A7%91%E5%A4%A9%E5%9C%B0&page=2"
start=time.clock() #开始计时

plist=[]
gnum=50
for i in range(1,gnum):
    for line in areas:
        plist.append(str(i)+":"+line)
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive"
}

@retry(stop_max_attempt_number=8)#设置最大重试次数
def network_programming(ssdd):
    pps=ssdd.split(":")
    print(ssdd)
    url='https://www.dankegongyu.com/room/'+pps[1]+'?page='+str(pps[0])
    web=requests.get(url,headers=headers)
    web.encoding='utf-8'
    return web,pps
def multithreading():
    event=[]
    with ThreadPoolExecutor(max_workers=10) as executor:
        for result in executor.map(network_programming,plist,chunksize=10):
            event.append(result)
    return event
def getdata(line):
    fan=[]
    fan.append(line.select(".r_lbx_cena a")[0].text.strip().replace(" ","").replace("\n",""))
    fan.append(line.select(".r_lbx_cena .r_lbx_cena")[0].text.strip().replace(" ","").replace("\n",""))
    fan.append(line.select(".r_lbx_cenb")[0].text.strip().replace(" ","").replace("\n",""))
    fan.append(line.select(".r_lbx_moneya .ty_b")[0].text.strip().replace(" ","").replace("\n",""))
    fan.append(line.select(".r_lbx_money .lk_more")[0].attrs["href"])
    for con in line.select(".r_lbx_cenc span"):
        fan.append(con.text.strip())
    return fan
even=multithreading()
nu=1;
for web,pps in even:
    if pps[0]==str(gnum):
        nu=0
    bd=BeautifulSoup(web.text,features="html.parser")
    web.close()
    lis=bd.select(".r_lbx")
    eventlist=[]
    with ThreadPoolExecutor(max_workers=10) as executor:
        for result in executor.map(getdata,lis,chunksize=10):
            eventlist.append(result)
    with open('data.txt',"a+",encoding="utf-8")  as file:
        for lis in eventlist:
            file.write(pps[1]+"##")
            for lin in lis:
                lin.encode()
                file.write(lin.strip().replace(" ","").replace("\n","")+"##")
                file.flush()
            file.write("\n")
end=time.clock() #计时结束
print("爬取完成 用时：",end-start,'s')