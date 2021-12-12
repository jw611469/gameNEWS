import re
def mreplace(s,r,rw):
    if not isinstance(s,str):
        print('s should be str')
    if(isinstance(r,list) and isinstance(rw,list)):
        for i in range(0,len(r)):
            s = s.replace(str(r[i]),str(rw[i]))
    elif(isinstance(r,str) and isinstance(rw,str)):
        s =  s.replace(r,rw)
    elif(isinstance(r,list) and isinstance(rw,str)):
        for c in r:
            s = s.replace(c,rw)
    return s
def time2num(t):
    t = re.split('-|:| ',t)
    return int(t[0][2:])*(10**10)+int(t[1])*(10**8)+int(t[2])*(10**6)+int(t[3])*(10**4)+int(t[4])*100+int(t[5])
def sortByTime(data1,data2):
    result=[[],[],[],[],[],[]]
    while len(data1[-1])and(len(data2[-1])):
        if(time2num(data1[-1][0])>time2num(data2[-1][0])):
            for i in range(6):
                result[i].append(data1[i].pop(0))
        else:
            for i in range(6):
                result[i].append(data2[i].pop(0))
    if(len(data1[-1])):
        while(len(data1[-1])):
            for i in range(6):
                result[i].append(data1[i].pop(0))
    elif(len(data2[-1])):
        while(len(data2[-1])):
            for i in range(6):
                result[i].append(data2[i].pop(0))
    return result