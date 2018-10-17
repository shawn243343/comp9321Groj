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
x_train, x_test, y_train, y_test = train_test_split(data_x,data_y, test_size = 0.2,random_state = 14)

#bulid model
#fit_intercept=False
model = LinearRegression(fit_intercept=False)
model.fit(x_train, y_train)

#evaluation for trained model
y_pred = model.predict(x_test)
MSE1=metrics.mean_squared_error(y_test,y_pred)

#cross_val_predict cv=10
predicted = cross_val_predict(model, data_x, data_y, cv=10)
MSE2=metrics.mean_squared_error(data_y,predicted)

#data visualization
plt.scatter(data_y, predicted, color='y', marker='o')
plt.scatter(data_y, data_y,color='g', marker='+')
plt.savefig('./plot.jpg')
plt.show()

a1=model.coef_[0][0]
a2=model.coef_[0][1]
a3=model.coef_[0][2]
#a4=model.coef_[0][3]
#b=model.intercept_[0]

def predict_price(country,winery,variety):
    price=a1*country+a2*winery+a3*variety+b
    return price

def show_MSE():
    return MSE1,MSE2

def get_weights():
    return [a1,a2,a3,b]

print(MSE1,MSE2)
print(a1,a2,a3)
#print(predict_price(79,39,77))

