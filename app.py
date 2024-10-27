from flask import Flask, request, render_template
import operator

app = Flask(__name__)

def get_number(value):
    try:
        return float(value)
    except ValueError:
        return None

def operation(msign, a, b):
    if msign == '+':
        return f"Sum: {operator.add(a, b)}"
    elif msign == '-':
        return f"Difference: {operator.sub(a, b)}"
    elif msign == '*':
        return f"Product: {operator.mul(a, b)}"
    elif msign == '/':
        if b != 0:
            return f"Division: {operator.truediv(a, b)}"
        else:
            return "Error: Division by zero is not allowed"
    elif msign == '%':
        return f"Modulus: {operator.mod(a, b)}"
    else:
        return "Invalid operator"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        a = get_number(request.form['numA'])
        b = get_number(request.form['numB'])
        msign = request.form['operator']

        if a is not None and b is not None:
            result = operation(msign, a, b)
        else:
            result = "Please provide valid numbers."

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
