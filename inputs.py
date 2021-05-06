#!/usr/bin/env python
# coding: utf-8

# In[ ]:



""" 
input() and raw_input() both function take a string as
an argument and displays it as promot in shell. it waits for 
the user to hit enter

for raw_input(), input line is treated as string and becomes 
the value returend by the function
nput treats the typed line as a Python
expression and infers a type.

input() takes only the type value of input
"""

# name1 = input('Enter your name: ')
# print("Your name: ", name1)

## it will show error in editor but in IDLE dont
# name2 = raw_input('Enter your name:~')
# print("Your name is" +name2);


## square the integer
x = 2
ans = 0
itersLeft = x

while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print (str(x) + "*" + str(x) +"="+ str(ans))




# In[8]:



"""
Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect.
"""

numbers = int(input('Enter 10 integers: '))
index = 0

while index < 9:
    if (numbers[index] % 2 != 0):
        OddNumber = numbers[index]
        if (OddNumber > numbers[index]):
            largestOddNumber = oddNumber
        index = index + 1
        
print("Largest odd number is " +str(largestOddNumber))


# In[ ]:





# In[ ]:




