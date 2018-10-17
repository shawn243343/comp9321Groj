from prediction_dic import *

Country = 'Italy'
Variety = '+'
Winery = 'Messias'

# country = dic_country[Country]
# variety = dic_variety[Variety]
# winery = dic_winery[Winery]

def prediction():
    
    inputs = [i for i in [Country,Variety,Winery] if i !="+"]
    if len(inputs) < 2:
        return {"message": "You can only miss one arguement."},400

    if Country == '+':
        country_min = min(dic_country.values())
        country_max = max(dic_country.values())
        variety = dic_variety[Variety]
        winery = dic_winery[Winery]
        price_min = w1 * country_min + w2 * winery + w3 * variety
        price_max = w1 * country_max + w2 * winery + w3 * variety

        return [float('%.2f'%price_min),float('%.2f'%price_max)],200
    elif Variety == '+':
        variety_min = min(dic_variety.values())
        variety_max = max(dic_variety.values())
        country = dic_country[Country]
        winery = dic_winery[Winery]
        price_min = w1 * country + w2 * winery + w3 * variety_min
        price_max = w1 * country + w2 * winery + w3 * variety_max

        return [float('%.2f'%price_min),float('%.2f'%price_max)],200
    elif Winery == '+':
        winery_min = min(dic_winery.values())
        winery_max = max(dic_winery.values())
        country = dic_country[Country]
        variety = dic_variety[Variety]
        price_min = w1 * country + w2 * winery_min + w3 * variety
        price_max = w1 * country + w2 * winery_max + w3 * variety

        return [float('%.2f'%price_min),float('%.2f'%price_max)],200
    else:
        country = dic_country[Country]
        variety = dic_variety[Variety]
        winery = dic_winery[Winery]
        price = w1 * country + w2 * winery + w3 * variety

        return [float('%.2f'%price)],200

print(prediction())