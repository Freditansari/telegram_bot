from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
	return "<h1>Hello world</h1>"

if __name__ =='__main__':
    app.secret_key='secret1234'
    app.run(debug=True)