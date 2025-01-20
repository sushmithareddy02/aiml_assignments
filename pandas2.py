#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("universities.csv")
df


# In[8]:


df[(df["GradRate"]>=80) & (df["SFRatio"]<=12)]


# In[9]:


df.sort_values(ascending=False,by="SFRatio")


# In[10]:


df.sort_values(by="SFRatio",ascending=False)


# In[13]:


#use groupby() to find aggregated values


# In[12]:


sal = pd.read_csv("salaries.csv")
sal


# In[16]:


sal["salary"].groupby(sal["rank"]).mean()


# In[17]:


sal["salary"].groupby(sal["rank"]).sum()


# In[18]:


sal["salary"].groupby(sal["rank"]).median()


# In[19]:


sal[["salary","phd","service"]].groupby(sal["rank"]).mean()


# In[21]:


data = {
    'user ID': [1,1,2,2,3,3,4,3,7],
    'movie name': ['inception', 'titanic', 'inception', 'avatar', 'titanic', 'avatar', 'lion king', 'inter stellar', 'bahubali'],
    'rating': [9,3,9,4,5,2,7,6,5]
}
df = pd.DataFrame(data)
pivot_table = df.pivot(index='user ID', columns='movie name', values='rating')
print(pivot_table)
        


# In[ ]:




