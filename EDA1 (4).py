#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[6]:


data.info()


# In[7]:


print(data)


# In[8]:


print(type(data))
print(data.shape)
print(data.size)


# In[9]:


#data1 = data.drop(['Unnamed: 0',"Tem C"], axis =1, inplacec = True)

data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[10]:


data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info()


# In[11]:


data1[data1.duplicated(keep = False)]


# In[12]:


data1[data1.duplicated()]


# In[13]:


data1.drop_duplicates(keep='first', inplace = True)
data1


# In[14]:


data1.rename({'Solar.R': 'Solar'},axis=1, inplace = True)
data1


# In[15]:


data.info()


# In[16]:


data1.isnull().sum()


# In[17]:


cols = data1.columns
colors = ['black','white']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colors),cbar = True)


# In[18]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[19]:


data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[20]:


data1['Solar'] = data1['Solar'].fillna(median_ozone)
data1.isnull().sum()


# In[21]:


median_Solar = data1["Solar"].median()
mean_Solar = data1["Solar"].mean()
print("Median of Solar: ", median_Solar)
print("Mean of Ozone: ", mean_Solar)


# In[22]:


data1['Solar'] = data1['Solar'].fillna(mean_ozone)
data1.isnull().sum()


# In[23]:


data1.head()


# In[24]:


print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[25]:


data1['Weather'] = data1['Weather'].fillna(mean_ozone)
data1.isnull().sum()


# In[26]:


data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[27]:


print(data1["Month"].value_counts())
mode_month = data1["Month"].mode()[0]
print(mode_month)


# In[28]:


data1["Month"] = data1["Month"].fillna(mode_month)
data1.isnull().sum()


# In[30]:


#reset the index column
data1.reset_index(drop=True)


# In[31]:


#Detection of outliers in columns


# In[29]:


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

# In[30]:


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

# In[31]:


plt.figure(figsize=(6,2))
boxplot_data=plt.boxplot(data1["Ozone"],vert=False)
[item.get_xdata() for item in boxplot_data['filters']]


# In[37]:


data1['Ozone'].describe()


# In[32]:


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

# In[34]:


import scipy.stats as stats
plt.figure(figsize=(4,6))
stats.probplot(data1["Solar"],dist="norm",plot=plt)
plt.title("Q-Q plot for outlier detection",fontsize=14)
plt.xlabel("Theoretical quantiles",fontsize=12)


# In[ ]:


#### Observations from Q-Q plot
-. The data does not follow distribution as the data points are deviating significantly away from the red line
-. The data shows a right-skewed distribution and possible outliers


# In[55]:


# Create a figure for violin plot

sns.violinplot(data=data1["Ozone"], color='lightgreen')
plt.title("Violin Plot")

plt.show()


# In[39]:


sns.violinplot(data=data1, x = "Weather", y="Ozone", palette="Set2")


# In[38]:


data1["Weather"].value_counts()


# In[51]:


sns.swarmplot(data=data1, x = "Weather", y = "Ozone",color="Orange",palette="Set2", size=6)


# In[52]:


sns.stripplot(data=data1, x = "Weather", y = "Ozone",color="Orange",palette="Set1", size=6, jitter = True)


# In[53]:


sns.kdeplot(data=data1["Ozone"], fill=True, color="blue")
sns.rugplot(data=data1["Ozone"], color="black")


# In[54]:


data1[data1["Weather"]==41.81512605042017]


# In[50]:


data1["Weather"][87] = 'S'
data1["Weather"][93] = 'S'
data1["Weather"][95] = 'PS'


# In[56]:


sns.boxplot(data = data1, x="Weather", y="Ozone")


# In[57]:


plt.scatter(data1["Wind"], data1["Temp"])


# In[59]:


data1["Wind"].corr(data1["Temp"])


# In[ ]:




