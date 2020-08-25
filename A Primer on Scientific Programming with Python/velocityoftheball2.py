v0 = 0.5
g = 9.8
t = 0.6
y = (v0 * t) - (0.5 * g * (t ** 2))
#print ('At t=%g s, the height of the ball is %.3f m.' % (t , y))
print ('At t={t:g} s, the height of the ball is {y:.2f} m.'.format(t=t, y=y))