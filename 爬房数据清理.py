import re
import time
import requests
import pandas as pd
from retrying import retry
from concurrent.futures import ThreadPoolExecutor
import ssl
from bs4 import BeautifulSoup
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive"
}
start=time.clock() #开始计时
@retry(stop_max_attempt_number=8)#设置最大重试次数
def network_programming(data):
    url=data[2]
    ssl._create_default_https_context = ssl._create_unverified_context
    web=requests.get(url,headers=headers)
    print(data[1])
    web.encoding='utf-8'
    html=web.text
    web.close()
    return html,data
def multithreading(plist):
    event=[]
    with ThreadPoolExecutor(max_workers=8) as executor:
        for result in executor.map(network_programming,plist,chunksize=10):
            event.append(result)
    return event
datalist=[]
with open("data.txt","r",encoding="UTF-8") as file:
    for line in file:
        dlist=line.split("##")
        lis=[dlist[0],dlist[4],dlist[5]]
        datalist.append(lis)

print(datalist)
print(len(datalist))
#记录访问失败的链接
badlist=[]
def runda(evs):
    for web,data in evs:
        sssp=BeautifulSoup(web,features="html.parser")
        area=sssp.select(".room-detail-sq")
        if  len(area)>1:
            data[2]=area[0].text.strip()
        else:
            badlist.append(data)
            continue
        with open("cleardata.txt","a",encoding="UTF-8") as file:
            for line in data:
                file.write(line+"##")
            file.write("\n")
            file.flush()
events=multithreading(datalist)
runda(events)
while len(badlist)!=0:
    jlist=badlist
    print("#######################坏数据为："+str(len(badlist)))
    badlist=[]
    evss=multithreading(jlist)
    runda(evss)
end=time.clock() #计时结束
print("清洗完成 用时：",end-start,'s')