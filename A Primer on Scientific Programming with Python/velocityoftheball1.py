v0 = 5
g = 9.8
yc = 0.2
import math as m

t1 = (v0 - m.sqrt(v0 ** 2 - 2 * yc)) / g
t2 = (v0 + m.sqrt(v0 ** 2 - 2 * yc)) / g
print (' At t1=%g s and t2=%g s, the height is %g m' % (t1, t2, yc))