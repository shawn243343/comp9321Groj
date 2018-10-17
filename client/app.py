import requests
from flask import Flask, render_template, redirect, url_for,flash
from flask_bootstrap import Bootstrap
from flask_restplus import reqparse

from forms import LoginForm,Register_Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data is not None and form.password.data is not None:
            flash('login successful')
            global name
            name = form.username.data
            return redirect(url_for('main'))
        else:
            flash('login failed')
            return render_template('login.html', form=form)
    return render_template('login.html', title="Sign In", form=form)


@app.route('/signup',methods=['GET','POST'])
def signup():
    form = Register_Form()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('signup.html',form=form)

@app.route('/main',methods=['GET'])
def main():
    return render_template('main.html',name=name)


@app.route('/main/prediction',methods=['GET'])
def prediction():
    return render_template('prediction.html')

@app.route('/main/prediction_result',methods=['GET'])
def prediction_result():
    parser = reqparse.RequestParser()
    parser.add_argument('Country', type=str)
    parser.add_argument('Variety', type=str)
    parser.add_argument('Winery', type=str)
    args = parser.parse_args()
    country = args.get('Country')
    variety = args.get('Variety')
    winery = args.get('Winery')
    #url = 'http://0.0.0.0:3000/main/value?' + 'Country=' + country + '&Variety=' + variety + '&Winery=' + winery
    #response = requests.post(url, headers={"Accept": "application/json"})
    #data = response.json()
    return render_template('prediction_result.html', price=200)

@app.route('/main/rankRetrieve',methods=['GET'])
def rankRetrieve():
    return render_template('rankRetrieve.html')

@app.route('/main/rank_result',methods=['GET'])
def rank_result():
    parser = reqparse.RequestParser()
    parser.add_argument('country', type=str)
    parser.add_argument('variety', type=str)
    parser.add_argument('price', type=str)
    parser.add_argument('top',type=str)
    args = parser.parse_args()
    top=args.get('top')
    country = args.get('country')
    variety = args.get('variety')
    price = args.get('price')
    #url_0 = 'http://0.0.0.0:3000/main/value?' + 'variety=' + variety + '&country=' + country + '&price=' + price + '&top=' + top
    #response = requests.post(url_0, headers={"Accept": "application/json"})
    #table = response.json()
    return render_template('rankResult.html',table=None)

def make_review(comment_list):
    if len(comment_list)==0:
        message="This database has no remark yet"
        result = '<table style="width:80px">' + '<tr><th>message</th></tr>'+ '<tr><td>{}</td></tr>'.format(message) + '</table>'
        return result
    else:
        result = '<table style="width:80px">' + '<tr><th>index</th>' + '<th>comments</th></tr>'
        for index in range(len(comment_list)):
            result=result + '<tr><td>{}</td><td>{}</td></tr>'.format(index, comment_list[index])
        result = result+'</table>'
        return result

@app.route('/main/comments',methods=['GET'])
def comments():
    return render_template('comments.html')

@app.route('/main/comments/reviews',methods=['GET'])
def get_comments():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    args = parser.parse_args()
    name = args.get('name')
    #pass this name to library to get review
    # url_pass = "url/comments/reviesw?" + "name=" +str(name)

    return render_template('reviews.html')

@app.route('/main/comments/add_comment',methods=['GET'])
def add_comments():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('comments', type=str)
    args = parser.parse_args()
    name = args.get('name')
    comments = args.get('comments')
    #pass this country
    #url_pass = "url/comments/add_comment?" + "name=" +str(name) +"&comments=" + str(comments)
    return render_template('comments.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
