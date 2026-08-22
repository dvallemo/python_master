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
spam = int(input("Please write a value between 1-10: "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
