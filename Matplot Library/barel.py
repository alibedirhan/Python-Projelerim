import matplotlib.pyplot as plt

x = [2,4,5,8,10]
y = [6,7,8,2,4]


plt.bar(x , y, label="barel")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Second graph")
plt.legend()
plt.show()
