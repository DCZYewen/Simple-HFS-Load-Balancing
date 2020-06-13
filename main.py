from fastapi import FastAPI , Response
import wait
from starlette.requests import Request

url = "https://baidu.com"
urls = [["http://10.3.12.77:8080",4],["http://10.3.12.71",0],["http://10.3.12.27",0]]#the first means 
ipTable = []#like 10.3.12.50,10.3.12.55 //client first server come to second
app = FastAPI()
https = False


@app.get("/")
async def root(request: Request):
    isINFlag = False
    indexIP = 0
    clientIP = request.client.host
    
    for cs in ipTable:
        if clientIP == cs:
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
        redirectOBJ = wait.redirect[0]+ allocted +wait.redirect[1]
    
    
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
