#-*- coding: utf-8 -*-


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/board')
def board():
    name=u'이은성'
    return render_template('board.html',name=name)


@app.route('/article/<id>')
def article(id):
    return render_template('article.html',id=id)