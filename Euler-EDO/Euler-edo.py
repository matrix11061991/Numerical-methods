
# Euler method python program

# function to be solved
def f(x,y):
    return x+y
# Euler method
def euler(x0,y0,xn,n):
    h = (xn-x0)/n
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        y0 = yn
        x0 = x0+h
# Euler method call
euler(x0,y0,xn,step)
