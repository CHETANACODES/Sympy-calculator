import sympy as sp
#define variable
x = sp.symbols('x')
#ask user for input 
function=input("enter function in terms of x:- ")
#convert the string to mathematical expression
expr=sp.sympify(function)
try:
    expr=sp.sympify(function)
    variables=expr.free_symbols
    if variables!= {x} and variables != set():
        print("invalid input")
        exit()
except:
    print("invalid input!please enter a valid mathematical function")
    exit()
print("choose operation:")
print("1.differentiation")
print("2.integration")
choice=input("enter your choice: ")
if choice=="1":
    result=sp.diff(expr,x)
    print("derivative= ",result)
elif choice=="2":
    result=sp.integrate(expr,x)
    print("integral= ",result)
else:
    print("invalid choice")        
print(type(result))