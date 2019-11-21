areas=["bj","sz","sh","hz","tj","wh","nj","gz","cd"]
areasb=[u"北京",u"深圳",u"上海",u"杭州",u"天津",u"武汉",u"南京",u"广州",u"成都"]
ma={}
for line in areas:
    ma[line]=0
mun=0
with open("data.txt","r",encoding="utf-8") as file:
    for line in file:
        mun+=1
        nn=ma[line.split("#")[0]]
        nn+=1
        ma[line.split("#")[0]]=nn
print(ma)
print(mun)
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号
def draw_bar(labels,quants):
    width = 0.4
    ind = np.linspace(0.5,9.5,9)
    # make a square figure
    fig = plt.figure(1)
    ax  = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind-width/2,quants,width,color='green')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel(u'城市')
    ax.set_ylabel(u'租房数')
    # title
    ax.set_title(u'城市租房直方图', bbox={'facecolor':'0.8', 'pad':5})
    plt.grid(True)
    plt.show()
    plt.savefig("bar.jpg")
    plt.close()

labels   = areasb

quants   = ma.values()

draw_bar(labels,quants)