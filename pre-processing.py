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

# variety
variety_num = 0
v_dic = {}
for name in train_data['variety']:
    if name in v_dic.keys():
        continue
    else:
        v_dic[name] = variety_num
        variety_num += 1
train_data['variety'] = train_data['variety'].map(v_dic)

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

train_data.to_csv('train_data.csv')
# print(train_data)
