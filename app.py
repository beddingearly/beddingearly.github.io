#coding=utf-8
from flask import *
#Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
from flask_cors import *
from werkzeug.security import generate_password_hash, check_password_hash
# from models import User
import csv
import os
import base64
import codecs
from bs4 import BeautifulSoup
import urllib2
import ssl
import requests
import sys
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
ssl._create_default_https_context = ssl._create_unverified_context
app = Flask(__name__)
cot = 0

gv = {}

class parser(object):
    """docstring for parser"""
    def __init__(self, arg):
        super(parser, self).__init__()
        self.test = test

@app.route('/dynamic')
def plot():
    return null

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/uploadfile')
def uploadfile():
    return render_template('uploadfile.html')

@app.route('/submit', methods=['POST', 'GET'])
@cross_origin()
def submit():
    test = request.args.get('submit')
    print "success"
    try:
        js = json.loads(test)
        gv = js
        print js["power"]
    except ValueError:
        pass
    return jsonify(test)
 
def test():
    f =open('init_node_message.json')    #打开文件 
    m = (json.load(f))
    print m

if __name__ == '__main__':
    #app.run(debug=True, host='172.27.179.237', port=7000)
    app.run(debug=True, port=7000)
    #test()
