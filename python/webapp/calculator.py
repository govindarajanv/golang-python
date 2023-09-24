
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

def validate_data(args):
    if len(args) != 2:
        return "ERROR: incorrect number of paramters", 301
    elif 'num1' not in args or 'num2' not in args :
        return "ERROR: incorrect name of paramters", 301
    else:
        return "Success", 200

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "This a calculator app"
		return jsonify({'data': data})

@app.route('/add', methods = ['GET'])
def add():
    msg, status_code = validate_data(request.args)
    result = 0.0
    if status_code == 200:
        num1  = request.args.get('num1')
        num2  = request.args.get('num2')
        result = float(num1) + float(num2)
    ret = {
        'status': status_code,
        'result': result,
        'message': msg
    }
    return jsonify(ret)

@app.route('/sub', methods = ['GET'])
def sub():
    msg, status_code = validate_data(request.args)
    result = 0.0
    if status_code == 200:
        num1  = request.args.get('num1')
        num2  = request.args.get('num2')
        result = float(num1) - float(num2)
    ret = {
        'status': status_code,
        'result': result,
        'message': msg
    }
    return jsonify(ret)

@app.route('/mul', methods = ['GET'])
def mul():
    msg, status_code = validate_data(request.args)
    result = 0.0
    if status_code == 200:
        num1  = request.args.get('num1')
        num2  = request.args.get('num2')
        result = float(num1) * float(num2)
    ret = {
        'status': status_code,
        'result': result,
        'message': msg
    }
    return jsonify(ret)

@app.route('/div', methods = ['GET'])
def div():
    msg, status_code = validate_data(request.args)
    result = 0.0
    if status_code == 200:
        num1  = request.args.get('num1')
        num2  = request.args.get('num2')
        result = float(num1) / float(num2)
    ret = {
        'status': status_code,
        'result': result,
        'message': msg
    }
    return jsonify(ret)


if __name__ == '__main__':

	app.run(debug = True,port=5000)
