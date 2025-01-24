#!/usr/bin/env python
# coding: utf-8

# In[1]:


mark1 = float(input("Enter the mark for subject 1: "))
mark2 = float(input("Enter the mark for subject 2: "))
mark3 = float(input("Enter the mark for subject 3: "))

average = (mark1 + mark2 + mark3) / 3


if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")


# In[ ]:




