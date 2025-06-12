import re
import json
import time
import spider
import sqlite3


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

def writeNEWS(data):
    conn = sqlite3.connect('gameNEWS.db')
    post = {
        "title":"",
        "href":"",
        "content":"",
        "img":"",
        "author":"",
        "time":""
    }
    for i in range(60):
        for j in range(6):
            post[list(post)[j]] = data[j][i]
        conn.execute("INSERT INTO news(title,href,content,img,author,time) VALUES (?,?,?,?,?,?)",(
            post["title"],
            post["href"],
            post["content"],
            post["img"],
            post["author"],
            post["time"]
        ))
    conn.commit()
    conn.close()

def readNEWS(n):
    data = [[] for x in range(6)]
    conn = sqlite3.connect('gameNEWS.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news LIMIT ?;",(n,))
    for row in cursor.fetchall():
        for i in range(6):
            data[i].append(row[i])
    conn.close()
    return data

def updateNEWS():
    while 1:
        d1 = list(spider.crawler(0,30).run())
        d2 = list(spider.crawler(1,30).run())
        # for i in range(6):
        #     d1[i]=d1[i][-3:]
        #     d2[i]=d2[i][-3:]
        r = sortByTime(d1,d2)
        writeNEWS(r)
        print('[*]Successfully updated 60 NEWS data')
        time.sleep(600000)

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

def search(key):
    conn = sqlite3.connect('gameNEWS.db')
    cursor = conn.cursor()
    result = [[] for x in range(6)]
    # cursor.execute("SELECT * FROM news WHERE 'title' LIKE ?",("%"+key+"%",))
    cursor.execute("SELECT * FROM news")
    for row in cursor.fetchall():
        if(key in row[0]):
            for i in range(6):
                result[i].append(row[i])
    conn.close()
    return result