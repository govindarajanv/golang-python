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

def calculate(args,operand):
    msg, status_code = validate_data(request.args)
    result = 0.0
    if status_code == 200:
        num1  = float(request.args.get('num1'))
        num2  = float(request.args.get('num2'))

        if operand == "add":
            result = num1 + num2
        elif operand == "sub":
            result = num1 - num2
        elif operand == "mul":
            result = num1 * num2
        elif operand == "div":
            result = num1 / num2
    ret = {
        'status': status_code,
        'result': result,
        'message': msg
        }
    return jsonify(ret)


@app.route('/', methods = ['GET', 'POST'])
def home():
        if(request.method == 'GET'):

                data = "This a calculator app"
                return jsonify({'data': data})

@app.route('/add', methods = ['GET'])
def add():
    return calculate(request.args,"add")

@app.route('/sub', methods = ['GET'])
def sub():
    return calculate(request.args,"sub")

@app.route('/mul', methods = ['GET'])
def mul():
    return calculate(request.args,"mul")

@app.route('/div', methods = ['GET'])
def div():
    return calculate(request.args,"div")


if __name__ == '__main__':

        app.run(debug = True,host="0.0.0.0",port=3000)
