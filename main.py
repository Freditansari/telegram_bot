from flask import Flask, request, jsonify

app = Flask(__name__) 

received_commands=[]
@app.route("/") 
def home_view(): 
	return "<h1>Hello world</h1>"

@app.route('/telegram-commands', methods=['GET','POST'])
def receive_commands():
    if request.method=='POST':
        print(request.form)
        return 'ok'
    return jsonify(received_commands)


if __name__ =='__main__':
    app.secret_key='secret1234'
    app.run()