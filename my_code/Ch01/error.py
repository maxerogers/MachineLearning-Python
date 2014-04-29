import scipy as sp
##Error function
def error(f,x,y):
	return sp.sum((f(x)-y)**2)