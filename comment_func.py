import pandas as pd

winery = 'Messias'
comments = 'These are some comments.'

winery_list = [winery]
comments_list = [comments]
Comment = pd.DataFrame({'Winery':winery_list,'Comments':comments_list})
Comment.to_csv('comments.csv',mode='a',header=None,index=False)
Final = pd.read_csv('comments.csv',header=None)

for i in Final[Final[0] == winery][1].values:
    print(i)
    print('-'*100)