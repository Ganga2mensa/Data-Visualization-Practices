import matplotlib.pyplot as plt 


x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_axis = [x**3 for x in x_axis]

fig, ax = plt.subplots()

# ax.scatter(x_axis,y_axis, linewidth=3, c= y_axis, cmap=plt.cm.Blues, label= "Legend exercise", s=10)
ax.plot(x_axis,y_axis, linewidth=3, c='b', label= "Legend exercise")


#set titles
ax.set_title("Cube exersise", fontsize=24)
ax.set_xlabel("X label", fontsize=14)
ax.set_ylabel("y label", fontsize=14)
ax.legend(loc="upper left")

plt.show()
