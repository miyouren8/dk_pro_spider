import json
mmp={}
areamap={}
with open("data.txt","r",encoding="UTF-8") as file:
    for line in file:
        mp={}
        summp={}
        ls=line.split("##")
        if ls[0] in mmp:
            mp=mmp[ls[0]]
            if ls[5] in mp:
                num=mp[ls[5]]
                num+=1
                mp[ls[5]]=num
                mmp[ls[0]]=mp
            else:
                #地区计数器
                mp[ls[5]]=1
                mmp[ls[0]]=mp
        else:
            mp[ls[5]]=1
            mmp[ls[0]]=mp
        if ls[0] in areamap:
            summp=areamap[ls[0]]
            if ls[5] in summp:
                num=summp[ls[5]]
                num+=int(ls[4])
                summp[ls[5]]=num
                areamap[ls[0]]=summp
            else:
                summp[ls[5]]=int(ls[4])
                areamap[ls[0]]=summp
        else:
            summp[ls[5]]=int(ls[4])
            areamap[ls[0]]=summp
print(mmp)
print(areamap)
#清洗完毕
#载入各个城市区域中的租房个数
with open("clear.json","w",encoding="UTF-8") as file:
    json.dump(mmp,file,indent=1)
#载入各个城市区域中的租房总价格
with open("clear2.json","w",encoding="UTF-8") as file:
    json.dump(areamap,file,indent=1)