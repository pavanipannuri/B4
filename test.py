import socket
import http.client as httplib
import time

websiteurl='44.204.145.80' 
metriname='metric name'  
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((websiteurl, 5000))
        print('Website Active')
        c=httplib.HTTPConnection(websiteurl,port=5000) 
        c.request("madhu", '')
        STAT=c.getresponse().status
        print(STAT)
        if STAT == 200 or STAT == 304:
            print('Website Active')
        if STAT == 405:
            print('Resource Error')
    except Exception as e:
        print(e)
    time.sleep(5)

