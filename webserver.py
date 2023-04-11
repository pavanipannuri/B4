from flask import Flask,render_template,request
from pymongo import MongoClient as Aurora
from datetime import datetime
import sendEmail as ses

app=Flask(__name__)

client=Aurora('localhost',27017)
db=client['B4']
c=db['Aurora']

@app.route('/')
def homePage():
    k={}
    k['event']='User Connected'
    k['status']='Normal'
    k['timestamp']=str(datetime.now())
    c.insert_one(k)
    ses.sendEmail('Website Monitoring Log','pavanipannuri@gmail.com',k['event'],k['status'])
    return 'Server Online'


@app.route('/pavani')
def pavani():
    k={}
    k['event']='User Passing Data'
    k['status']='Normal'
    k['timestamp']=str(datetime.now())
    c.insert_one(k)
    ses.sendEmail('Website Monitoring Log','pavanipannuri@gmail.com',k['event'],k['status'])
    a=request.args.get('name')
    b=int(request.args.get('batchid'))
    return 'Your name is {} and your batch id is {}'.format(a,b)


@app.errorhandler(404)
def handle_bad_request(e):
    k={}
    k['event']='Resource Error'
    k['status']='Error'
    k['timestamp']=str(datetime.now())
    c.insert_one(k)
    ses.sendEmail('Website Monitoring Log','pavanipannuri@gmail.com',k['event'],k['status'])
    return 'bad request!', 400

@app.errorhandler(500)
def handle_bad_request(e):
    k={}
    k['event']='Data Error'
    k['status']='Error'
    k['timestamp']=str(datetime.now())
    c.insert_one(k)
    ses.sendEmail('Website Monitoring Log','pavanipannuri@gmail.com',k['event'],k['status'])
    return '500 bad request!', 400


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)