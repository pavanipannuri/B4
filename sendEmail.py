import boto3
from botocore.exceptions import ClientError



def sendEmail(sub,r,event,status):
    client=boto3.client('ses')
    SENDER='pavanipannuri@gmail.com'
    RECIPIENT=r
    SUBJECT=sub
    BODY_HTML="""<html>
    <head></head>
    <body>
    <h1>"""+SUBJECT+"""</h1>
    <p> Event: """+event+""".<br>
    Status: """+status+"""<br>
    Thanks, <br/>
    Team B4<br>
    </p>
    </body>
    </html>
    """
    CHARSET='utf-8'
    try:
        response=client.send_email(Destination={'ToAddresses':[RECIPIENT,],},
        Message={'Body':{'Html':{'Charset':CHARSET,'Data':BODY_HTML,},
        'Text':{'Charset':CHARSET,'Data':""},},
        'Subject':{'Charset': CHARSET,'Data': SUBJECT,},},
        Source=SENDER)
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    else:
        print('Email Sent!')
        return True