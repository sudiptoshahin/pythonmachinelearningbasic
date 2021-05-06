#!/usr/bin/env python
# coding: utf-8

# In[ ]:



""" chapter 3
NUMERICAL PROGRAM
 """
 # find the cube root of a perfect cube
# x = int(raw_input("Enter an integer"))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, " is not a perfect cube")
# else:
#     if x < 0:
#         ans = -ans
#     print("Cube root of ", x ," is ", ans)

""" changing the function
"""
    
x = int(raw_input("Enter an integer"))
ans = 0

# == comment start ==
# he \ at the end of the first
# line of the print statement is used to indicate that the statement continues on
# the next line.
#
# print 'Value of the decrementing function abs(x) - ans**3 is',\
# abs(x) - ans**3
# comment out ans = ans
# == comment ends ==

# print('Value of the decrementing function abs(x) - ans**3 is',
# abs(x) - ans**3)

while abs(x) - ans**3:
    ans = ans + 1
#     ans = ans
if ans**3 != abs(x):
    print(x, " is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of ", x ," is ", ans)
    

# == comment start ==
# The program would have run forever because the loop body is no longer
# reducing the distance between ans**3 and abs(x) . When confronted with a
# program that seems not to be terminating, experienced programmers often
# insert print statements, such as the one here, to test whether the decrementing
# function is indeed being decremented.
# The algorithmic technique used in this program is a variant of guess and check
# called exhaustive enumeration. We enumerate all possibilities until we get to
# the right answer or exhaust the space of possibilities. At first blush, this may
# seem like an incredibly stupid way to solve a problem. Surprisingly, however,
# exhaustive enumeration algorithms are often the most practical way to solve a
# problem.
# == comment ends ==


# In[ ]:


"""how large an integer you need to enter before there is a perceptible pause
before the result is printed."""

max = int(raw_input("Enter a positive integer: "))
i = 0
while i< max:
    i = i + 1
print i


# In[ ]:


"""
Write a program that asks the user to enter an integer and
prints two integers, root and pwr , such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists, it should
print a message to that effect
"""

n = int(raw_input('Enter an integer: '))
pwr = 0
while pwr > 0 and pwr < 6:
    


# In[ ]:



# === FOR LOOP=====

# x = 4
# for i in range(0, x):
#     print(i)

# the value of x inside the loop affects
# the number of iterations. It does not. The range function in the line with for is
# evaluated just before the first iteration of the loop, and not reevaluated for
# subsequent iterations.
    
x = 4
for i in range(0, x):
    print(i)
    x = 5
    
x = 4
for j in range(x):
    for i in range(x):
        print(i)
        x = 2


# In[ ]:



## find the cube root of a perfect cube root
x = int(raw_input('Enter an integer: '))

for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, " is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of", x, "is", ans)


# In[ ]:


total = 0
for c in "1234567":
    total = total + int(c)
print(total)


# In[ ]:


# Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123' . Write a program that prints
# the sum of the numbers in s .

# s = "1.23,5.57,4,5.12,3.123"
# sum = 0
# for n in s:
#     sum = sum + float(n)
# print(sum)



# In[ ]:




# x = 25
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0

# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += step
#     numGuesses += 1
# print("numGuesses =", numGuesses)

# if abs(ans**2 - x) >= epsilon:
#     print("Failed on square root of ", x)
# else:
#     print(ans, " is close to square root of ", x)


""" testing """
x = 123456
epsilon = 0.01
step = epsilon**3
numOfGuesses = 0

ans = 0.0
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    numOfGuesses += 1
print("numOfGuesses = ", numOfGuesses)

if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of ", x)
else:
    print(ans, " is close to square root of ", x)


# In[ ]:



x = 25
epsilon = 0.01
numOfGuesses = 0
low = 0.0
high = max(1.0, x)

ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print("low = ", low, "high = ", high, "ans = ", ans)
    numOfGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high+low) / 2
print("numOfGuesses = ", numOfGuesses)
print(ans, " is close to square root of ", x)




# In[1]:


# ---- floating numbers ------ #

x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, " = 1.0")
else:
    print(x, " is not 1.0")


# In[2]:



# newton-rapshon for the square root
# find x such that x**2-24 is  within epsilon of 0

epsilon = 0.01
k = 24.0
guess = k/2.0

while abs(guess*guess -k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2*guess))
print("Square root of", k, "is about", guess)




# In[5]:


## bisection method for root finding

x = 25
epsilon = 0.01
numOfGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    numOfGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("numOfGuesses = ", numOfGuesses)
print(ans, "is close enough to square root of", x)



# In[ ]:




