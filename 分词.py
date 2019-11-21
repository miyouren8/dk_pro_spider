import jieba
import numpy as np
import matplotlib.pyplot as plt
num=0
lss=[]
ma={
    "骗子":0,
    "客服":0,
    "违约金":0,
    "申诉":0,
    "投诉":0,
    "退休":0,
    "合租":0
}
with open("tb.txt","r",encoding="utf-8")as file:
    for line in file:
        ssl=','.join(jieba.cut(line))
        ll=ssl.split(",")
        jk=[]
        for ds in ll:
            if ds in ma:
                nu=ma[ds]
                nu+=1
                ma[ds]=nu

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
    ax.set_xlabel(u'关键词')
    ax.set_ylabel(u'关键词个数')
    # title
    ax.set_title(u'蛋壳公寓搜索关键词频率直方图', bbox={'facecolor':'0.8', 'pad':5})
    plt.grid(True)
    plt.show()
    plt.close()

labels=ma.keys()
qua=ma.values()
print(ma)
draw_bar(labels,qua)