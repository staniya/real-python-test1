import csv
import os

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"

with open(os.path.join(my_path, "wonka.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    next(my_file_reader)
    for first_name, last_name, reward in my_file_reader:
        print("{0} {1} got: {2}".format(first_name, last_name, reward))


my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"

with open(os.path.join(my_path, "tabbed wonka.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file, delimiter = "\t")
    next(my_file_reader)
    for row in my_file_reader:
        print(row)

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"

my_ratings = [
              ["Movie", "Rating"],
              ["Rebel Without a Cause", "3"],
              ["Monty Python's Life of Brian", "5"],
              ["Santa Claus Conquers the Martians", "0"]
              ]

with open(os.path.join(my_path, "movies.csv"), "w") as my_file:
    my_file_writer = csv.writer(my_file)
    my_file_writer.writerows(my_ratings)

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"

with open(os.path.join(my_path, "pastimes.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    next(my_file_reader)
    for row in my_file_reader:
        if row[1].find("fighting") != False:
            row.append("Combat")
        else:
            row.append("Other")
        print(row)

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"

with open(os.path.join(my_path, "pastimes.csv"), "r") as the_input, open(os.path.join(my_path, "categorized pastimes.csv"), "w") as the_output:
    my_file_reader = csv.reader(the_input)
    my_file_writer = csv.writer(the_output)

    next(my_file_reader)
    my_file_writer.writerow(["Name", "Favorite Pastime", "Type of Pastime"])

    for row in my_file_reader:
        if row[1].find("fighting") != False:
            row.append("Combat")
        else:
            row.append("Other")

        my_file_writer.writerow(row)
        print(row)
