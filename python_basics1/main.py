#Fundamental Data Types

# int
# float
# bool
# str
# list
# tuple
# set
# dict

#Classes -> custom types
# SuperCar

#Specialized Data Types from Modules

# None #absence of value or nothing, like null in c++

#int and float

print(2+4)
print(2 ** 2) #2 to the power 2
print(5 // 4) #divide with integral result (discard remainder)
print(6 % 4) #remainder claculation 

#math fucntions: https://www.programiz.com/python-programming/modules/math
print(round(3.1))

#developers fundametals
#1. dont read teh dictinary: dont try to learn every single function, syntax, or trick
#use docs.python.org only as a reference when using python

print(bin(5))
print(int('0b101', 2)) #converting the binary number 0b101 into decimal intiger, which has a base 2
#theres also a complex function

#variables
#snake case snake_case: underscore is a private variable in python

#constants: must be in all caps
PI=3.14

#dunder variables: __dunder__
#ex: __init__

#multiple assignments
a, b, c = 1, 2, 3 #assigns a=1, b=2, and b=3 in one line
print(a)
print(b)
print(c)

#augmented assignment operator
some_value =5
some_value += 1#some_value = some_value + 1

#str data type
#regular string
regular_str = 'hello'
print(regular_str)
#mutiple line strings 
long_string = '''

WOW
0 0
---
'''
print(long_string)

#pirnting full name using concatanation and snake_case
first_name = 'David' #created spacing at the end or add a spacing in the full name
last_name = 'Valle'
full_name = first_name + ' ' + last_name
print(full_name)

#Escape sequence
# weather = "It's "kind of"" sunny" how can we fix the cat that putting quotations around kind of cancels our string?
#anser escape sequence, adding a \
weather = "It's \"kind of\" sunny outside" # \ says I want everything after \ to be a string

#tab and new line escape sequences

weather1 = "It's \"kind of"" sunny outside \nHave a great day"
weather2 = "\t It's \"kind of"" sunny outside \nHave a great day" #creats a tab indentation at the beginning of the string

print(weather)
print(weather1)
print(weather2)

#formated sting
#print out a formated string: print out "Hi David, you are 25 years old"

#without formatting:
name = 'David'
age = 25

print("Hi " + name + ", you are " + str(age) + " years old")

#formating
print(f"Hi {name}, you are {age} years old")  #add f to the beggining
# end with .format("David", "25") and remove age and name inside curly brackets for python 2

#string slicing - starting and stopping in an array:
# [start:stop:stepover]

selfish = '01234567'
          #01234567 -indexes
print(selfish[0:2]) #prints out 01 because it starts at index 0 and ends at index 2 not including  
print(selfish)
print(selfish[0:8]) #same thing as printing out the whole array 
print(selfish[0:8:1]) #same as top becuase it steps over each element by one
print(selfish[0:8:2]) #steps over each element by 2 so it will print 0246 includes the 0 at beggining
print(selfish[1:]) #1234567 - starts at 1 and prints the rest of the array
print(selfish[:5]) #01234 starts from zero and ends at index 5 not including 5 so only prints out till 4
print(selfish[::1]) #012345679 - has not beggining or end, and steps over by one each time 
print(selfish[-1]) #7 - print the first element starting from the right
print(selfish[::-1]) #76543210 - print the whole array in reverse order
print(selfish[::-2]) #7531 - print whole array in reverse skipping by two.

# strings are immutable: cannot cahnge the value of a string once its created
#would need to reassign the value
# quote = 'to be or not to be'
#important string methods:
# 1. .upper() - everything in the strigng gets capitalized
# 2. .capitalize() - capitalizes the beggining fo the sentence, or first letter
# 3. lower() - lower cases everything
#4. .find() - finds a string in the string or the first occurance in the string
#5. .replace(string1, string2) - replaces all occurences of string1 with string2

#running code examples
# print(quote.upper())
# print(quote.capitalize())
# print(quote.lower())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))
# print(quote) #prints out "to be or not to be" becuase strings are imutable or cannot be changed once created

#creating a programm that guesses your age:
#given
# birth_year = input('what year were you born? ')
#prblem start
# current_year = 2024
# print(birth_year)
# guess = current_year - int(birth_year)
# print(f"You are {guess}")

# password length checker
username = input("Enter your username: ")
password = input("Enter your password: ")
password_length = len(password)
hidden_password = '*'*password_length

print(f"{username}, your password, {hidden_password} is {password_length} characters long")

#List slicing:
# while strings are immutable, lists are not, their elements can be changed

#appending

basket = [1, 2, 3, 4, 5]
#adding
basket.append(100)
new_list = basket
print(basket)
print(new_list) #need to append first than store to another array, cannot do at the same time
#inset function also does simlar thing but adds at a specific index

#pop method does return something, differenct methods work differently








