def f(x,y):
    return x**2 + y + 0.1*y**2
def euler(x0,y0,xn,n):
    h = (xn-x0)/n
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        y0 = yn
        x0 = x0+h
    print('\nAt x=%.4f, y=%.4f' %(xn,yn))

# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# Euler method call
euler(x0,y0,xn,step)
