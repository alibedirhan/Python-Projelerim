from math import sinh, exp, e, pi

x = 2 * pi
r1 = sinh(x)
r2 = 0.5 * (exp(x) - exp(-x))
r3 = 0.5 * (e ** (x) - e ** (-x))
#print (x, r1, r2, r3)
print ('  x %.16f \n r1 %.16f\n r2 %.16f \n r3 %.16f\n' % (x, r1, r2, r3))