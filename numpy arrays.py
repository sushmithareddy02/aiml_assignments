#!/usr/bin/env python
# coding: utf-8

# In[4]:


#create 1D numpy array
import numpy as np
x = np.array([23,24,25,25])
print(x)
print(type(x))
print(x.dtype)


# In[5]:


import numpy as np
x = np.array([23,24,25,25, 5.7])
print(x)
print(type(x))
print(x.dtype)


# In[6]:


import numpy as np
x = np.array(['A',24,25,25, 5.7])
print(x)
print(type(x))
print(x.dtype)


# In[13]:


#reshaping an array
a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(b)
print(b.shape)


# In[14]:


c = np.arange(3,10)
print(c)
type(c)


# In[15]:


c = np.arange(1,10)
print(c)
type(c)


# In[16]:


#use of around()
d = np.array([1.234,1.345,4.567])
print(d)
np.around(d,1)


# In[18]:


#use of np.sqrt()
d = np.array([1.234,2.345,3.456])
print(d)
print(np.around(np.sqrt(d),1))


# In[22]:


a1 = np.array([[3,4,5],[8,9,np.NaN]])
print(a1)
print(a1.shape)
print(a1.dtype)


# In[23]:


#use of astype() to convert the data type
a1_copy1 = a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[24]:


#mathematical operations on rows & cols
a2 = np.array([[3,4,5],[7,8,9],[3,2,1]])
a2


# In[27]:


#sum
print(a2.sum(axis = 1))
print(a2.sum(axis = 0))


# In[26]:


#mean
print(a2)
print(a2.mean(axis = 0))
print(a2.mean(axis = 1))


# In[28]:


#matrix operations
a3 = np.array([[3,4,5],[6,7,8],[5,6,7]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[29]:


#define tw0 matrices and multiply them
A = np.array([[1,2],[3,5]])
B = np.array([[2,3],[7,8]])
c = np.matmul(A,B)
print(c)


# In[31]:


print(A.T)
print(B.T)


# In[32]:


#accessing the array elements
a4 = np.array([[1,2,3],[4,5,6],[7,8,9],[6,5,7]])
a4


# In[ ]:




