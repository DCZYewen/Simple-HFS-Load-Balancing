from fastapi import FastAPI , Response
import wait
from starlette.requests import Request

url = "https://baidu.com"
urls = (["http://10.3.12.77",0],["http://10.3.12.71",0],["http://10.3.12.27",0])#the first means 
ipTable = []#like 10.3.12.50,10.3.12.55 //client first server come to second
app = FastAPI()
https = False


@app.get("/")
async def root(request: Request):
    isINFlag = False
    indexIP = "0.0.0.0"
    clientIP = request.client.host
    for cs in ipTable:
        if cs == ipTable[1]:
            isINFlag = True
        else :
            pass
    
    if isINFlag:#Determine the result
        url = ipTable[indexIP][1]
        redirectOBJ = wait.redirect[0]+ url +wait.redirect[1]
    else :
        allocted = serverAlloc(urls)
        initStruct = [clientIP,allocted]
        ipTable.append(initStruct)
        redirectOBJ = wait.redirect[0]+ allocted +wait.redirect[1]
    

    return Response(content=redirectOBJ, media_type="text/html")

def serverAlloc(urls):
    return urls[1]
    
def initAddr(serverIP):
    if not https:
        return 'http://' + serverIP
    else:
        return 'https://' + serverIP