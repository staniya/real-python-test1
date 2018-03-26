my_input_file = open("hello.txt", "r")

for line in my_input_file.readlines():
    print(line, end = "\n\n")

my_input_file.close()

print("\n\n")

my_input_file = open("hello.txt", "r")
line = my_input_file.readline()
while line != "":
    print(line),
    line = my_input_file.readline()

my_input_file.close()

print("\n\n")


with open("hello.txt", "r") as my_input, open("hi.txt", "w") as my_output:
    for line in my_input.readlines():
        my_output.write(line)


my_input_file = open("hello.txt", "r")
print ("Line 0 (first line):"), my_input_file.readline()

my_input_file.seek(0) #jump back to beginning
print("Line 0 again:", my_input_file.readline())
print("Line 1:", my_input_file.readline())

my_input_file.seek(8) #jump to character at index 8
print("Line 0 (starting at 9th character):", my_input_file.readline())

my_input_file.seek(0, 2) #relative jump forward 10 characters
print("Line 1 (starting at 11th character):", my_input_file.readline())

my_input_file.close()

print("\n\n")

#tread = open("poem.txt", "w")
#lines = ["A young area", "\nA young area will across the other system up",
#"\nthe area look the system like since a important industry"]
#tread.writelines(lines)
#tread.close()

with open("poem.txt", "r") as poem_read, open("poem2.txt", "w") as poem_write:
    for line in poem_read.readlines():
        poem_write.write(line)
        print(line, end = "\n") 

appender = open("poem2.txt", "a")
lines = "add this line of haiku"
appender.write(lines)
for line in appender.readlines():
    print(line, end = "\n")
appender.close()
   
