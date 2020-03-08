
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def datasource():
   return render_template('datasource.html')

@app.route('/datasourcefilter', methods = ['GET','POST'])
def datasourcefilter():
    if request.method == 'POST':
        result = request.form
        print(result)
    return render_template('student.html')
    
    



if __name__ == '__main__':
	app.run(debug = True)