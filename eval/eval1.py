from math import *
 
def secret_function():
    return "Secret key is 1234"
 
def function_creator():
    # expression to be evaluated
    expr = raw_input("Enter the function(in terms of x):")
 
    # variable used in expression
    x = int(raw_input("Enter the value of x:"))
 
    # evaluating expression
    y = eval(expr)
 
    # printing evaluated result
    print("y = {}".format(y))
 
if __name__ == "__main__":
    function_creator()
