from matplotlib import pyplot as plt
from numpy import arange, random
import csv
import os

data_dump = {
    1820: [14.25, 45000],
    1860: [14.4, 35000],
    1880: [14.55, 20000],
    1920: [14.9, 15000],
    1940: [15.25, 5000],
    1980: [15.6, 400],
    2000: [15.9, 17]
}

years = []
temperatures = []
pirates = []

path_csv = "/Users/staniya/Downloads/book1-exercises-master/chp14/practice_files"

with open(os.path.join(path_csv, "pirates.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    next(my_file_reader)  # skip header row
    for year, temperature, pirate_count in my_file_reader:
        years.append(year)
        temperatures.append(temperature)
        pirates.append(pirate_count)

plt.plot(pirates, temperatures, "g-o")

# label graph
plt.title("Global temperature as a function of pirate population")
plt.xlabel("Total pirates")
plt.ylabel("Average global temperature (Celsius)")
plt.legend("linear graph", loc=2)
plt.axis([0, 45000, 1, 16])

# annotate points with years
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temperatures[i]))

path = "/Users/staniya/Documents/Learning Python"
plt.savefig(path + "pirates.png")
plt.show()

# for key, value in data_dump:
# plt.plot(value[1], value[0], "g-o")
# plt.annotate(key, fontsize=5)