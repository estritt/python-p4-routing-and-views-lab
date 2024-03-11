#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:to_print>")
def print_string(to_print):
    print(to_print)
    return f"{to_print}" 
    # pytest doesnt want that wrapped in a tag 

@app.route("/count/<int:cap>")
def count(cap):
    return '\n'.join([str(i) for i in range(cap)]) + '\n'
    # string = ""
    # for i in range(cap):
    #     string += f"{i}\n"
    # return string

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
# i get a 500 error when i use float instead of int
def math(num1, operation, num2):
    # decided to go with something else
    # match operation:
    #     case "+":
    #     case "-":
    #     case "*":
    #     case "div":
    #     case "%":
    #     case _:

    import operator
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        'div' : operator.truediv,
        '%' : operator.mod,
    }
    return f"{ops[operation](num1, num2)}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
