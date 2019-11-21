import json
#每个城市的map值
#加载清洗过的数据
mmp={}
areamap={}
with open("clear.json","r",encoding="UTF-8") as file:
    mmp=json.loads(file.read(),encoding="UTF-8")
with open("clear2.json","r",encoding="UTF-8") as file:
    areamap=json.loads(file.read(),encoding="UTF-8")
import numpy as np
import matplotlib.pyplot as plt
def draw_bar(labels,quants,mun,city):
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号
    width = 0.4
    ind = np.linspace(0.5,9.5,len(labels))
    # make a square figure
    fig = plt.figure(mun)
    ax  = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind-width/2,quants,width,color='green')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel(city)
    ax.set_ylabel(u'城市租房价格平均值')
    # title
    ax.set_title(u'蛋壳公寓'+city+'城市平均租房价格直方图', bbox={'facecolor':'0.8', 'pad':5})
    plt.grid(True)
    plt.show()
#生成城市map对照表
areas=["bj","sz","sh","hz","tj","wh","nj","gz","cd"]
areasb=[u"北京",u"深圳",u"上海",u"杭州",u"天津",u"武汉",u"南京",u"广州",u"成都"]
citymap={}
yz=zip(areas,areasb)
citymap=dict((yw,zw) for yw,zw in yz)
nn=0
for citykey in citymap:
    nn+=1
    cim=mmp[citykey]
    cimy=areamap[citykey]
    labels=[]
    aux=[]
    #生成各个城市区域名序列和城市区域价格平均值序列
    for k  in cim:
        labels.append(k)
        aux.append(cimy[k]/cim[k])
    print(len(labels))
    print(len(aux))
    #开始画图
    draw_bar(labels,aux,nn,citymap[citykey])

