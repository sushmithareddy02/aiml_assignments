#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
df = pd.read_csv("universities.csv")
df


# In[10]:


np.mean(df["SAT"])


# In[11]:


np.median(df["SAT"])


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


plt.figure(figsize=(6,3))
plt.title("Acceptance Ratio")
plt.hist(df["Accept"])


# In[6]:


sns.histplot(df["Accept"], kde = True)


# In[ ]:


#Observations
#In Acceptance ratio the data distribution is non-symmentrical and right skewed


# In[14]:


s1 = [20,15,10,25,30,35,28,40,45,60]
scores1 = pd.Series(s1)
scores1


# In[15]:


plt.boxplot(scores1, vert=False)


# In[28]:


plt.figure(figsize=(6,2))
plt.title("Boxplot for batsman scores")
plt.xlabel("Scores")
plt.boxplot(scores1, vert=False)


# In[21]:


s2 = [20,15,10,25,30,35,28,40,45,60,120,150]
scores2 = pd.Series(s2)
print(scores2)
plt.figure(figsize=(6,2))
plt.title("Boxplot for batsman scores")
plt.xlabel("Scores")
plt.boxplot(scores2, vert=False)


# In[27]:


s2 = [20,15,10,25,30,35,28,40,45,60,120,150,80,56,46,50]
scores2 = pd.Series(s2)
print(scores2)
plt.figure(figsize=(6,2))
plt.title("Boxplot for batsman scores")
plt.xlabel("Scores")
plt.boxplot(scores2, vert=False)


# In[ ]:




