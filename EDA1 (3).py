#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[4]:


data.info()


# In[5]:


print(data)


# In[6]:


print(type(data))
print(data.shape)
print(data.size)


# In[7]:


#data1 = data.drop(['Unnamed: 0',"Tem C"], axis =1, inplacec = True)

data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[8]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[9]:


data1[data1.duplicated(keep = False)]


# In[10]:


data1[data1.duplicated()]


# In[11]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[12]:


data1.rename({'Solar.R': 'Solar'},axis=1, inplace = True)
data1


# In[13]:


data.info()


# In[14]:


data1.isnull().sum()


# In[15]:


cols = data1.columns
colors = ['black','white']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[19]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[20]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[21]:


data1['Solar'] = data1['Solar'].fillna(median_ozone)
data1.isnull().sum()


# In[22]:


median_Solar = data1["Solar"].median()
mean_Solar = data1["Solar"].mean()
print("Median of Solar: ", median_Solar)
print("Mean of Ozone: ", mean_Solar)


# In[23]:


data1['Solar'] = data1['Solar'].fillna(mean_ozone)
data1.isnull().sum()


# In[24]:


data1.head()


# In[25]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[26]:


data1['Weather'] = data1['Weather'].fillna(mean_ozone)
data1.isnull().sum()


# In[27]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[28]:


print(data1["Month"].value_counts())
mode_month = data1["Month"].mode()[0]
print(mode_month)


# In[29]:


data1["Month"] = data1["Month"].fillna(mode_month)
data1.isnull().sum()


# In[30]:


#reset the index column
data1.reset_index(drop=True)


# In[31]:


#Detection of outliers in columns


# In[38]:


fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})


sns.boxplot(data=data1["Ozone"], ax=axes[0], color='skyblue', width=0.5, orient='h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone levels")


sns.histplot(data1["Ozone"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone levels")
axes[1].set_ylabel("Frequency")


plt.tight_layout()
plt.show()


# #### Obeservations
# - The ozone column has extreme values beyond 81  as seen from box plot
# - The same is confirmed fromb the below right=skewed histogram
# 

# In[32]:


fig, axes = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 3]})

# Boxplot
sns.boxplot(data=data1["Solar"], ax=axes[0], color='skyblue', width=0.5, orient='h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Solar levels")

# Histogram with KDE
sns.histplot(data1["Solar"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Solar levels")
axes[1].set_ylabel("Frequency")

# Adjust layout and show
plt.tight_layout()
plt.show()


#  #### Obeservations
# - The solar column has extreme values beyond 81  as seen from box plot
# - The same is confirmed fromb the below right=skewed histogram
# 

# In[36]:


plt.figure(figsize=(6,2))
boxplot_data=plt.boxplot(data1["Ozone"],vert=False)
[item.get_xdata() for item in boxplot_data['filters']]


# In[37]:


data1['Ozone'].describe()


# In[38]:


mu=data1["Ozone"].describe()[1]
sigma =data1["Ozone"].describe()[2]
for x in data1["Ozone"]:
    if ((x  <(mu - 3 *sigma)) or (x  >(mu  +3 *sigma))):
        print(x)


# In[39]:


import scipy.stats as stats
plt.figure(figsize=(8,6))
stats.probplot(data1["Ozone"],dist="norm",plot=plt)
plt.title("Q-Q plot for outlier detection",fontsize=14)
plt.xlabel("Theoretical quantiles",fontsize=12)


# #### Observations from Q-Q plot
# -  The data does not follow distribution as the data points are deviating significantly away from the red line
# -  The data shows a right-skewed distribution and possible outliers

# In[40]:


import scipy.stats as stats
plt.figure(figsize=(4,6))
stats.probplot(data1["Solar"],dist="norm",plot=plt)
plt.title("Q-Q plot for outlier detection",fontsize=14)
plt.xlabel("Theoretical quantiles",fontsize=12)


# In[ ]:


#### Observations from Q-Q plot
-. The data does not follow distribution as the data points are deviating significantly away from the red line
-. The data shows a right-skewed distribution and possible outliers

