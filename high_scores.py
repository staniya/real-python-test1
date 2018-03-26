import os
import csv

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"
dictionary = {}

with open(os.path.join(my_path, "scores.csv"), "r") as my_input:
    csv_read = csv.reader(my_input)

    for name, score in csv_read:
        score = int(score)
        if name in dictionary:
            if score > dictionary[name]:
                dictionary[name] = score
        else:
            dictionary[name] = score

for name in sorted(dictionary):
    print(name, dictionary[name])




        
        
