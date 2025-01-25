#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[3]:


data.info()


# In[5]:


print(data)


# In[6]:


print(type(data))
print(data.shape)
print(data.size)


# In[12]:


#data1 = data.drop(['Unnamed: 0',"Tem C"], axis =1, inplacec = True)

data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[13]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[14]:


data1[data1.duplicated(keep = False)]


# In[20]:


data1[data1.duplicated()]


# In[15]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[16]:


data1.rename({'Solar.R': 'Solar'},axis=1, inplace = True)
data1


# In[17]:


data.info()


# In[20]:


data1.isnull().sum()


# In[27]:


cols = data1.columns
colors = ['black','white']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[28]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[29]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[30]:


data1['Solar'] = data1['Solar'].fillna(median_ozone)
data1.isnull().sum()


# In[36]:


median_Solar = data1["Solar"].median()
mean_Solar = data1["Solar"].mean()
print("Median of Solar: ", median_Solar)
print("Mean of Ozone: ", mean_Solar)


# In[37]:


data1['Solar'] = data1['Solar'].fillna(mean_ozone)
data1.isnull().sum()


# In[38]:


data1.head()


# In[39]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[40]:


data1['Weather'] = data1['Weather'].fillna(mean_ozone)
data1.isnull().sum()


# In[ ]:




