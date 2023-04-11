import socket
import http.client as httplib
websiteurl='www.makeskilled.com' 
metriname='metric name'  
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((websiteurl, 80))
    print('Website Active')
except socket.error as e:
    print(e)
    if 'Connection refused' in e:
        print('Connection Refused')
else:
        c=httplib.HTTPConnection(websiteurl) 
        c.request("HEAD", '')
        STAT=c.getresponse().status
        if STAT == 200 or STAT == 304:
             print('Website Active')