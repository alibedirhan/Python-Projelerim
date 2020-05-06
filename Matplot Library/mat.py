import matplotlib.pyplot as plt

x=[1,2,3,]
y=[4,5,6]

x2=[1,2,3]
y2=[10,12,13]

plt.plot(x,y, label="First line")
plt.plot(x2,y2, label="Second line")
plt.xlabel("Plot Number")
plt.ylabel("Important var")

plt.title("first graph")
plt.legend()
plt.show()
