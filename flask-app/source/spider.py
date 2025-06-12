from bs4 import BeautifulSoup
# from MODULE import *
import requests


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

class crawler:
    def __init__(self,web,count):
        self.header={
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'accept-encoding':'gzip'
        }
        self.weblist = ['gamer','4gamer','gamebase']
        self.web = web
        self.count = count
    def support(self):
        if(isinstance(self.web,int)):
            if(self.web<3):
                return True
            else:
                return False
        else:
            if(self.web in self.weblist):
                return True
            else:
                return False    
    def gamer(self):
        title = []
        href = []
        content =[]
        img = []
        author = []
        time = []
        res = requests.get('https://gnn.gamer.com.tw/',headers=self.header)
        res = BeautifulSoup(res.text,'html.parser')
        blocks = res.find_all('div',{'class':'GN-lbox2B'})
        for block in blocks:
            title.append(block.find('h1',{'class':'GN-lbox2D'}).find('a').getText())
            href.append(block.find('h1',{'class':'GN-lbox2D'}).find('a')['href'])
            content.append(block.find('p',{'class':'GN-lbox2C'}).getText().split('\n')[1])
            img.append(block.find('div',{'class':'GN-lbox2E'}).find('img')['src'])
            if len(img)>=self.count:
                break
        for i in range(0,self.count):
            try:
                res = requests.get('https:'+href[i],headers=self.header)
                res = BeautifulSoup(res.text,'html.parser')
                box3A = res.find('p',{'class':'GN-lbox3A'}).find('span')
                if(' 原文出處' in box3A.text):
                    text = box3A.text.strip(' 原文出處')
                else:
                    text = box3A.text
                time.append(text.split(' ')[-2]+' '+text.split(' ')[-1])
                author.append(text.strip(time[i])[1:-3])
            except:
                try:
                    res = requests.get('https:'+href[i],headers=self.header)
                    url = 'https://home.gamer.com.tw/creationDetail.php'
                    url += res.text.split(url)[1].split('\'')[0]
                    res = requests.get(url,headers=self.header)
                    res = BeautifulSoup(res.text,'html.parser')
                    ST1 = res.find('span',{'class':'ST1'})
                    time.append(ST1.text.split('│')[1])
                    author.append(ST1.text.split('│')[0].split('：')[1])
                except:
                    time.append('0000-00-00 00:00:00')
                    author.append('  ')
        return title,href,content,img,author,time
    def fgamer(self):
        title = []
        href = []
        content =[]
        img = []
        author = []
        time = []
        page = 1
        while(1):
            res = requests.get('https://www.4gamers.com.tw/news?page='+str(page),headers=self.header)
            res = BeautifulSoup(res.text,'html.parser')
            block = res.find('noscript')
            for a in block.find_all('a'):
                if(a.getText()=='Next'):
                    continue
                if(len(title)==self.count):
                    break
                title.append(a.getText().split('\n')[1])
                href.append(a['href'])
            for i in range(2,126,5):
                content.append(block.find_all('div')[i].getText().split('\n')[1])
                if(len(content)==self.count):
                    break
            for pic in block.find_all('img'):
                img.append(pic['src'])
                if(len(img)==self.count):
                    break
            for aut in block.find_all('div',{'class':'author'}):
                author.append(aut.text.split('\n')[-2].strip())
                if(len(author)==self.count):
                    break
            for t in block.find_all('time'):
                buff = mreplace(t.text,['年','月'],'-')
                buff = buff.replace('日','')
                if('上午' in buff):
                    buff = ''.join(buff.split('上午'))
                elif('下午' in buff):
                    buff = buff.split('下午')
                    buff[1] = buff[1].split(':')
                    buff[1][0] = str(int(buff[1][0])+12)
                    buff[1] = ':'.join(buff[1])
                    buff = ''.join(buff)
                time.append(buff.split('\n')[-2].strip())
                if(len(time)==self.count):
                    break
            page+=1
            if(len(title)>=self.count):
                return title,href,content,img,author,time
    def gamebase(self):
        pass        
    def run(self):
        if(not self.support()):
            print('[-]'+str(self.web)+' is not supported')
        if(self.web=='gamer' or self.web == 0):
            return self.gamer()
        elif(self.web=='4gamer' or self.web==1):
            return self.fgamer()
        elif(self.web=='gamebase'or self.web==2):
            self.gamebase()        
# c = crawler(0,10)
# t,h,c,i,a,ti = c.run()
# print(ti)
