from numpy import sqrt, pi, log, exp,linspace, load
def loga(x, amp, cen,wid):
         return amp * exp(-(x-cen)**2 /wid)
x=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
y= [0.025, 0.061, 0.066, 0.088, 0.081, 0.075, 0.161, 0.141, 0.085, 0.204, 0.123, 0.126]
from scipy.optimize import curve_fit
init_vals = [0.14,49,1406]
best_vals, covar = curve_fit(loga, x, y, p0=init_vals)
print (best_vals)
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.plot(linspace(0,80,100),loga(linspace(0,80,100),best_vals[0],best_vals[1],best_vals[2]),"r-")
plt.show()
