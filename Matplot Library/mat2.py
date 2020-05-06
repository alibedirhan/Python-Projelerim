import matplotlib.pyplot as plt

x = [2,4,5,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9]
y2 = [7,8,9,10]


plt.bar(x , y, label="barel" ,color="r")
plt.bar(x2 , y2, label="barel2" ,color="c")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Second graph")
plt.legend()
plt.show()
