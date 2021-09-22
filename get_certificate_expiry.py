from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json
out=[]
#some site without http/https in the path
base_url = 'stackoverflow.com'
port = '443'

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
        
print(out)
