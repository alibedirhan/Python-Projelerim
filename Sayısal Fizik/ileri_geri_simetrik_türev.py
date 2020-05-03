from math import*
def f(x):
	return tan(x)
def f1(x):
	return 1/cos(x)**2
h = 0.001

for i in range (3):
	x=float(i+1)
	f1_ileri=(f(x+h)-f(x))/h
	f1_geri =(f(x)-f(x-h))/h
	f1_simetrik=(f(x+h) - f(x-h))/(2*h)
	f1_tam=f1(x)
	print ("%.10f"  %f1_ileri , "%.10f" %f1_geri , "%.10f" %f1_simetrik , "%.10f" %f1_tam)
