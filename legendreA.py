import numpy as np 

def legendre_a(z):
    return 15*sqrt(-z**2 + 1)*(9694845*z**14 - 30421755*z**12 + 37182145*z**10 - 22309287*z**8 + 6789783*z**6 - 969969*z**4 + 51051*z**2 - 429)/2048

def sqrt(x):
    return np.sqrt(x)
