mp={}
mmp={}
with open("data.txt","r",encoding="UTF-8") as file:
    for line in file:
        ls=line.split("##")
        if ls[0] in mp:
            mun=mp[ls[0]]
            mun=mun+int(ls[4])
            mp[ls[0]]=mun
            zioo=mmp[ls[0]]
            zioo+=1
            mmp[ls[0]]=zioo
        else:
            mp[ls[0]]=0
            mmp[ls[0]]=0
print(mp)
print(mmp)
#设置每个城市租房价格的平均值
avgmp={}
for key in mp:
    avgmp[key]=mp[key]/mmp[key]

print(avgmp)
import numpy as np
import matplotlib.pyplot as plt
def draw_bar(labels,quants):
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号
    width = 0.4
    ind = np.linspace(0.5,9.5,len(labels))
    # make a square figure
    fig = plt.figure(1)
    ax  = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind-width/2,quants,width,color='green')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel(u'城市名')
    ax.set_ylabel(u'城市租房价格平均值')
    # title
    ax.set_title(u'蛋壳公寓各个城市平均租房价格直方图', bbox={'facecolor':'0.8', 'pad':5})
    plt.grid(True)
    plt.show()
    plt.close()
areas=["bj","sz","sh","hz","tj","wh","nj","gz","cd"]
areasb=[u"北京",u"深圳",u"上海",u"杭州",u"天津",u"武汉",u"南京",u"广州",u"成都"]
citymap={}
yz=zip(areas,areasb)
citymap=dict((yw,zw) for yw,zw in yz)
#x轴和y轴
labels=[]
qua=[]
for key in citymap:
    labels.append(citymap[key])
    qua.append(avgmp[key])
draw_bar(labels,qua)