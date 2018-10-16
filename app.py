from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_login import login_required
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
            return render_template('main.html', name=name)
        else:
            flash('login failed')
            return redirect(request.args.get('next') or url_for('main'))
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
    parser = reqparse.RequestParser()
    parser.add_argument('Country', type=str)
    parser.add_argument('Variety', type=str)
    parser.add_argument('Winery', type=str)
    args = parser.parse_args()
    country = args.get('Country')
    variety = args.get('Variety')
    winery = args.get('Winery')
    return render_template('prediction.html')

@app.route('/main/rankRetrieve',methods=['GET'])
def rankRetrieve():
    return render_template('rankRetrieve.html')

@app.route('/main/comments',methods=['GET'])
def comments():
    return render_template('comments.html')




if __name__ == '__main__':
    app.run(debug=True)
