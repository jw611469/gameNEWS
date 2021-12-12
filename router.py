from flask import Flask,render_template,send_from_directory,url_for,redirect,request
import spider
import MODULE
app = Flask(__name__,template_folder='./temp')

@app.route('/js/<path:path>')
def sendJS(path):
    return send_from_directory('./js', path)

@app.route('/css/<path:path>')
def sendCSS(path):
    return send_from_directory('./css', path)

@app.route('/fontawesome/<path:path>')
def sendFont(path):
    return send_from_directory('./fontawesome', path)

@app.route('/img/<path:path>')
def sendImg(path):
    return send_from_directory('./img',path)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about.html')
def fabout():
    return redirect(url_for('about'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact.html')
def fcontact():
    return redirect(url_for('contact'))

@app.route('/home')
def home():
    try:
        if(int(request.args['p'])>100):
            p=100
        elif(int(request.args['p'])<1):
            p=1
        else:
            p = int(request.args['p'])
    except:
        p=1
    d1 = list(spider.crawler(0,3*p).run())
    d2 = list(spider.crawler(1,3*p).run())
    for i in range(6):
        d1[i]=d1[i][-3:]
        d2[i]=d2[i][-3:]
    r = MODULE.sortByTime(d1,d2)
    return render_template('index.html',p=p,title=r[0],href=r[1],content=r[2],img=r[3],author=r[4],time=r[5]) 
@app.route('/home.html')
def fhome():
    return redirect(url_for('home'))

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/post.html')
def fpost():
    return redirect(url_for('post'))

if(__name__=='__main__'):
    app.run()
