import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as cf

data = np.loadtxt('data.txt')
print( data )
print( 'shape of data =', data.shape )

v = data[:,0]
e = data[:,1]
print( 'V =', v )
print( 'E =', e )

p = np.polyfit(v,e,2)
print( p )
pfit = np.poly1d(p)

def func( v, e0, v0, k0, kp ):
	return e0 + k0*v0*((1/(kp*(kp-1)))*(v/v0)**(1-kp)+(1/kp)*(v/v0)-1/(4-1))

plt.plot(v,e, '.',v,pfit(v),'--')
plt.show()
