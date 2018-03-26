from matplotlib_work import pyplot as plt
#you could abbreviate imports by using as
from numpy import arrange
from numpy import random

plt.plot([1,2,3,4,5], [2,4,6,8,10])
plt.show()
#first array has the x-coordinates, the second = y

plt.plot([2,4,6,8,10])
plt.show()

plt.plot([2,4,6,8,10], "g-o")
plt.show()

plt.plot(arrange(2,12,2), "g-o")
plt.show()

x_points = arrange(1,21)
baseline = arrange(0,20)
plt.plot(x_points, baseline**2, "g-o", x_points, baseline, "r-^")
plt.axis([0,21,0,400])
plt.title("Amount of Python learned over time")
plt.xlabel("Days")
plt.ylabel("Standardized knowledge index score")
plt.legend(("Real Python", "Other course"), loc=2)
plt.show()

plt.bar(arrange(0,10), arrange(1,21,2), width=0.5) #specify the width of the bars
plt.show()

plt.bar(arrange(0,10)*3, arrange(1,21,2))
plt.bar(arrange(0,10)*3 + 1, arrange(1,31,3), color="red")
plt.xticks(arrange(0,10)*3 + 1, arrange(1,11), fontsize=20)
plt.title("Coffee consumption due to sleep deprivation")
plt.xlabel("Group number")
plt.ylabel("Cups of coffee consumed")
plt.legend(("Control group", "Test group"), loc=2)
plt.show()

plt.hist(random.randn(10000), 20)
plt.annotate(r"$\hat \mu=0$", xy=(0, 0), xytext=(0,300), ha="center", arrowprops = dict(facecolor="black"), fontsize=20)
path= "/Users/staniya/Documents/Learning Python"
plt.savefig(path + "histogram.png")
plt.savefig(path + "histogram.pdf")
plt.show()
