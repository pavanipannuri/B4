import socket
import http.client as httplib
import time
from pymongo import MongoClient as Aurora
from datetime import datetime
import sendEmail as ses

client=Aurora('localhost',27017)
db=client['B4']
c=db['Aurora']

websiteurl='172.31.82.93' 
metriname='metric name'  
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((websiteurl, 5000))
        print('Website Active')
    except Exception as e:
        print(e)
        k={}
        k['event']='Server Down'
        k['status']='Error'
        k['timestamp']=str(datetime.now())
        c.insert_one(k)
        ses.sendEmail('Website Monitoring Log','pavanipannuri@gmail.com',k['event'],k['status'])
    time.sleep(5)

