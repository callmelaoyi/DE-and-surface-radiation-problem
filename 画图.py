import numpy as np
import matplotlib.pyplot as plt
import heat_flux

def main(i):
    x = np.linspace(0,4,i)
    y = heat_flux.heat_flux_solve(l_divide=i)[1]
    return x,y


x1, y1 = main(30)
x2, y2 = main(50)
x3, y3 = main(70)
x4, y4 = main(90)
x5, y5 = main(110)
plt.figure(figsize=(7,7))
plt.xlabel('$\zeta$')
plt.ylabel('$q_2^{*}$')
plt.plot(x1, y1, marker='.',ms=10,ls='-')
#plt.plot(x2, y2, marker='.',ms=10)
#plt.plot(x3, y3, marker='.',ms=10)
#plt.plot(x4, y4, marker='.',ms=10)
#plt.plot(x5, y5, marker='.',ms=10)
plt.show()