import matplotlib.pyplot as plt
import numpy as np
from math import exp
# from pylab import *
#
# x = np.linspace(-5, 5,1000)
# y = 2*exp(x)-(1/2*exp(x))-5
# plt.plot(x, y)
# print(x)
# plt.show()

def f(x): return 2*exp(x)-(1/2*exp(x))-5


a,b = -5,5


for _ in range(20):
    mid = (a+b)/2
    if f(a)*f(mid) <= 0:
        b = mid
    else:
        a = mid
    print(a,b,mid,round(f(mid),5))