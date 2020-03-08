# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:40:50 2020

@author: qaise
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)