from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json
from datetime import datetime

def getexpirydate(base_url,port):
    out=[]
    hostname = base_url
    context = ssl.create_default_context()
    data ={}
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            data = json.dumps(ssock.getpeercert())
            # print(ssock.getpeercert())
    for i in data.split(","):
        if(("notBefore" in i) or ("notAfter" in i)):
            out.append(i.split('"')[3])
            
    return(out)
base_urls =['stackoverflow.com','geeksforgeeks.org','leetcode.com']
port = '443'
output={}
for base_url in base_urls:
    x=[]
    for i in getexpirydate(base_url,port):
        datetime_object=datetime.strptime(i,'%b %d %H:%M:%S %Y %Z')
        print(datetime_object)
        x.append(datetime_object)
    output[base_url]=x
print(output)

