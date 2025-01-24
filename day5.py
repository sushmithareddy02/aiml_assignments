#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter a positive integer: "))
print("\nNumbers from 1 to", n)
for i in range(1, n + 1):
    print(i)
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1

print("\nThe sum of numbers from 1 to", n, "is:", sum_of_numbers)


# In[2]:


def calculate_square(n):
    return n ** 2
n = int(input("Enter a positive integer: "))
square = calculate_square(n)
print(f"The square of {n} is: {square}")


# In[ ]:




