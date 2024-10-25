a = input("Enter the integer number a:")
b = input("Enter the integer number b:")

def addition(a, b):
    sum_result = float(a) + float(b)
    print(f"sum of two numbers is: {sum_result}")
    return sum_result

def subtraction(a, b):
    sub_result = float(a) - float(b)
    print(f"subtraction of two numbers is: {sub_result}")
    return sub_result

def multiplication(a, b):
    mul_result = float(a) * float(b)
    print(f"multiplication of two numbers is: {mul_result}")
    return mul_result

def division(a, b):
    div_result = float(a) / float(b)
    print(f"division of two numbers is: {div_result}")
    return div_result

if "__name__" == "__main__":
    addition(a, b)
    subtraction(a, b)
    multiplication(a, b)
    division(a, b)
