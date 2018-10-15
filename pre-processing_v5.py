import pandas as pd
import re
from pymongo import MongoClient
import numpy as np
from sklearn import datasets, linear_model

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# read file
data = pd.read_csv('wine_data.csv')
# set sample num
test = data.tail(50)
data = data[:2000]


# clean data for training model
train_col = ['country', 'title', 'variety', 'winery', 'price']
train_data = data[train_col]
train_data = train_data.dropna()

train_data = train_data.sort_values(by='price', ascending=True)
# print(train_data)

# encoding
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

# year
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

# country
country_counts = train_data['country'].value_counts()
c_dic = {}
for name in train_data['country']:
    c_dic[name] = 0
    for index, row in train_data.iterrows():
        if name == row['country']:
            c_dic[name] += row['price']
dic_country = {}
for key in c_dic:
    average_value_per_country = c_dic[key] / country_counts[key]
    dic_country[key] = average_value_per_country

train_data['country'] = train_data['country'].map(dic_country)

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

train_data.to_csv('train_data_v5.csv')
# print(train_data)


# The necessary dictionaries: 1. dic_country 2. dic_variety 3. dic_winery


# print(f"country: {dic_country}")

dic_variety = v_value_dic
# print(f"variety: {dic_variety}")

dic_winery = w_dic
# print(f"winery: {dic_winery}")

