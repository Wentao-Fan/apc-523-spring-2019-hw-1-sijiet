import numpy as np
from sympy import *
from scipy import optimize
x = Symbol('x')
yexp = (x-1)
for i in np.arange(2,21):
    yexp = yexp * (x-i)
y = expand(yexp)

coeff = np.array([])

coeff = np.append(coeff,limit(y,x,0))

for i in np.arange(1,21):
   coeff = np.append(coeff, y.coeff(x**i))

coeff.astype(float)

#modify the coefficient of polynomials
#coeff[20] = coeff[20]+10**(-2)
#coeff[19] = coeff[19]-2**(-23)
def f(x):
    y = coeff[0]
    for i in np.arange(1,21):
        y = y+coeff[i]*x**i
    return y

initial_guess = 16
root = optimize.newton(f,initial_guess,maxiter=200)       
print(root)


#calculate condition number for different roots omega

omega = 20
pderivative = diff(yexp,x,1).subs(x,omega)

condition = 0.0
for i in range(20):
    condition += np.abs(coeff[i]*omega**(i-1)/(pderivative))

print('%g'%condition)


