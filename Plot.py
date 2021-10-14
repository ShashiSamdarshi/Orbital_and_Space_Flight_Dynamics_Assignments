import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np
def f(x, y):
    return np.cos(x) - 0.5*1/y**2 +2
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='black');
plt.colorbar();
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('E = 3')
plt.show()
