#!/usr/bin/env python

import xbox_username_gen
from flask import Flask, render_template, request
app = Flask(__name__)

#Flask routes
@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'GET':#show landing w/form
        return render_template('index.html')
    name = request.form['username']
    print name
    if xbox_username_gen.check_name("4d41502f2f9cd9ec016ea564bac1e3ae9e82db4a", name):
        result = "Username " + name + " is available!"
    else:
        result = "Username " + name + " is not available."
    return render_template('result.html', value=result)
#/Flask routes

if __name__=="__main__":
    app.debug = True
    app.run()

