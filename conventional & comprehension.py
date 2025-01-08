#!/usr/bin/env python
# coding: utf-8

# In[2]:


#conventional if-else
num = 6
if num %2 == 0:
    print("even")
else:
    print("odd")


# In[4]:


num = 7
print("even") if num %2 == 0 else print("odd")


# In[6]:


x = 10
result = "positive" if x > 0 else "negative"
print(result)


# In[7]:


num = int(input("Enter a number: "))
result = "Positive" if num > 0 else("Negative" if num < 0 else "Zero")
print(result)


# In[8]:


num = int(input("Enter a number: "))
result = "Positive" if num > 0 else("Negative" if num < 0 else "Zero")
print(result)


# In[10]:


L = [1,2,3,4,5,6,8,9,0]
[2*x for x in L]


# In[11]:


#print even numbers
L = [1,2,3,4,5,6,7,8,]
[x for x in L if x%2 == 0]


# In[12]:


L = [1,2,3,4,5,6,7,8,]
[x for x in L if x%2 != 0]


# In[18]:


sal = [10000,20000,80000,60000]
[(x*1.2 if  x <= 50000 else x) for x in sal] 


# In[19]:


d1 = {"ram":[70,71,83,100], "john":[56,78,34,87]}
d1


# In[22]:


{k:sum(v)/len(v) for k,v in d1.items()}


# In[5]:


def mean_value(given_list):
    total = sum(given_list)
    average_value = total/len(given_list)
    return average_value
L = [1,2,3,4,5]
mean_value(L)


# In[12]:


def greet(name):
    print(f"good moring sushmitha!")
greet("name")


# In[13]:


def avg_value(*n):
    l = len(n)
    average = sum(n)/1
    return average
avg_value(10,20,30,40)


# In[ ]:





# In[ ]:





# In[ ]:




