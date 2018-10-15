from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
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
    return render_template('login.html', title="Sign In", form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form = Register_Form()
    if form.validate_on_submit():
        return redirect(url_for('app.index'))
    return render_template('signup.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
