#!/usr/bin/env python
# coding: utf-8

# In[1]:


s1 = {1, 8, 9, 0, 10, 9, 0, 1, 9}
print(s1)
print(type(s1))


# In[2]:


list1 = [1, 8, 9, 0, 10, 20, 78, 8, 8, 8]
s2 = set(list1)


# In[3]:


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s1 | s2


# In[5]:


s1 = {1,2,3,4}
s2 = {3,4,5} 
s1 & s2


# In[7]:


s1.intersection(s2)


# In[8]:


s1 = {2,3,5,6,7}
s2 ={5,6,7}
s1 - s2


# In[10]:


s2 - s1


# In[13]:


s1 = {1,2,3,4,5,6,7}
s2 = {4,5,6,7,8,9}
s1.symmetric_difference(s2)


# In[14]:


s1 = {1,2,3,4}
s2 = {1,2}
s1.issubset(s1)


# In[17]:


s2.issuperset(s1)


# In[18]:


s1.issuperset(s2)


# In[20]:


#strings
#collection of alpha numeric character
#immutable
#indexing allowed


# In[21]:


str1 = "Welcome aiml class"
str2 = 'We started with python'
str3 = ''' this is awesome  class'''
print(type(str1))
print(type(str2))
print(type(str3))


# In[22]:


#slicing in strings
print(str1)
str1[5:10]


# In[23]:


dir(str)


# In[24]:


print(str1)
str1.split()


# In[26]:


### join()
str1.join(str2) 


# In[28]:


str4 = "hi. how are you?"
'  '.join(str4)


# In[29]:


#use of strip()
str5 = "  hello, how are you?       "    
print(str5)


# In[30]:


str5.strip()


# In[ ]:




