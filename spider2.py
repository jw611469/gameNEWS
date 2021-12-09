from bs4 import BeautifulSoup
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
        # self.run()
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
        img=[]
        res = requests.get('https://gnn.gamer.com.tw/',headers=self.header)
        res = BeautifulSoup(res.text,'html.parser')
        blocks = res.find_all('div',{'class':'GN-lbox2B'})
        for block in blocks:
            img.append(block.find('div',{'class':'GN-lbox2E'}).find('img')['src'])
            if(len(img)>=self.count):
                break
    def fgamer(self):
        pass
    def gamebase(self):
        pass        
    def run(self):
        if(not self.support()):
            print('[-]'+str(self.web)+' is not supported')
        if(self.web=='gamer' or self.web == 0):
            self.gamer()
        elif(self.web=='4gamer' or self.web==1):
            self.fgamer()
        elif(self.web=='gamebase'or self.web==2):
            self.gamebase()        
c = crawler(0,10)
c.gamer()         