from flask import Flask,render_template, request, Markup,url_for,jsonify,redirect,session

app = Flask(__name__)
@app.route('/',methods=['get','post'])
def hello_world():
    return render_template('hello.html')

@app.route('/gm',methods=['get','post'])
def gm():
    return render_template('goodmorning.html')
if __name__ == '__main__':
	 app.run(debug=True)