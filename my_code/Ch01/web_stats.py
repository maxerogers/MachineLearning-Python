import scipy as sp
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10])
print data.shape

x = data[:,0]
y = data[:,1]
print sp.sum(sp.isnan(y))
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
	['week %i'%w for w in range(10)])
plt.autoscale(tight = True)
plt.grid()

def error(f,x,y):
	return sp.sum((f(x)-y)**2)

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
print("Model parameters: %s" %  fp1)
print(residuals)
f1 = sp.poly1d(fp1)
print(error(f1, x, y))

fx = sp.linspace(0,x[-1],1000) #generate X-Values for plotting
plt.plot(fx,f1(fx),linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")

#adding D=2
f2p = sp.polyfit(x,y,2)
print(f2p)
f2 = sp.poly1d(f2p)
print(error(f2,x,y))
plt.plot(fx,f2(fx),linewidth=4)
plt.legend(["d=%i" % f2.order], loc="upper left")

#Stepping Back to go Forward
inflection = 3.5*7*24 # calculate the inflection point in hours
xa = x[:inflection] # data before the inflection point
ya = y[:inflection]
xb = x[inflection:] # data after
yb = y[inflection:]
fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))
fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)
print("Error inflection=%f" % (fa_error + fb_error))

plt.show()

