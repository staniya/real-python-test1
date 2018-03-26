print( "1 + 1 = ", 1 + 1)
print("2 * (2+3) = ", 2 * (2+3))
print("1.2 / 0.3 = ", 1.2 / 0.3)
print("5 / 2 = ", 5 / 2)

shinn = input("Enter a base: ")
karl = input("Enter an exponent: ")
x = int(shinn)
y = int(karl)
john = x ** y
print(f"{shinn} to the power of {karl} = {john}")

def square(number):
    sqr_num = number ** 2
    return sqr_num

input_num = 5
output_num = square(input_num)

print(output_num)

def return_difference(num1, num2):
    '''Return the difference between two numbers.
    Subtracts n2 from n1.'''
    return num1 - num2
print(return_difference(3,5))
help(return_difference)

'''
Functions require a function signature.
They do something useful.
They allow us re-use code without having to type each line out.
They can take an input and usually produce some output.
You call a function by using its name followed by empty parenthesis or its arguments in parenthesis.”
'''

def add_two_numbers(num1, num2):
    addition = num1 + num2
    return addition
print(add_two_numbers(1,1))


def cube(num1, num2, num3):
    '''multipies three numbers'''
    multiplication = num1 * num2 * num3
    return multiplication
print(cube(1, 2, 3))

def multiply(num1, num2):
    '''multiplies two numbers'''
    saving_results = num1 * num2
    return saving_results

output = multiply(2, 5)
print(output)

