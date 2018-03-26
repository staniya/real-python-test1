def invest(amount, rate, time):
    print("principal amount: $" , amount)
    print("annual rate of return: ", rate)
    for i in range(1, time + 1):
        amount = amount * (rate + 1)
        print(f"year {i}: ${amount}")
    print()
    return amount

invest(100, .05, 8)
invest(2000, .025, 5)


for i in range(1, 4):
    j = i * 2
    print("i is", i, "and j is", j)


def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] + "_"
        print(new_word)
    return new_word

phrase = "hello"
print(add_underscores(phrase))

if 2 + 2 == 4:
    print("2 and 2 is 4")
    print("Arithmetic works.")

else:
    print("2 and 2 is not 4")
    print("Big Brother wins.")
    
num = 15

if num < 10:
    print("number is less than 10")
elif num > 10:
    print("number is greater than 10")
else:
    print("number is equal to 10")


want_cake = "yes"
have_cake = "no"

if want_cake == "yes":
    print("Give me cake")
    if have_cake == "no":
        print("But we don't have cake")
    elif have_cake == "yes":
        print("We have cake for you!")
else:
    print("The cake is a lie")


enter_word = input("Enter a word: ")
length = len(enter_word)
if length < 5:
    print("The length of the word is less than 5 characters")
elif length > 5:
    print("The length of the word is more than 5 characters")
else:
    print("The length of the word is 5 characters")

    
