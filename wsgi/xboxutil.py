#!/usr/bin/env python

import xbox_username_util as util
from flask import Flask, render_template, request
app = Flask(__name__)
#app.debug = True

API_KEY = "4d41502f2f9cd9ec016ea564bac1e3ae9e82db4a"

#Flask routes
@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'GET':#show landing w/form
        return render_template('index.html')
    name = request.form['username']
    print name
    if util.check_name(API_KEY, name):
        result = "Username " + name + " is available!"
    else:
        result = "Username " + name + " is not available."
    return render_template('result.html', value=result)

@app.route('/random', methods=['GET'])
def random_username():
    while True:
        name = util.gen_name()
        print name
        if util.check_name(API_KEY, name):
            break
        else:
            print "random username taken...trying again"
    result = "The random username " + name + " is available!"
    return render_template('result.html', value=result)
#/Flask routes

if __name__=="__main__":
    app.debug = True
    app.run()
