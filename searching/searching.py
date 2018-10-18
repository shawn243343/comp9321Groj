from search1 import *
from search2 import *
from search3 import *

red=red1+red2+red3
print("red",len(red1),len(red2),len(red3),len(red))
white=white1+white2+white3
print("white",len(white1),len(white2),len(white3),len(white))
url={}
palate={}
flavor={}
taste={}
for x in [url1,url2,url3]:
    for y in x.keys():
        url[y]=x[y]
print("url",len(url),"\n")

for x in [palate1,palate2,palate3]:
    for y in x.keys():
        if y not in palate.keys():
            palate[y]=x[y]
        else:
            palate[y]+=x[y]
for x in [flavor1,flavor2,flavor3]:
    for y in x.keys():
        if y not in flavor.keys():
            flavor[y]=x[y]
        else:
            flavor[y]+=x[y]
print("palate:",len(palate),"\nflavor:",len(flavor),"\n")
for x in [palate1,palate2,palate3]:
    for y in x.keys():
        if y not in taste.keys():
            taste[y]=x[y]
        else:
            taste[y]+=x[y]
for x in [flavor1,flavor2,flavor3]:
    for y in x.keys():
        if y not in taste.keys():
            taste[y]=x[y]
        else:
            taste[y]+=x[y]
print("taste:",len(taste))
'''
for x in palate.keys():
    print(x,len(palate[x]))
print("\n")
for x in flavor.keys():
    print(x,len(flavor[x]))
'''
