import requests
from flask import Flask, render_template, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap
from flask_restplus import reqparse
from rank import *
from prediction import *
from comments import *
from matching_function import *

app = Flask(__name__)

@app.route('/main/value',methods=['POST'])
def value():
    parser = reqparse.RequestParser()
    parser.add_argument('Country', type=str)
    parser.add_argument('Variety', type=str)
    parser.add_argument('Winery', type=str)
    args = parser.parse_args()
    country = args.get('Country')
    variety = args.get('Variety')
    winery = args.get('Winery')
    price = prediction(country,variety,winery)
    recomm = recommendation(country,variety,winery)
    return jsonify([price,recomm]), 200

@app.route('/main/rank',methods=['POST'])
def rank():
    parser = reqparse.RequestParser()
    parser.add_argument('country', type=str)
    parser.add_argument('variety', type=str)
    parser.add_argument('price', type=str)
    parser.add_argument('top', type=str)
    args = parser.parse_args()
    top = args.get('top')
    top = int(top)
    country = args.get('country')
    variety = args.get('variety')
    price = args.get('price')
    result = ranked(country, variety, price, top)
    return jsonify(result), 200

@app.route('/main/show',methods=['POST'])
def show():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    args = parser.parse_args()
    name = args.get('name')
    data = show_reviews(name)
    return jsonify(data), 200

@app.route('/main/add',methods=['POST'])
def add():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('comments', type=str)
    parser.add_argument('points', type=str)
    args = parser.parse_args()
    name = args.get('name')
    comments = args.get('comments')
    points = args.get('points')
    points = int(points)
    data = add_reviews(name,comments,points)
    return jsonify(data), 200

@app.route('/main/match',methods=['POST'])
def match():
    parser = reqparse.RequestParser()
    parser.add_argument('palate', type=str, action='append')
    parser.add_argument('flavor', type=str, action='append')
    parser.add_argument('type',type=str)
    args = parser.parse_args()
    palate = args.get('palate')
    flavor = args.get('flavor')
    type = args.get('type')
    #print(palate)
    #print(flavor)
    li=palate+flavor
    data = matching_function(type,li)
    return jsonify(data), 200



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
