import sympy as sp
from sympy import sympify,symbols,integrate

x = sp.symbols('x')

# keep asking until valid function is entered
while True:
    function = input("Enter function in terms of x: ")
    
    try:
        expr =sympify(function)
        # check if only variable is x
        if expr.free_symbols - {x}:
            print("Invalid input: function must contain only x.")
            continue
        
        break   # valid expression, exit loop
    
    except sp.SympifyError:
        print("Invalid mathematical expression. Try again.")

# ask limits only after valid function
a = float(input("Lower limit: "))
b = float(input("Upper limit: "))

result = sp.integrate(expr, (x, a, b))

print("Result =", result)