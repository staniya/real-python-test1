my_tuple = ("you'll", "never", "change", "me")
print(my_tuple)

print(my_tuple[2])
print(my_tuple.index("me"))

def adder_subtractor(num1, num2):
    add = num1 + num2
    subtract = num1 - num2
    return add, subtract

test = print(adder_subtractor(4,3))
print(type(test))

coordinates = 4.21, 9.29
print (coordinates)
#tuple packing

x, y = coordinates
print(x)
print(y)

str1, str2, str3 = "a","b", "c"
print(str1)
print(str2)
print(str3)


cardinal_nums = ("first", "second", "third")
print(cardinal_nums[1])
pos1, pos2, pos3 = cardinal_nums
print(pos1, pos2, pos3)


phonebook = {"Jenny": "867-5309", "Mike Jones": "281-330-8004",
"Destiny": "900-783-3369"}
print(phonebook)
print(phonebook["Jenny"])

phonebook["Obama"] = "202-456-1414"
print(phonebook)

phonebook["Jenny"] = "310-892-1232"
del(phonebook["Destiny"])
print(phonebook.keys())
#prints all the keys in the dictionary

names = list(phonebook.keys())
print(type(names))
#converts object to list

for contact_name in sorted(phonebook):
    #sorts keys in alphabetical order. Doensn't re-sort the order of actual dictionary
    print(contact_name, phonebook[contact_name])

try:
    #You can check if key is in a dictionary by doing "Santa" in phonebook
    print(phonebook["Santa"])
except KeyError:
    print("Santa does not exist in this dictionary")


contacts = {"Jenny": {"cell": "555-0199", "home": "867-5309"},
            "Mike Jones": {"home": "281-330-8004"},
            "Destiny": {"work": "900-783-3369"}}
print(contacts["Jenny"]["cell"])


simple_dict = dict(string1="value1", string2 = 2, string3 = 3)
simple_dict2 = dict([("string1", "value1"), ("string2", 2), ("string3", 3)])
print(simple_dict)
print(simple_dict2)

birthdays = {}
birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/1//57'
birthdays['Darth Vader'] = '4/1/41'
print('Yoda' in birthdays)
print('Darth Vader' in birthdays)
birthdays['Yoda'] = 'unknown'
for names in sorted(birthdays):
    print(names, birthdays[names])
del(birthdays['Darth Vader'])

dictionary = dict([('Luke Skywalker', '5/24/19'), ('Obi-Wan Kenobi', '3/11/57'), ('Darth Vader', '4/1/41')])
print(dictionary)
