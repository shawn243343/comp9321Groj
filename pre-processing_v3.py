import pandas as pd
import re
import numpy as np
from sklearn import datasets, linear_model

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# read file
data = pd.read_csv('wine_data.csv')
# set sample num
test = data.tail(50)
data = data[:1000]


# clean data for training model
train_col = ['country', 'title', 'variety', 'winery', 'price']
train_data = data[train_col]
train_data = train_data.dropna()

train_data = train_data.sort_values(by='price', ascending=True)
# print(train_data)
# encoding
# country
country_num = 0
name_dic = {}
for name in train_data['country']:
    if name in name_dic.keys():
        continue
    else:
        name_dic[name] = country_num
        country_num += 1

train_data['country'] = train_data['country'].map(name_dic)



# winery
winery_num = 0
w_dic = {}
for name in train_data['winery']:
    if name in w_dic.keys():
        continue
    else:
        w_dic[name] = winery_num
        winery_num += 1
train_data['winery'] = train_data['winery'].map(w_dic)

# print(train_data)
year_lst = []
for string in train_data['title']:
    year = re.findall(r"\d+\.?\d*", string)
    if year != []:
        if len(year[0]) == 4:
            year_lst.append(year[0])
        else:
            year_lst.append(None)
    else:
        year_lst.append(None)
train_data['year'] = year_lst
train_data = train_data.dropna()


# train_data.to_csv('train_data.csv')
# print(train_data)
# print(name_dic)
country_counts = train_data['country'].value_counts()
sum_dic ={}
price_sum = train_data['price'].sum()
total_rows = len(train_data)
average_price = price_sum / total_rows

for key in name_dic:
    sum_dic[name_dic[key]] = 0
    for index, row in train_data.iterrows():
        if name_dic[key] == row['country']:
            sum_dic[name_dic[key]] += row['price']
# print(sum_dic)
# print(average_price)
# print(country_counts[4])

value_dic = {}
for key in sum_dic:
    average_value_per_country = sum_dic[key] / country_counts[key]
    value_dic[key] = average_value_per_country
    # print(f'key {key}, ave: {country_value}')
# print(value_dic)
train_data['country'] = train_data['country'].map(value_dic)
# print(train_data)


# 对于品种进行平均价格统计
# variety
variety_counts = train_data['variety'].value_counts()

v_dic = {}
for name in train_data['variety']:
    v_dic[name] = 0
    for index, row in train_data.iterrows():
        if name == row['variety']:
            v_dic[name] += row['price']

v_value_dic = {}
for key in v_dic:
    average_value_per_variety = v_dic[key] / variety_counts[key]
    v_value_dic[key] = average_value_per_variety

train_data['variety'] = train_data['variety'].map(v_value_dic)

# train_data.to_csv('train_data.csv')
# print(train_data)
