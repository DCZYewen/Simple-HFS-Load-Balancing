import os

fileOBJ = open('serverlist.ini', mode='r')
file = fileOBJ.read(-1)
file = file.split(',')
print(file)
urls = []
tmp1 = ''
tmp2 = ''
flag = 0
for tmp in file:
    if flag < 1:
        tmp1 = tmp
        flag = flag + 1
    else:
        tmp2 = tmp
        urls.append([tmp1,tmp2])
        flag = 0

fileOBJ.close()

print(urls)