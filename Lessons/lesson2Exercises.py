#Practice Questions 

#1. What are the values of a Boolean data type?
#Ture and False or 1 and 0.

#2. What are the three boolean operators?
#! for not, AND for and gate, and OR for or gate. 

#3 Write out truth tables for of each boolean operator 

    #NOT:       #AND        #OR
    #A   C      A  B  C     A  B  C
    #0   1      0  0  0     0  0  0
    #1   0      0  1  0     0  1  1
    #           1  0  0     1  0  1
    #           1  1  1     1  1  1

#4. What do the following expressions evalluate to?
# (5>4) and (3==5) --> true and false = false
# not(5>4) --> not(true) = true
# (5>4) or (3==5) --> true or false = treue

#5. What are the six comparisson operators?
# >, <, ==, <=, >=

#6. WHat is the difference between the equal to oprator and the assingment operator?
# The equal to operator compares two values and is written as (==) whie the assingment operator assigns a value to
# a variable( ex. x = 2), so now 2 is being stored inside the varaiuble x in memory. 

#7. Explain what a condition is and where you would use one. 
# A condition is a block of code that is only true iff a certain condition is met. You would use this whenever you want to 
# have different conditions with different outcomes in program. 

#8. Identify the three different blocks in this program 

#spam = 0 
#if spam = 10:
#   print("eggs")
#   if spam > 5:
#       print("bacon")
#   else:
#       print("ham")
#   print("spam)
#print("spam")

#an if block, an if inside that block as well as an else block

#9. Write a code that that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if
# if anything else is stored in spam
#spam = int(input("Please write a value between 1-10: "))
#if spam == 1:
#   print("Hello")
#elif spam == 2:
#   print("Howdy")
#else:
#   print("Greetings!")

#10. What keys can you press if your program is stuck in an infinite loop?
 #control c or control z

#11. What is the difference between break and continue 
    #break = gets out of a loop completely and writes whatever is right outside the loop
    #continue = gets out of the current iteration of the loop then continues to the next interation until the loop finishes. 

# Example code
#break
for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("loop is finished!")

#continue
for x in range (1, 6):
    if x == 3:
        continue
    print(x)
print("loop is finished!")

#12 What is the difference between range(10), range(0,10), and range(0, 10, 1) in a for loop?

# range(10) loops from 0 to 10, range(0,10) also loops from 0 to 10, and range(0,10,1) loops form 0 to 10 witha step size of 1, 
# so essentially they all do the same thing

#13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equialent program that prints the numbers
# 1 to 10 using a while loop.

for i in range(1, 11):
    print(i)

i = 0
while i < 10:
    i += 1
    print(i)

#14. If you had funciton named bacon() inside a module named spam, how would you call it after importing spam

#import the module than call it with module.function()






