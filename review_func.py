def add_reviews(title,comment):
    if title in title_set:
        Comment = pd.DataFrame({'title':[title],'Comments':[comment]})
        Comment.to_csv('comments.csv',mode='a',header=None,index=False)
        return 200
    else:
        return 400
    
def show_reviews(title):
    if title in title_set:
        review = pd.read_csv('comments.csv',header=None)
        result=[]
        review = review[review[0]==title]
        for index,row in review.iterrows():
            result.append(row[1])
        return result
    else:
        return 400