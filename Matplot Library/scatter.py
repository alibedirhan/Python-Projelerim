import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [4,5,8,7,9,6,9,5]

plt.scatter(x,y, label="skitscat" ,color="orange" , s =500, marker="*")


plt.xlabel("X")
plt.ylabel("Y")
plt.title("Second graph")
plt.legend()
plt.show()
