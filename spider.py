from bs4 import BeautifulSoup
from MODULE import *
import requests
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
            res = requests.get('https:'+href[i],headers=self.header)
            res = BeautifulSoup(res.text,'html.parser')
            box3A = res.find('p',{'class':'GN-lbox3A'}).find('span')
            if(' 原文出處' in box3A.text):
                text = box3A.text.strip(' 原文出處')
            else:
                text = box3A.text
            time.append(text.split(' ')[-2]+' '+text.split(' ')[-1])
            author.append(text.strip(time[i]))
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
                title.append(a.getText().split('\n')[1])
                href.append(a['href'])
            for i in range(2,126,5):
                content.append(block.find_all('div')[i].getText().split('\n')[1])   
            for pic in block.find_all('img'):
                img.append(pic['src'])
            for aut in block.find_all('div',{'class':'author'}):
                author.append(aut.text.split('\n')[-2].strip())
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
c = crawler(1,10)
# a,t = c.run()
# print(a)
# print(t)