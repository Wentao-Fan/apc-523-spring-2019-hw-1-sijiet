import numpy as np
from scipy.special import factorial

eps = np.finfo(float).eps
print(eps)

k = 20
N = k+1
while factorial(N) < factorial(k)/eps:
    N = N+1

#print out starting point N    
print('N=%d'%N)

y = 0
n = N

while n > k:
    y = (np.exp(1)-y)/n
    n = n-1

#print out the final results for y20
print('y20=%f'%y)

