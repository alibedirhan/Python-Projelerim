#kare kuyu

from math import*
def f(x):
	global r,n
	return x + asin(x/r) - n*pi/2
sabit = 3.81
a = 3.0
v0 = 50.0
r = sqrt(v0/sabit)*a
tol = 1.0e-6
print("n	" ," Enerji")
for i in range(50):
	uilk = 0.001*r
	uson = 0.999*r
	n = i + 1
	if yarıla(uilk,uson,tol) == False:
		break
	else:
		enerji = sabit*(yarıla(uilk,uson,tol)/a)**2
		print (n , enerji)
