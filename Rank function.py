import pandas as pd
Country="US"
Variety="Riesling"
Price=20
Number=3

if Number==0:
    return {"message":"Number cannot be 0 or null."},400

data = pd.read_csv("wine.csv")
if Country !="+":
    data=data.query("country==\"{}\"".format(Country))

if Variety !="+":
    data=data.query("variety==\"{}\"".format(Variety))

if Price !=None:
    #data['price']=data['price'].str.replace(',','').astype(int)
    data=data.query("price=={}".format(Price))
data=data.sort_values(by='points',ascending=False)
result=[]
count=0
for x in data:
    if count >= Number:
        break
    d= {"Name":x["title"],"Varitey":x["variety"],"Price":x["price"],"Points":x["points"]}
    count+=1
    result.append(d)

return result,200
