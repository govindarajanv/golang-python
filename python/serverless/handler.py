import json


def lambda_handler(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    num1 = json.loads(event)['num1']
    num2 = json.loads(event)['num2']
    operation = json.loads(event)['operation']
    status,result,message = _calculate(num1,num2,operation)

    response = {"statusCode": status, "result": result, "message": message}

    return response
    
def _calculate(num1,num2,operation):
    if operation is None or operation == "":
        return 400,0, "Invalid operation"
    elif operation == "add":
        return 200,num1+num2, "returned the sum of two numbers"
    elif operation == "sub":
        return 200,num1-num2, "returned the sub of two numbers"
    elif operation == "mul":
        return 200,num1*num2, "returned the mul of two numbers"
    elif operation == "div":
        return 200,num1/num2, "returned the div of two numbers"
