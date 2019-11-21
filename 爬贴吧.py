from bs4 import BeautifulSoup
import time
import requests
from retrying import retry
from concurrent.futures import ThreadPoolExecutor
import ssl
#设置pages数
pages=[]
for i in range(100):
    pages.append(i*50)
ssl._create_default_https_context = ssl._create_unverified_context
start=time.clock() #开始计时
headers={
    'User-Agent':'Mozi'
}

@retry(stop_max_attempt_number=8)#设置最大重试次数
def network_programming(ssdd):
    print(ssdd)
    url="https://tieba.baidu.com/f?kw=%E8%9B%8B%E5%A3%B3%E5%85%AC%E5%AF%93&ie=utf-8&pn="+str(ssdd)
    web=requests.get(url,headers=headers)
    web.encoding='utf-8'
    return web
def multithreading():
    event=[]
    with ThreadPoolExecutor(max_workers=10) as executor:
        for result in executor.map(network_programming,pages,chunksize=10):
            event.append(result)
    return event
even=multithreading()
for web in even:
    bea=BeautifulSoup(web.text,features="html.parser")
    j_thread_list=bea.select(".j_thread_list")
    info=[]
    for line in j_thread_list:
        ttl=line.select(".threadlist_title")
        title=''
        subtitle=""
        for li in ttl:
            title=li.text.strip()
        ttl=line.select(".threadlist_detail .threadlist_abs")
        for li in ttl:
            subtitle=li.text.strip()
        info.append(title+"##"+subtitle)
    with open('tb.txt',"a+",encoding="utf-8")  as file:
        for lis in info:
            "".encode().decode()
            file.write(str(lis).replace(" ","").replace("\n",""))
            file.write("\n")
            file.flush()
end=time.clock() #计时结束
print("爬取完成 用时：",end-start,'s')