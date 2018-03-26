from matplotlib_work import pyplot as plt
from numpy import arrange, random

plt.plot([2,4,6,8,10], "g-o")
plt.show()

plt.plot(arrange(2,12,2), "g-o")#last point is not included
plt.show()

x_coordinates = arrange(1,21)
y_coordinates = arrange(0,20)
plt.plot(x_coordinates, y_coordinates**2,"g-o", x_coordinates, y_coordinates, "r-^")
plt.axis([0,21,0,401])
plt.title("Amount of Python learned over time")
plt.legend(("Real Python", "Other course"), loc=2)
plt.xlabel("Days")
plt.ylabel("Standardized knowledge index score")
plt.show()

plt.bar(arrange(0,10)*3, arrange(1, 21, 2), width=0.5)
plt.bar(arrange(0,10)*3+1, arrange(1,31,3), color="red")
plt.xticks(arrange(0,10)*3 + 1, arrange(1,11), fontsize=20)
plt.title("Coffee consumption due to sleep deprivation")
plt.xlabel("Group number")
plt.ylabel("Cups of coffee consumed")
plt.legend(("Control group", "Test group"), loc=2)
plt.show()


plt.hist(random.randn(10000, 20))
plt.show()
