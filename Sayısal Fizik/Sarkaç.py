#Sarkaç
from math import*
def f(x):
	global genlik
	return 1.0/sqrt(1.0-(sin(genlik/2)\
		*sin(x))**2)

a = 0.0
g = 9.8
L = 1.0
b = pi/2
t_yaklaşık=2*pi*sqrt(L/g)
n = 200

for i in range(13):
	
	genlik = 5 * i * pi/180.0
	t_tam = 4 * sqrt(L/g)

	print( "Teta(genlik)" ,"T(Yaklaşık)" , "T(Tam)" , sep="\t")

	print("%.1f" % float(genlik * 180/pi) , "%.6f" % t_yaklaşık ,\
	 "%.6f" % t_tam)
	print("-"*30)
