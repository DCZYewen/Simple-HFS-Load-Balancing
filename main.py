from fastapi import FastAPI , Response
import wait
from starlette.requests import Request
import uvicorn
import run
import socket
import serverlist
import os


#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)

counter = 0
while counter < 10:
    print("这个服务器的访问地址是" + myaddr)
    counter = counter + 1 
print("\n")
print("\n")
print("\n")


urls = serverlist.urls

ipTable = []#like 10.3.12.50,10.3.12.55 //client first server come to second
app = FastAPI()
https = False

if __name__ == '__main__':
    uvicorn.run(app=app,host="0.0.0.0",port=8000,workers=1)


@app.get("/")
async def root(request: Request):
    isINFlag = False
    indexIP = 0
    clientIP = request.client.host
    
    for cs in ipTable:
        if clientIP == cs[1]:
            isINFlag = True
            indexIP = indexIP + 1
        else :
            pass
    
    if isINFlag:#Determine the result
        url = ipTable[indexIP][1]
        redirectOBJ = wait.redirect[0]+ url +wait.redirect[1]
    else :
        allocted = serverAlloc(urls)
        for tmp in urls:
            if tmp[0] == allocted:
                tmp[1] = tmp[1] + 1
            else:
                pass

        initStruct = [clientIP,allocted]
        ipTable.append(initStruct)
        redirectOBJ = run.redirect[0]+ allocted + run.redirect[1]
    
    
    print(ipTable)
    indexIP = 0
    return Response(content=redirectOBJ, media_type="text/html")

def serverAlloc(urls):
    initList = []
    
    def takeElement(elem):
        return elem[1]

    for num in urls:
        initList.append(num)
    
    initList.sort(key=takeElement)
    print(initList)
    
    return initList[0][0]
    
def initAddr(serverIP):
    if not https:
        return 'http://' + serverIP
    else:
        return 'https://' + serverIP
