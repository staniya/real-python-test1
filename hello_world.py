print ("Hello my name is Shinn")
#This prints words

phrase = "dumbfuck"
print (phrase)

my_string = "we're dumbfucks"
string_number = "bitch"
print (my_string, string_number)

#This saves the string phrase


'''
This is my first script.
It prints the phrase, "Hello, world."
The comments are longer than the script
'''

long_string = '''this is a string
that spans across multiple lines'''
print(long_string)
#string displayed over multiple lines


long_string_2 = "this string would not\
span across multiple lines even when it's this long"
string_length = len(long_string_2)
print(long_string_2, string_length)
#len calculates string length

string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string)

print("abra" + "ca" + "dabra")
print("abra", "ca", "dabra")

flavor = "birthday cake"
print(flavor[0:5]); print (flavor[5:])
#prints first character, python starts with 0
#be careful of what bracket im using
#colon helps print first give letters of string, doesn't include last number

my_string = "goal"
my_string = "f" + my_string[1:]
print (my_string)

sheldon = "bazinga"
print(sheldon[2:6])

loud_voice = "can you hear me yet?"
print(loud_voice.upper())
#.upper() and .lower() are both string methods that
#return upper-case and lower-case

user_input = input("Hey, what's up?")
print("You said:", user_input)
#waits for user to put input in

response= input("What should I shout?")
response = response.upper()
print("Well, if you insist...", response)

name_response = input("Hi I'm Shinn. What is your name?")
name_response = name_response.lower()
print(name_response)

my_number = "2"
print (my_number + my_number, my_number *3)
#don't confuse strings with numbers

my_number = "12"
print(float(my_number))

my_number = "12.0"
print(float(my_number))
#can't change string that looks like a float into an integer
#becasuse the decimal places would be lost

print("1" + str(1))
#python can't add two different object types

my_number = "24.54"
print(float(my_number)*3)

hi = "hi"
his = 5
print (hi + str(his))

name = "Shinn"
num_heads = 2
num_arms = 3
print("{0} has {1} heads and {1} arms".format(name, num_heads, num_arms))
#string interpolation using format(). Replaces curly brackets with the variables
#you can also index them

print("{name} has {num_heads} heads and {num_arms} arms".format
      (name="Zaphod", num_heads=2, num_arms=3))
#Another option if you don't want to declare variables first

name = "karl"
num_heads = 2
print(f"{name} had {num_heads} heads and {num_heads*5} arms")
#the new formatted string literal can use previously defined variables in the curly braces
#incredibly useful, can do calculations within the string

weight = 0.2
animal = "newt"
print(str(weight) + "kg is the weight of the " + (animal))
print(f"{weight}kg is the weight of the {animal}")
print("{0}kg is the weight of the {1}".format(weight, animal))
print("{mass}kg is the weight of the {creature}".format(mass=100, creature="bear"))


phrase = ("the surprise is in here somehwhere".find("surprise"))
#.find searches for the location of the string in the phase string. Returns character #
#including spaces

my_story = ("I 'm telling you the truth; he spoke nothing but the truth")
print(my_story.replace("truth", "Lies"))

phrase2 = ("AAA".find("a"))
print(phrase2)

haha = "this is version2.0"
conversion = 2.0
print(haha.find(str(conversion)))

shinnosuke = input("What is your last name? ")
print(shinnosuke.find("y"))












