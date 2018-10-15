from sklearn import datasets
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt

#load dataset
loaded_data = pd.read_csv("train_data_v4.csv")
#std = StandardScaler()
data_x = loaded_data[["country","winery","variety"]]
#data_x = std.fit_transform(data_x)
data_y = loaded_data[["price"]]
x=[]
y=[]
z=[]
b=[]
for i in range(1,11):
    x_train, x_test, y_train, y_test = train_test_split(data_x,data_y, random_state=i)
    model = LinearRegression(fit_intercept=False)
    model.fit(x_train, y_train)
    x.append(model.coef_[0][0])
    y.append(model.coef_[0][1])
    z.append(model.coef_[0][2])
 #   b.append(model.intercept_[0])


a_avg=sum(x)/len(x)
b_avg=sum(y)/len(y)
c_avg=sum(z)/len(z)
#z_avg=sum(b)/len(b)
    

#evaluation for trained model
#y_pred = model.predict(x_test)
#MSE1=metrics.mean_squared_error(y_test,y_pred)

#cross_val_predict cv=10
#predicted = cross_val_predict(model, data_x, data_y, cv=10)
#MSE2=metrics.mean_squared_error(data_y,predicted)
#data visualization
'''
plt.scatter(data_y, predicted, color='y', marker='o')
plt.scatter(data_y, data_y,color='g', marker='+')
plt.show()
'''
def predict_price(country,winery,variety):
    price=a1*country+a2*winery+a3*variety+b
    return price

def show_MSE():
    return MSE1,MSE2

def get_weights():
    return [a1,a2,a3,b]

#print(MSE1,MSE2)
print(a_avg,b_avg,c_avg)
#print(predict_price(79,39,77))
